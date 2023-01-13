# 수 정렬하기
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

for i in range(len(array)):
    for j in range(len(array)):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]

for data in array:
    print(data)
