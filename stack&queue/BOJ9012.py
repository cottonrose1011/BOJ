t = int(input())

for _ in range(t):
    stack = []
    ps = input()
    for s in ps:
        if s == '(':
            stack.append(s)
        else:
            if s == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)

    print('YES' if len(stack) == 0 else 'NO')

