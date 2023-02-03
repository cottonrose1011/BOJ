def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, array)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            array.append(i)
            dfs(depth+1, n, m)
            visited[i] = False
            array.pop()


n, m = map(int, input().split())
array = []
visited = [False] * (n + 1)
dfs(0, n, m)
