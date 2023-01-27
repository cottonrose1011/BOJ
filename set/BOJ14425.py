n, m = map(int, input().split())
s = set()
array = []
result = 0
for _ in range(n):
    s.add(input())
for _ in range(m):
    array.append(input())
for x in array:
    if x in s:
        result += 1
print(result)
