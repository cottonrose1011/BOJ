n = int(input())
data = list()
for i in range(n):
    data.append(input())

count = 0
s1 = set()
for x in data:
    s1.clear()
    isGroup = 1
    for i in range(len(x)):
        if i == 0:
            s1.add(x[i])
        if i >= 1 and x[i] != x[i-1]:
            if x[i] not in s1:
                s1.add(x[i])
            else:
                isGroup = 0
                break
                # 그 다음 반복문으로 넘어감
    if isGroup == 1:
        count += 1

print(count)
