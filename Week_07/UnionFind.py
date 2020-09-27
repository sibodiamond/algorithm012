class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def union(self, i, j):
        p1 = self.parent(i)
        p2 = self.parent(j)
        self.p[p1] = p2

    def parent(self, i):
        root = i
        while self.p[root] != root:
            root = self.p[root]
        # 通过上面loop使得root指向i的parent
        # 下面loop,使得i到root之间的节点的parent均指向root.
        while self.p[i] != i:
            x = i; i = self.p[i]; self.p[x] = root
        return root
