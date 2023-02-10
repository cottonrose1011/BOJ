import sys
input = sys.stdin.readline


def dfs(depth, idx):
    global minV
    if depth == n//2:
        team_start = 0
        team_link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    team_start += array[i][j]
                elif not visited[i] and not visited[j]:
                    team_link += array[i][j]
        minV = min(minV, abs(team_link - team_start))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i+1)
            visited[i] = 0


n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [0]*n
minV = 1e9
dfs(0, 0)
print(minV)
