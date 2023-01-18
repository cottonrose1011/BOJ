def hanoi(n, src, dst):
    # 보조로 이동할 기둥 찾기
    temp = 6 - src - dst
    # 종료 조건
    if n == 0:
        return
    # 보조 기둥으로 이동을 재귀로 해결
    hanoi(n - 1, src, temp)
    print(src, dst)
    # 목표 기둥으로 이동
    hanoi(n - 1, temp, dst)


n = int(input())
print(pow(2, n) - 1)
hanoi(n, 1, 3)
