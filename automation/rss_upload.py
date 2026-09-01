#!/usr/bin/env python3
"""Create an UNPUBLISHED draft episode on RSS.com for The GenAI Evolution Atlas.

This uploads a generated podcast episode to RSS.com as a *draft* so the owner
can review it and press publish. It never publishes on its own.

Flow (per RSS.com's documented API shape):
  1. Authenticate with the account API key via the `X-API-Key` header.
  2. Resolve the show id for "The GenAI Evolution Atlas".
  3. Register the episode audio from its public download URL -> get an audio id.
  4. Create the episode (season 2, the episode number, title, description,
     the audio id) in a DRAFT / unpublished state.
  5. Record the resulting episode id + status back into podcasts/episodes.json.

Requirements:
  - An RSS.com **Network plan** (the API is gated to it).
  - The API key in the env var `RSS_API_KEY` (never commit it).
  - Outbound egress to api.rss.com (this repo's automation environments block
    it by policy — run this locally, or in an environment whose network policy
    allows api.rss.com).

Usage:
  export RSS_API_KEY=...                 # from RSS.com account settings
  python3 automation/rss_upload.py --episode 1            # dry-run (default)
  python3 automation/rss_upload.py --episode 1 --yes      # actually create draft
  python3 automation/rss_upload.py --list-shows           # discover show id

⚠️  SCHEMA-TO-CONFIRM: the exact endpoint paths, request field names, and the
    draft/unpublished flag below are built from RSS.com's public description of
    the API (X-API-Key auth; "pass the file's download URL ... returns an audio
    upload id ... a second call to create the episode"). They are isolated in
    the `API` block so they can be reconciled against the authoritative docs at
    https://api.rss.com/v4/docs in one place. On any 4xx the script prints the
    full response body so the field names can be corrected quickly.
"""
import argparse
import json
import os
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MANIFEST = REPO / "podcasts" / "episodes.json"
SHOW_NAME = "The GenAI Evolution Atlas"


# ─── API shape — reconcile against https://api.rss.com/v4/docs ───────────────
class API:
    BASE = "https://api.rss.com/v4"
    # endpoints (relative to BASE)
    SHOWS = "/shows"                        # GET  -> list shows
    AUDIO = "/audio"                        # POST -> register audio by URL, returns id
    EPISODES = "/shows/{show_id}/episodes"  # POST -> create episode

    # request field names for "create episode"
    F_TITLE = "title"
    F_DESCRIPTION = "description"
    F_SEASON = "season"
    F_EPISODE = "episode"
    F_AUDIO_ID = "audio_id"
    # draft/unpublished: RSS.com exposes a status/visibility flag; set it to the
    # non-public value so the owner publishes manually. Confirm the exact key +
    # value against the docs ("draft" | "unpublished" | published:false, etc.).
    F_STATUS = "status"
    STATUS_DRAFT = "draft"

    # field name for "register audio by URL"
    F_AUDIO_URL = "url"
    # key under which the created-audio id comes back
    R_AUDIO_ID = "id"
    # key under which the created-episode id comes back
    R_EPISODE_ID = "id"
# ─────────────────────────────────────────────────────────────────────────────


def _opener():
    """urllib opener honoring the agent proxy + CA bundle when present."""
    ctx = ssl.create_default_context()
    ca = os.environ.get("SSL_CERT_FILE") or "/root/.ccr/ca-bundle.crt"
    if os.path.exists(ca):
        try:
            ctx.load_verify_locations(ca)
        except Exception:
            pass
    handlers = [urllib.request.HTTPSHandler(context=ctx)]
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if proxy:
        handlers.append(urllib.request.ProxyHandler({"https": proxy, "http": proxy}))
    return urllib.request.build_opener(*handlers)


def _request(method, path, api_key, body=None):
    url = API.BASE + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("X-API-Key", api_key)
    req.add_header("Accept", "application/json")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with _opener().open(req, timeout=120) as resp:
            raw = resp.read().decode()
            return resp.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        print(f"  ! HTTP {e.code} {method} {url}\n    {detail}", file=sys.stderr)
        raise
    except urllib.error.URLError as e:
        print(f"  ! network error {method} {url}: {e.reason}", file=sys.stderr)
        print("    (api.rss.com is egress-blocked in this repo's automation "
              "environments — run this locally.)", file=sys.stderr)
        raise


def load_manifest():
    return json.loads(MANIFEST.read_text())


def save_manifest(m):
    MANIFEST.write_text(json.dumps(m, indent=2) + "\n")


def find_episode(manifest, number):
    for ep in manifest.get("episodes", []):
        if ep.get("episode") == number:
            return ep
    return None


def known_show_id(manifest):
    """Show id from env or manifest, without any network call (None if unknown)."""
    return os.environ.get("RSS_SHOW_ID") or manifest.get("rss_show_id")


def resolve_show_id(api_key, manifest):
    known = known_show_id(manifest)
    if known:
        return known
    _, shows = _request("GET", API.SHOWS, api_key)
    items = shows if isinstance(shows, list) else shows.get("data", shows.get("shows", []))
    for s in items:
        if str(s.get("title", s.get("name", ""))).strip().lower() == SHOW_NAME.lower():
            return s.get("id") or s.get("show_id")
    raise SystemExit(f"Could not find show {SHOW_NAME!r}. Shows seen: "
                     + ", ".join(str(s.get("title", s.get("name"))) for s in items))


def list_shows(api_key):
    _, shows = _request("GET", API.SHOWS, api_key)
    print(json.dumps(shows, indent=2))


def create_draft(api_key, ep, show_id, season, dry_run):
    audio_url = ep["audio_url"]
    reg_body = {API.F_AUDIO_URL: audio_url}
    ep_body = {
        API.F_TITLE: ep["title"],
        API.F_DESCRIPTION: ep["description"],
        API.F_SEASON: season,
        API.F_EPISODE: ep["episode"],
        API.F_STATUS: API.STATUS_DRAFT,
        # F_AUDIO_ID is filled in after the audio is registered
    }
    ep_path = API.EPISODES.format(show_id=show_id)

    print(f"  show_id       : {show_id}")
    print(f"  audio (URL)   : POST {API.BASE}{API.AUDIO}  {reg_body}")
    print(f"  episode       : POST {API.BASE}{ep_path}")
    print(f"                  {json.dumps({**ep_body, API.F_AUDIO_ID: '<from audio step>'})}")

    if dry_run:
        print("  (dry-run — nothing sent. Re-run with --yes to create the draft.)")
        return None

    _, audio = _request("POST", API.AUDIO, api_key, reg_body)
    audio_id = audio.get(API.R_AUDIO_ID)
    if not audio_id:
        raise SystemExit(f"No audio id in response: {audio}")
    ep_body[API.F_AUDIO_ID] = audio_id
    _, created = _request("POST", ep_path, api_key, ep_body)
    episode_id = created.get(API.R_EPISODE_ID)
    print(f"  ✓ draft created: episode_id={episode_id} (UNPUBLISHED)")
    return {"episode_id": episode_id, "audio_id": audio_id}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--episode", type=int, help="episode number from episodes.json")
    ap.add_argument("--list-shows", action="store_true", help="print your RSS.com shows and exit")
    ap.add_argument("--yes", action="store_true",
                    help="actually create the draft (default is dry-run)")
    args = ap.parse_args()

    api_key = os.environ.get("RSS_API_KEY")
    if not api_key:
        raise SystemExit("RSS_API_KEY is not set. Export your RSS.com API key first.")

    if args.list_shows:
        list_shows(api_key)
        return
    if args.episode is None:
        raise SystemExit("Pass --episode N (or --list-shows).")

    manifest = load_manifest()
    ep = find_episode(manifest, args.episode)
    if ep is None:
        raise SystemExit(f"Episode {args.episode} not found in {MANIFEST}.")
    if ep.get("rss_status") == "published":
        raise SystemExit(f"Episode {args.episode} is already published — refusing.")

    season = ep.get("season", manifest.get("season", 2))
    # Resolve the show id over the network only when actually sending; a dry-run
    # uses whatever is known locally (or a placeholder) and stays offline.
    if args.yes:
        show_id = resolve_show_id(api_key, manifest)
    else:
        show_id = known_show_id(manifest) or "<resolved at send time>"

    print(f"Episode S{season}E{ep['episode']:02d} — {ep['title']!r}")
    result = create_draft(api_key, ep, show_id, season, dry_run=not args.yes)

    if result:
        ep["rss_status"] = "draft"
        ep["rss_episode_id"] = result["episode_id"]
        if not manifest.get("rss_show_id"):
            manifest["rss_show_id"] = show_id
        save_manifest(manifest)
        print(f"  updated {MANIFEST.relative_to(REPO)} (rss_status=draft). "
              "Review it on RSS.com and publish when ready.")


if __name__ == "__main__":
    main()
