import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
words = {}

for _ in range(n):
    w = input().rstrip()
    if len(w) < m:
        continue
    if w not in words:
        words[w] = 1
    else:
        words[w] += 1

result = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for x in result:
    print(x[0])
