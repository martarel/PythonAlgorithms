#Distance queries (find distance from node A to B) in O(log(n)) using lowest common ancestor (O(n)log(n)) to build
import math
import sys
sys.setrecursionlimit(10**6)
def dfs(u, p, memo, lev, log, g):
    memo[u][0] = p
    for i in range(1, log + 1):
        memo[u][i] = memo[memo[u][i - 1]][i - 1]
         
    for v in g[u]:
        if v != p:
            lev[v] = lev[u] + 1
            dfs(v, u, memo, lev, log, g)
 
def lca(u, v, log, lev, memo):
    if lev[u] < lev[v]:
        u, v = v, u
    for i in range(log, -1, -1):
        if (lev[u] - pow(2, i)) >= lev[v]:
            u = memo[u][i]   
    if u == v:
        return v
    for i in range(log, -1, -1):
        if memo[u][i] != memo[v][i]:
            u = memo[u][i]
            v = memo[v][i]    
    return memo[u][0]


n, q = map(int, input().split())
log = math.ceil(math.log(n, 2))
memo = [[-1 for i in range(log + 1)] for j in range(n+1)]
tree = [[] for _ in range(n + 1)]
lev = [0 for i in range(n + 1)]
for _ in range(n-1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)
dfs(1, 1, memo, lev, log, tree)
for query in range(q):
  a, b = map(int, input().split())
  lc = lca(a, b, log, lev, memo)
  ans = lev[a] + lev[b] - (2 * lev[lc])
  print(ans)

#----------------------------------
  
#Find Centroid (can be used for centroid decomposition
n = int(input())
tree = [[] for _ in range(n)]
for edge in range(n-1):
  a, b = map(int, input().split())
  tree[a-1].append(b-1)
  tree[b-1].append(a-1)
size = [0 for _ in range(n)]
maxi = n//2
def find(u, p):
  size[u] = 1
  for v in tree[u]:
    if v != p:
      find(v, u)
      size[u] += size[v]
def centroid(u, p, sz):
  for v in tree[u]:
    if p != v:
      if size[v] * 2 > sz:
        return centroid(v, u, sz)
  return u

find(0, -1) 
ans = centroid(0, -1, n )
print(ans+1)



#----------------------------------

#Euler tour technique (flatten tree to array to speed up queries)
MX = 10**6
n, m = map(int, input().split())
tree = [[] for _ in range(n)]
timer = 0
start = [MX for _ in range(n)]
end = [MX for _ in range(n)]
for edge in range(m):
  a, b = map(int, input().split())
  tree[a-1].append(b-1)
  tree[b-1].append(a-1)


def dfs(node, parent):
  global timer
  start[node] = timer
  timer += 1
  for neigh in tree[node]:
    if neigh != parent:
      dfs(neigh, node)
  end[node] = timer - 1



#----------------------------------

#Heavy light decomposition on trees (implement specific queries separately)
n = int(input())
graph = [[] * n]
for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
depth = [] * n
parent = [] * n
heavy = [-1] * n
head = [] * n
pos = [] * n
curr = 0

def dfs(v):
  size = 1
  max_c_size = 0
  for c in graph[v]:
    parent[c] = v
    depth[c] = depth[v] + 1
    c_size = dfs(c)
    size += c_size
    if c_size > max_c_size:
      max_c_size = c_size
      heavy[v] = c
  return size 

def decompose(v, h):
  global curr 
  head[v] = h
  curr += 1
  pos[v] = curr
  if heavy[v] != -1:
    decompose(heavy[v], h)
  for c in graph[v]:
    if c != parent[v] and c!= heavy[v]:
      decompose(c, c)

dfs(0)
decompose(0, 0)





