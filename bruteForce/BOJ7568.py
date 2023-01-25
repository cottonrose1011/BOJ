n = int(input())
array = []
rank = [0]*n
count = 1
for _ in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

for i in range(n):
    for j in range(n):
        if array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            count += 1
    rank[i] = count
    count = 1

for x in rank:
    print(x, end=" ")
