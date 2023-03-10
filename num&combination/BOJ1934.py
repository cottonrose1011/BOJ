def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return int(a*b/gcd(a, b))


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))
