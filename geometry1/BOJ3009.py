setX = set()
setY = set()
x1, y1 = map(int, input().split())
setX.add(x1)
setY.add(y1)
x2, y2 = map(int, input().split())
setX.add(x2)
setY.add(y2)
x3, y3 = map(int, input().split())
setX.add(x3)
setY.add(y3)
sumX = x1 + x2 + x3
sumY = y1 + y2 + y3
tx = 0
ty = 0
for x in setX:
    tx += 2*x
for y in setY:
    ty += 2*y
print(tx - sumX, ty - sumY)
