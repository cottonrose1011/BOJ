t = int(input())
array = []
for _ in range(t):
    array.append(input())
for data in range(t):
    result = array[data][0]+array[data][-1]
    print(result)
