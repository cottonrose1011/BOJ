n = int(input())

for i in range(1, n+1):
    blank = ' ' * (n - i)
    star = blank + '*' * (2*i - 1)
    print(star)
for i in range(n-1, 0, -1):
    blank = ' ' * (n - i)
    star = blank + '*' * (2*i - 1)
    print(star)
