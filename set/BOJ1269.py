n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
aSubB = a-b
bSubA = b-a
print(len(aSubB)+len(bSubA))
