Turning questions into software, one experiment at a time.

[resume (PDF)](Baaqar_Naqi_Resume.pdf) · [email](mailto:baaqarnaqi@gmail.com)

```mermaid
%%{init: {"layout":"dagre","look":"classic","theme":"base","themeVariables":{"primaryColor":"#21262d","primaryTextColor":"#e6edf3","primaryBorderColor":"#8b949e","lineColor":"#7d8590","fontFamily":"ui-sans-serif, -apple-system, 'Segoe UI', sans-serif","fontSize":"14px","edgeLabelBackground":"#0d1117"},"flowchart":{"curve":"linear","nodeSpacing":30,"rankSpacing":45}}}%%
flowchart TD
    ME((Curiosity))

    ME --> SYS(Systems)
    ME --> INT(Intelligence)
    ME --> HUM(Human Understanding)

    SYS --> WEB[Web Technologies]
    SYS --> DIST[Distributed Systems]
    SYS --> OS[Operating Systems]

    INT --> IR[IR & Knowledge Graphs]
    INT --> ML[Machine Learning]

    HUM --> NLP[Language / NLP]
    HUM --> ACC[Accessibility]
    HUM --> RL[Learning & Behaviour]

    OS --> OSTEP([📚 my_ostep_projects])
    ML --> ALGOS([📚 ml_algos])
    DIST --> DDIA([📚 ddia-notes])

    WEB --> ATP([📦 Native Artifacts<br>artifact-to-pwa])
    DIST --> COMM([📦 Peerspace<br>serverless-comm])
    WEB -.-> COMM

    ACC --> DYS([📦 Dyslexia Lens<br>dyslexia-accessibility-nlp])
    NLP -.-> DYS

    IR --> NIE([🔧 Narrative Intelligence Engine])
    NLP --> NIE
    DDIA -.-> NIE

    RL --> ALIEN([🚧 Alien Invasion<br>RL Environment])

    classDef root fill:#2a1e3d,stroke:#bc8cff,stroke-width:2px,color:#d2a8ff
    classDef branch fill:#161b22,stroke:#8b949e,stroke-width:1.5px,color:#e6edf3
    classDef leaf fill:#0d1117,stroke:#484f58,stroke-width:1.5px,color:#c9d1d9
    classDef learn fill:#12261e,stroke:#3fb950,stroke-width:1.5px,color:#7ee787
    classDef project fill:#1c2b3a,stroke:#58a6ff,stroke-width:1.5px,color:#a5d6ff
    classDef tool fill:#2b2416,stroke:#d29922,stroke-width:1.5px,color:#e3b341
    classDef wip fill:#2b1618,stroke:#f85149,stroke-width:1.5px,color:#ff7b72

    class ME root
    class SYS,INT,HUM branch
    class WEB,DIST,OS,IR,ML,NLP,ACC,RL leaf
    class OSTEP,ALGOS,DDIA learn
    class ATP,COMM,DYS project
    class NIE tool
    class ALIEN wip

    linkStyle default stroke:#7d8590,stroke-width:1.5px
```


**Currently**
- ✓ Reading — Designing Data-Intensive Applications (Kleppmann)
- ✓ Building — Narrative Intelligence Engine

<p align="center"><i> "What I cannot create, I do not understand." — Richard Feynman </i></p>
