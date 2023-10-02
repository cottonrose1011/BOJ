n, m = map(int, input().split())
array = [0] * (n+1)
for x in range(1, n+1):
    array[x] = x
for x in range(m):
    i, j = map(int, input().split())
    temp = array[i: j+1]
    temp.reverse()
    array[i: j+1] = temp
for i in range(1, n+1):
    print(array[i], end=" ")
