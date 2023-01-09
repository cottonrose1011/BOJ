import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def bfs_reverse(r):
    global count
    visited[r] = count
    queue = deque([r])
    while queue:
        v = queue.popleft()
        graph[v].sort(reverse=True)
        for x in graph[v]:
            if visited[x] == 0:
                count += 1
                queue.append(x)
                visited[x] = count


n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs_reverse(r)

for i in visited[1:]:
    print(i)
