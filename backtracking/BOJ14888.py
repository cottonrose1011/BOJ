def dfs(depth, num):
    global plus, minus, multi, div, max_value, min_value

    if depth == n:
        max_value = max(num, max_value)
        min_value = min(num, min_value)
    else:
        if plus > 0:
            plus -= 1
            dfs(depth + 1, num + array[depth])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(depth + 1, num - array[depth])
            minus += 1
        if multi > 0:
            multi -= 1
            dfs(depth + 1, num * array[depth])
            multi += 1
        if div > 0:
            div -= 1
            dfs(depth + 1, int(num / array[depth]))
            div += 1


n = int(input())
array = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
max_value = -1e9
min_value = 1e9

dfs(1, array[0])

print(max_value)
print(min_value)
