# Graph Algorithms

This folder contains implementations of **core graph algorithms** commonly used in
computer science, networking, and algorithm design.

The purpose of this directory is to provide a **high-level overview** of all graph-related
algorithms in the repository. Each algorithm category is organized into its own subfolder,
and **each subfolder contains its own `README.md`** with detailed explanations of the
algorithms implemented there.


## Folder Structure

```text
graph/
│
├── traversal/              # Graph traversal algorithms
│   ├── bfs.*
│   ├── dfs.*
│   └── README.md           # Traversal theory, complexity, and usage
│
├── shortest_path/          # Shortest path algorithms
│   ├── dijkstra.*
│   ├── bellman_ford.*
│   └── README.md           # Shortest path explanations
│
├── mst/                    # Minimum Spanning Tree algorithms
│   ├── kruskal.*
│   ├── prim.*
│   └── README.md           # MST theory and implementations
│
└── README.md               # (This file) Graph algorithms overview
