T = int(input())
answer = list()
for _ in range(T):
    k = int(input())
    n = int(input())

    array = [[0]*14 for _ in range(k+1)]

    for i in range(len(array[0])):
        array[0][i] = i+1
    for i in range(len(array)):
        array[i][0] = 1

    for i in range(1, len(array)):
        for x in range(1, len(array[0])):
            array[i][x] = array[i][x-1] + array[i-1][x]

    answer.append(array[k][n-1])
for data in answer:
    print(data)
