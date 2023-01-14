import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def reversed_dfs(r):
    global visited, graph, count
    visited[r] = count
    graph[r].sort(reverse=True)
    for i in graph[r]:
        if visited[i] == 0:
            count += 1
            reversed_dfs(i)


n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
count = 1
visited = [0] * (n+1)
for _ in range(1, m+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

reversed_dfs(r)

for j in range(1, n+1):
    print(visited[j])
