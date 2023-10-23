def gcd(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a


a, b = map(int, input().split())
print(a*b // gcd(a, b))
