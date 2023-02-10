def fib(n):
    global rCount

    if n == 1 or n == 2:
        return 1  # 코드1
    else:
        rCount += 1
        return fib(n - 1) + fib(n - 2)


def fibo_dp(n):
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


n = int(input())
f = [0] * (n+1)
f[1], f[2] = 1, 1
rCount = 1
fib(n)
print(rCount, n-2)
