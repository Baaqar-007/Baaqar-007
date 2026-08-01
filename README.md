<div align="center">

<img src="assets/threshold.svg" width="100%" alt=""/>

# Baaqar Naqi

<img src="https://readme-typing-svg.demolab.com/?font=Georgia&size=16&pause=1400&color=B08D57&background=00000000&center=true&vCenter=true&width=560&height=32&repeat=false&lines=Notes+kept+while+learning+how+things+actually+work." alt="Notes kept while learning how things actually work."/>

<sub>CS undergraduate · systems · machine learning · narrative</sub>

<br/>

[Juvenilia](#juvenilia) · [Working Papers](#working-papers) · [The Manuscript](#the-manuscript) · [Marginalia](#marginalia) · [Colophon](#colophon)

<br/>

<img src="assets/divider.svg" width="100%" alt=""/>

</div>

<br/>

## Juvenilia

The early pieces. Kept because scrapping them would mean forgetting what they taught.

**[my_ostep_projects](https://github.com/Baaqar-007/my_ostep_projects)** · `C`
CPU scheduling and memory management, worked through by hand from the OSTEP problem sets. Implementing lottery scheduling made the tradeoff between fairness and throughput concrete in a way reading about it never did.

**[ml_algos](https://github.com/Baaqar-007/ml_algos)** · `Makefile`
Decision trees, GLMs, SVMs, MLPs, and clustering, derived from the underlying math instead of imported. Backpropagation stopped being a black box once I'd worked out the chain rule for it myself, mistakes included.

**[serverless-comm](https://github.com/Baaqar-007/serverless-comm)** · `JavaScript`
Peer-to-peer video, chat, and file transfer over WebRTC, with no backend server. Removing the server didn't remove the coordination problem — it just moved it into signaling, which turned out to be the harder half.

**[dyslexia-accessibility-nlp](https://github.com/Baaqar-007/dyslexia-accessibility-nlp)** · `Jupyter Notebook`
NLP applied to make text more readable for people with dyslexia. The harder part wasn't the model — it was learning enough about how dyslexia actually affects reading to know what "more readable" should mean.

A couple of earlier exercises — a small arcade game, a Flask blog — aren't listed individually. They taught less, but they're part of why the OSTEP work was approachable at all.

<sub>[↑ catalogue](#baaqar-naqi)</sub>

<br/>

<img src="assets/divider.svg" width="100%" alt=""/>

<br/>

## Working Papers

**[artifact-to-pwa](https://github.com/Baaqar-007/artifact-to-pwa)** began as a short weekend utility — turning a Claude-generated HTML or React artifact into an installable, offline-capable app without a build step.

To work offline, calls to `localStorage` needed to keep behaving exactly as they always had — synchronous, instant — while the actual data moved to IndexedDB in the background, since that's the only persistent store a service worker can rely on. The shim mirrors state in memory and returns immediately, then queues an IndexedDB `put()` behind it.

Someone asked, reasonably, what happens to that last write if the tab closes in the gap between the call returning and the transaction committing. It survives — the queued transaction still completes on navigation or a normal tab close. It does not survive a hard crash inside that same window. That isn't a flaw so much as the actual shape of the guarantee IndexedDB gives you, one most people who use it never have reason to look at directly.

<sub>published as `@baaqar/artifact-to-pwa` on npm</sub>

<sub>[↑ catalogue](#baaqar-naqi)</sub>

<br/>

<img src="assets/divider.svg" width="100%" alt=""/>

<br/>

## The Manuscript

Most retrieval systems answer a question by ignoring when something was true and where it came from. This one doesn't get to — a **Narrative Intelligence Engine**:

<!-- TODO: link the repo here once it's public — [Narrative Intelligence Engine](#) -->

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

Reading **Designing Data-Intensive Applications** (Kleppmann) alongside it, for the same reason the pipeline has a temporal layer at all — storage and consistency guarantees are easy to assume and hard to actually verify.

<sub>[↑ catalogue](#baaqar-naqi)</sub>

<br/>

<img src="assets/divider.svg" width="100%" alt=""/>

<br/>

## Marginalia

*Added automatically. Not curated.*

<!--START_SECTION:activity-->
<!--END_SECTION:activity-->

<sub>if this hasn't moved in a while, the workflow is quiet, not broken</sub>

<sub>[↑ catalogue](#baaqar-naqi)</sub>

<br/>

<img src="assets/divider.svg" width="100%" alt=""/>

<br/>

## Colophon

Printed by **Baaqar Naqi**, CS undergraduate, working from UTC−12.

<!-- TODO: optional — a small portrait or personal mark, e.g. <img src="assets/mark.png" width="48"/> -->

[linkedin](https://www.linkedin.com/in/baaqar-naqi-910332217/) · [leetcode](https://leetcode.com/u/Baaqar-007/) · [instagram](https://www.instagram.com/baaqarnaqi/)
