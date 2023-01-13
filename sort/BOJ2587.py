# 대표값2
array = []
for _ in range(5):
    array.append(int(input()))
array.sort()
print(sum(array)//5)
print(array[2])
