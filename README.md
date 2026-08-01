# Baaqar Naqi

CS undergraduate. Systems, machine learning, retrieval.

[Now](#now) · [Systems](#systems) · [Applied](#applied) · [Archive](#archive) · [Log](#log)

---

## Now

**Narrative Intelligence Engine** — a retrieval pipeline for novels that tracks how character relationships change over the course of a story, not just what's true about them at a single point in time.

*In design. No public repo yet.*

```
Dataset
  ↓  Entity Canonicalization
  ↓  Knowledge Graph
  ↓  Temporal Layer
  ↓  Vector Embeddings
  ↓  Hybrid Retrieval
  ↓  LLM
  ↓  Answer
```

Most RAG systems treat facts as timeless — a relationship either holds or it doesn't. Fiction breaks that assumption constantly: two characters are allies in chapter 3 and enemies by chapter 20, and a query about "their relationship" only makes sense with a *when* attached to it. That's what the temporal layer is for — versioning graph edges instead of overwriting them, so retrieval can answer "what was true at this point in the story," not just "what's true now."

The harder open question is entity canonicalization across a novel's own inconsistency — the same character referred to by name, nickname, title, and pronoun, sometimes within one paragraph, with resolution that has to work without ever having seen the book before.

Reading **Designing Data-Intensive Applications** (Kleppmann) alongside this, mainly because the temporal layer's correctness depends on storage and consistency guarantees I'd rather verify than assume.

---

## Systems

**[artifact-to-pwa](https://github.com/Baaqar-007/artifact-to-pwa)** — converts a Claude-generated HTML or React artifact into an installable, offline-capable app with no build step. Published as `@baaqar/artifact-to-pwa` on npm.

The offline behavior depends on `localStorage` calls staying synchronous while the actual writes move to IndexedDB, since that's the only store a service worker can persist to. The shim mirrors state in memory and returns immediately, then queues the real write behind it:

```
call setItem()
  → memory mirror updated, returns instantly
  → IndexedDB put() queued
       → commits after current task
       → survives navigation / tab close
       → does not survive a crash inside this gap
```

That gap is small — a few milliseconds — but it's real, and it's the actual shape of the durability guarantee IndexedDB gives you, not an approximation of it.

**[serverless-comm](https://github.com/Baaqar-007/serverless-comm)** — peer-to-peer video, chat, and file transfer over WebRTC, with local AI running client-side in Web Workers. No backend server.

Removing the server doesn't remove the coordination problem, it just relocates it: two peers who've never spoken have to find each other and exchange connection metadata before WebRTC can take over. Handled with STUN first — each peer asks a public STUN server what its own reachable address looks like from outside its NAT, then the two exchange those addresses directly. That fails against symmetric NAT or a firewall that blocks the direct path, which is where TURN comes in as a fallback: a relay server both peers can reach, forwarding traffic between them when a direct connection isn't possible. STUN when it can be direct, TURN when it can't — the server stays out of the data path either way, it just helps two strangers find each other.

---

## Applied

**[dyslexia-accessibility-nlp](https://github.com/Baaqar-007/dyslexia-accessibility-nlp)** — NLP applied to make text more readable for people with dyslexia. The harder part wasn't the model; it was learning enough about how dyslexia actually affects reading to know what "more readable" should mean.

---

## Archive

Earlier work, compressed:

- **[my_ostep_projects](https://github.com/Baaqar-007/my_ostep_projects)** — CPU scheduling and memory management from the OSTEP problem sets, in C. FCFS through stride scheduling, free-space allocators, by hand.
- **[ml_algos](https://github.com/Baaqar-007/ml_algos)** — decision trees, GLMs, SVMs, MLPs, and clustering, derived from the underlying math instead of imported.
- Two smaller exercises (an arcade game, a Flask blog) aren't listed individually — lower signal, but part of how the above got approachable.

---

## Log

<!--START_SECTION:activity-->
<!--END_SECTION:activity-->

Updates once daily. If the dates above stop moving, the workflow stopped — not the work.

---

[linkedin](https://www.linkedin.com/in/baaqar-naqi-910332217/) · [leetcode](https://leetcode.com/u/Baaqar-007/) · [instagram](https://www.instagram.com/baaqarnaqi/)

<!-- if you're reading this in source rather than rendered: hi. -->
