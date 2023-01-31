import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for i in range(n):
    name = input().rstrip()
    dic[name] = i+1
    dic[str(i+1)] = name
for _ in range(m):
    question = input().rstrip()
    print(dic[question])
