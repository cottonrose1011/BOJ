import sys

input = sys.stdin.readline
n = int(input())
dance = {'ChongChong': 1}

for _ in range(n):
    rabbit = input().split()
    if rabbit[0] in dance:
        dance[rabbit[1]] = 1
    elif rabbit[1] in dance:
        dance[rabbit[0]] = 1

print(len(dance))
