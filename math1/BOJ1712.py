A, B, C = map(int, input().split())
# A: 고정 비용, B: 가변 비용, C: 노트북의 가격
salesVolume = 0

if B >= C:
    salesVolume = -1
else:
    salesVolume = (A // (C-B)) + 1

print(salesVolume)
