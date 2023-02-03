def dfs(depth, s, n, m):
    if depth == m:
        print(' '.join(map(str, array)))
        return
    for i in range(s, n):
        if not visited[i]:
            array.append(i + 1)
            dfs(depth+1, i, n, m)
            visited[i] = False
            array.pop()


n, m = map(int, input().split())
array = []
visited = [False] * n
dfs(0, 0, n, m)
