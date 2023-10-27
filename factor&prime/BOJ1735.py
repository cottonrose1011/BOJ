def gcd(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a = a1*b2 + a2*b1
b = b1 * b2
fact = gcd(a, b)

a = a//fact
b = b//fact

print(a, b)

