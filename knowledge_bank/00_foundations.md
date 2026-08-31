# Stage 0 — Foundations: before the Transformer

**Goal:** understand the problems that the Transformer was invented to solve. If
you know *why* attention was added to sequence models, the 2017 paper reads like
an inevitability rather than magic.

---

## 1. The task: sequence modeling

Language is a sequence. Early neural NLP framed most problems as **sequence
modeling**: given tokens so far, predict what comes next (language modeling), or
map one sequence to another (translation, summarization — "sequence-to-sequence").

The dominant tool was the **Recurrent Neural Network (RNN)** and its improved
variants, **LSTM** (Long Short-Term Memory) and **GRU**. An RNN processes tokens
one at a time, carrying a *hidden state* vector forward that is meant to
summarize everything seen so far.

**Two structural problems fall out of this:**

1. **The vanishing/exploding gradient problem.** Signals have to propagate
   through many time steps during training; gradients shrink or blow up, so RNNs
   struggle to learn *long-range* dependencies. LSTMs/GRUs mitigate this with
   gating but don't eliminate it.
2. **It's inherently sequential.** Step *t* depends on step *t−1*, so you cannot
   parallelize across the sequence during training. On modern GPUs — which are
   massively parallel — this is a fundamental throughput ceiling.

## 2. seq2seq and the information bottleneck

The **seq2seq** model (Sutskever et al., 2014) uses an **encoder** RNN to read
the input and compress it into a single fixed-length vector, then a **decoder**
RNN to generate the output from that vector.

The flaw is visible immediately: *one fixed vector* has to hold the entire
meaning of a sentence — or a paragraph. This is the **information bottleneck**.
The longer the input, the worse it gets.

## 3. Attention as the fix (Bahdanau, 2014)

**Attention** removed the bottleneck. Instead of forcing the encoder into one
vector, keep *all* the encoder's per-token hidden states. At each decoding step,
compute a set of weights over the input tokens — how much to "attend" to each —
and form a **weighted sum** of their representations. The decoder now looks back
at the *whole* input and focuses on the relevant parts for each output word.

This is the key idea to internalize:

> Attention = a learned, content-based, weighted lookup. For a given query, score
> every candidate, softmax the scores into weights, and return the weighted
> average of the candidates' values.

That single sentence is, essentially, all of "scaled dot-product attention" in
Stage 1 — just without the RNN wrapped around it.

## 4. Representations: word embeddings

Running underneath all of this: **distributed representations**. Rather than
treating words as atomic symbols, map each to a dense vector where geometry
encodes meaning (*king − man + woman ≈ queen*). **word2vec** (Mikolov, 2013) and
**GloVe** (Pennington, 2014) popularized static embeddings; **ELMo** (Stage 2)
later made them *contextual*. Embeddings are the input layer of every model you
will study from here on.

---

## Checkpoints — you should be able to explain…
- Why RNN-based sequence models can't be parallelized across the sequence.
- What the "information bottleneck" in vanilla seq2seq is, and how attention
  removes it.
- The query/score/softmax/weighted-sum pattern of attention, in words.
- What a word embedding is and why dense vectors beat one-hot symbols.

## Reading list
- **Primary — Bahdanau, Cho, Bengio (2014), _Neural Machine Translation by
  Jointly Learning to Align and Translate_.** The paper that introduced
  attention to seq2seq. arXiv:1409.0473
- **Sutskever, Vinyals, Le (2014), _Sequence to Sequence Learning with Neural
  Networks_.** arXiv:1409.3215
- **Explainer — Christopher Olah, _Understanding LSTM Networks_** (colah's blog).
  The clearest visual explanation of LSTMs; still the standard reference.
- **Explainer — Jay Alammar, _Visualizing A Neural Machine Translation Model
  (Seq2seq with Attention)_.** Builds the intuition you'll reuse in Stage 1.
- *Optional* — Mikolov et al. (2013), word2vec (arXiv:1301.3781).

## Bridge to Stage 1
Attention worked, but it was still bolted onto a slow, sequential RNN. The 2017
question was radical: *what if attention were the whole model, and we threw the
recurrence away entirely?* That's Stage 1.
