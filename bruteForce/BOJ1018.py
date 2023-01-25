n, m = map(int, input().split())
board = [[]*m for _ in range(n)]
for i in range(n):
    s = input()
    for x in s:
        board[i].append(x)
count = []

for a in range(n-7):
    for b in range(m-7):
        index1 = 0  # W로 시작할 경우 : 바꿔야 할 체스 판 개수
        index2 = 0  # B로 시작할 경우 : 바꿔야 할 체스 판 개수
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        index1 += 1
                    if board[i][j] != 'B':
                        index2 += 1
                else:
                    if board[i][j] != 'B':
                        index1 += 1
                    if board[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))
print(min(count))
