def star(num):
    num //= 3
    print("***" * num)
    print("* *" * num)
    print("***" * num)
    if num / 3 > 1:
        print(" ")


n = int(input())

star(n)
