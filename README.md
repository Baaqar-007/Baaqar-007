<div align="center">

<img src="assets/threshold.svg" width="100%" alt="a gate, glowing faintly"/>

<!-- TODO: this arch is hand-coded line art — swap for your own illustration here if you want something more personal -->

# Baaqar Naqi

<img src="https://readme-typing-svg.demolab.com/?font=Georgia&size=17&pause=1200&color=C9A227&background=00000000&center=true&vCenter=true&width=560&height=40&repeat=false&lines=Every+system+tells+a+story%2C+if+you+read+closely+enough." alt="Every system tells a story, if you read closely enough."/>

<sub>CS undergrad · systems · machine learning · narrative</sub>

<br/>

### The Doors

[![I · Apprentice Pieces](https://img.shields.io/badge/I%20·%20Apprentice%20Pieces-C9A227?style=flat-square)](#i-apprentice-pieces)
[![II · The Grimoire](https://img.shields.io/badge/II%20·%20The%20Grimoire-C9A227?style=flat-square)](#ii-the-grimoire)
[![III · The Present Work](https://img.shields.io/badge/III%20·%20The%20Present%20Work-C9A227?style=flat-square)](#iii-the-present-work)
[![Marginalia](https://img.shields.io/badge/Marginalia-C9A227?style=flat-square)](#marginalia)
[![Colophon](https://img.shields.io/badge/Colophon-C9A227?style=flat-square)](#colophon)

<img src="assets/divider.svg" width="100%" alt=""/>

</div>

## I. Apprentice Pieces

> *Every worked craft begins with pieces made only to learn the tool.*

The early ones stay on the shelf — scrapping them would mean forgetting what they taught.

**[my_ostep_projects](https://github.com/Baaqar-007/my_ostep_projects)** `C`
CPU scheduling — FCFS, SJF, SRTF, RR, lottery, stride — and free-space management, worked through by hand from the OSTEP problem sets.

**[ml_algos](https://github.com/Baaqar-007/ml_algos)** `Makefile`
Decision trees, GLMs, SVMs, MLPs, and clustering — each derived from the underlying math rather than imported.

**[serverless-comm](https://github.com/Baaqar-007/serverless-comm)** `JavaScript`
Peer-to-peer video, chat, and file transfer over WebRTC, with local AI running client-side in Web Workers. No server in sight.

**[dyslexia-accessibility-nlp](https://github.com/Baaqar-007/dyslexia-accessibility-nlp)** `Jupyter Notebook`
NLP applied somewhere it could actually help — text made more readable for people with dyslexia.

<sub>[↑ back to the doors](#the-doors)</sub>

<img src="assets/divider.svg" width="100%" alt=""/>

## II. The Grimoire

> *A spell cast quickly can still teach you something you didn't ask to learn.*

**[artifact-to-pwa](https://github.com/Baaqar-007/artifact-to-pwa)** started as a weekend fix — turning a Claude-built HTML/React artifact into an installable app with one command, no Webpack, no manifest wrangling by hand. Published as [`@baaqar/artifact-to-pwa`](https://www.npmjs.com/package/@baaqar/artifact-to-pwa) on npm.

<details>
<summary><b>unseal the grimoire</b> — what it ended up teaching me</summary>
<br/>

It became something else once people started using it. The trick underneath — making `localStorage` calls resolve instantly while quietly persisting to IndexedDB in the background — opened a real question in the comments: what happens to the last write if the app dies in the gap between the call returning and the transaction committing?

Answering it properly meant actually understanding IndexedDB's transaction lifecycle, not just calling its API — `setItem` updates an in-memory mirror synchronously, then queues an IndexedDB `put()` that commits after the current task finishes. Safe across tab closes and navigation. Not safe against a hard crash in that few-millisecond window. Worth a line in the README; worth more as a lesson in what "instant" actually means underneath.

</details>

<sub>[↑ back to the doors](#the-doors)</sub>

<img src="assets/divider.svg" width="100%" alt=""/>

## III. The Present Work

> *Every answer is a small story, told from evidence.*

A retrieval-augmented pipeline, built because most RAG systems forget that facts have a *when* and a *where*, not just a *what* — a **Narrative Intelligence Engine**:

<!-- TODO: add the repo link here once it's public — [Narrative Intelligence Engine](#) -->

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

Reading **Designing Data-Intensive Applications** (Kleppmann) alongside it — mostly because I'd rather understand how the storage and consistency guarantees underneath a system like this actually work than assume them.

<sub>[↑ back to the doors](#the-doors)</sub>

<img src="assets/divider.svg" width="100%" alt=""/>

## Marginalia

<!--START_SECTION:activity-->
<!--END_SECTION:activity-->

<sub>added automatically, once a day — not written by hand</sub>

<sub>[↑ back to the doors](#the-doors)</sub>

<img src="assets/divider.svg" width="100%" alt=""/>

## Colophon

Printed by **Baaqar Naqi**, CS undergrad, somewhere at UTC−12.

<!-- TODO: add a small portrait or personal sigil here if you'd like one, e.g. <img src="assets/sigil.png" width="60"/> -->

[![LinkedIn](https://img.shields.io/badge/LinkedIn-C9A227?style=flat-square&logo=linkedin&logoColor=0D1117)](https://www.linkedin.com/in/baaqar-naqi-910332217/)
[![LeetCode](https://img.shields.io/badge/LeetCode-C9A227?style=flat-square&logo=leetcode&logoColor=0D1117)](https://leetcode.com/u/Baaqar-007/)
[![Instagram](https://img.shields.io/badge/Instagram-C9A227?style=flat-square&logo=instagram&logoColor=0D1117)](https://www.instagram.com/baaqarnaqi/)
