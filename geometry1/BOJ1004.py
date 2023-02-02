from math import sqrt


t = int(input())
answer = []
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    planet = []
    result = 0
    n = int(input())
    for _ in range(n):
        a, b, c = map(int, input().split())
        planet.append((a, b, c))
    for i in range(len(planet)):
        d1 = sqrt(abs(x1-planet[i][0]) ** 2 + abs(y1-planet[i][1]) ** 2)
        d2 = sqrt(abs(x2 - planet[i][0]) ** 2 + abs(y2 - planet[i][1]) ** 2)
        r = planet[i][2]
        if d1 < r and d2 < r:
            pass
        elif d1 < r or d2 < r:
            result += 1
    answer.append(result)
for x in answer:
    print(x)
