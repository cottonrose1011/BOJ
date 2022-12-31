n = int(input())
room = 1
count = 0
a = 1

if n == 1:
    pass
elif 2 <= n <= 7:
    room = 2
else:
    while n > a:
        count += 1
        a += 6*count
    room += count

print(room)

