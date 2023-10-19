import sys
input = sys.stdin.readline

while True:
    a, b, c = list(map(int, input().split()))
    if a+b+c == 0:
        break
    sumWithoutMaxValue = a + b + c - max(a, b, c)
    if a == b and b == c:
        print("Equilateral")
    elif max(a, b, c) >= sumWithoutMaxValue:
        print("Invalid")
    elif a != b and b != c and a != c:
        print("Scalene")
    else:
        print("Isosceles")
