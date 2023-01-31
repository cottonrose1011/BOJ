s = input()
result = set()
for i in range(len(s)):
    for j in range(len(s)):
        result.add(s[i:(len(s)-j)])
print(len(result)-1)
