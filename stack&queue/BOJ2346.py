from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
result = []
i = 1
balloons = deque()
for x in array:
    balloons.append((x, i))
    i += 1

while len(balloons) > 0:
    move = balloons[0][0]
    if move > 0:
        result.append(balloons.popleft()[1])
        balloons.rotate(-(move - 1))

    else:
        result.append(balloons.popleft()[1])
        balloons.rotate(-move)

for data in result:
    if data != result[len(result) - 1]:
        print(data, end=" ")
    else:
        print(data, end="")
