from math import sqrt

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
    rp = r1 + r2
    rm = abs(r2-r1)
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == rp or d == rm:
            print(1)
        elif rp > d > rm:
            print(2)
        else:
            print(0)
            