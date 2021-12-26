class DisjointSet:
    parent = {}
    rank = {}
    def makeSet(self, universe):
        for i in range(universe):
            self.parent[i] = i
            self.rank[i] = 0
 
    def Find(self, k):
 
        if self.parent[k] != k:
            self.parent[k] = self.Find(self.parent[k])
 
        return self.parent[k]
 
    def Union(self, a, b):
 
        x = self.Find(a)
        y = self.Find(b)
 
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] = self.rank[y] + 1
