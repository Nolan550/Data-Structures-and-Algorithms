class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


def kruskal(vertices, edges):
    edges.sort()
    ds = DisjointSet(vertices)
    mst = []
    total_weight = 0

    for w, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight


if __name__ == "__main__":
    V = 4
    edges = [
        (10, 0, 1),
        (6, 0, 2),
        (5, 0, 3),
        (15, 1, 3),
        (4, 2, 3)
    ]

    mst, cost = kruskal(V, edges)

    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")
    print("Total cost:", cost)
