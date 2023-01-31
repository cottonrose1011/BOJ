n = int(input())
array = list(map(int, input().split()))
m = int(input())
question = list(map(int, input().split()))
dic = {}
for x in array:
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1
for q in question:
    if q in dic:
        print(dic[q], end=" ")
    else:
        print(0, end=" ")
