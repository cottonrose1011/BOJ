n = int(input())
array = list(map(int, input().split()))
stack = []
i = 1

while not array:
    if array[0] != i:
        num = array[0]
        array.remove(num)
        stack.append(num)
    else:
        array.remove(i)
        i += 1

    while len(stack) > 0:
        if stack[-1] == i:
            stack.pop()
            i += 1
        else:
            break

print("Nice" if not stack else "Sad")
