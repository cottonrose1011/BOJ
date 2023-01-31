x, y, w, h = map(int, input().split())
w1 = w - x
h1 = h - y

print(min(x, y, w1, h1))
