n = int(input())
count = 0

while n >= 0:
    if n % 5 == 0:
        count += n//5
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)
# 5의 배수로 떨어질 때 까지 3의 count 올리기
