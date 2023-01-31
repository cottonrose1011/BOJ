import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = {}
count = 0
array = []

for _ in range(n+m):
    name = input().rstrip()
    if name not in result:
        result[name] = 1
    else:
        result[name] += 1

for x in result:
    if result[x] > 1:
        count += 1
        array.append(x)
array.sort()

print(count)
for x in array:
    print(x)
