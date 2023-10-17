n, b = map(int, input().split())

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while n:
    result += str(num_list[n % b])
    n //= b
print(result[::-1])
