import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(vertex):
    global array, visited, count
    visited[vertex] = True
    for j in array[vertex]:
        if not visited[j]:
            count += 1
            number[j] = count
            dfs(j)


n, m, r = map(int, input().split())
array = [[] for _ in range(n+1)]
visited = [False] * (n+1)
number = [0] * (n+1)
count = 1
number[r] = count

for i in range(m):
    v, d = map(int, input().split())
    array[v].append(d)
    array[d].append(v)

for data in array:
    data.sort()

dfs(r)

for k in range(1, n+1):
    print(number[k])
