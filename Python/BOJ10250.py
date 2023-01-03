T = int(input())
answer = list()
for _ in range(T):
    h, w, n = map(int, input().split())
    wCount = 0
    hCount = 0
    for i in range(n):
        if i % h == 0:
            hCount += 1
            wCount = 0
        wCount += 1

    if hCount < 10:
        answer.append(str(wCount) + "0" + str(hCount))
    else:
        answer.append(str(wCount) + str(hCount))
    h = 0
    w = 0
    n = 0

for data in answer:
    print(data)
