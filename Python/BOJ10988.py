word = input()
result = 2

for i in range(len(word)//2):
    if word[i] != word[-i-1]:
        result = 0
if result == 2:
    result = 1
print(result)
