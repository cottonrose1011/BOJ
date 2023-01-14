import math


def goldBach(n):
    array = [True for _ in range(n + 1)]
    a = 0
    b = 0
    for x in range(2, int(math.sqrt(n)) + 1):
        if array[x]:
            j = 2
            while x * j <= n:
                array[x * j] = False
                j += 1

    if array[n // 2]:
        a = n // 2
        b = n // 2
    else:
        count = n - 1
        while count >= 0:
            if array[count]:
                if array[n - count] and (count > n - count):
                    prev_a = a
                    prev_b = b
                    a = n - count
                    b = count
                    sub = b - a
                    if b - a > sub:
                        a = prev_a
                        b = prev_b
            count -= 1
    print(a, b)


T = int(input())
answer = list()
for i in range(T):
    n = int(input())
    answer.append(n)
for data in answer:
    goldBach(data)
