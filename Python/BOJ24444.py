import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
# 인터프리터 오류


def bfs(vertex):
    global graph, visited, count
    visited[vertex] = count
    queue = deque()
    queue.append(vertex)
    while queue:
        v = queue.popleft()
        graph[v].sort()
        for x in graph[v]:
            if visited[x] == 0:
                count += 1
                queue.append(x)
                visited[x] = count


n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1

for _ in range(1, m+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(r)

for i in visited[1:]:
    print(i)

