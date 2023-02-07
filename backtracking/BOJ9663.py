def check(depth):
    for i in range(depth):
        if visited[depth] == visited[i] or abs(visited[depth]-visited[i]) == depth - i:
            return False
    return True


def dfs(depth):
    global count
    if depth == n:
        count += 1
    else:
        for i in range(n):
            visited[depth] = i
            if check(depth):
                dfs(depth + 1)


n = int(input())
count = 0
visited = [0] * n
dfs(0)
print(count)
