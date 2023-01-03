up, down, v = map(int, input().split())

if (v-up) % (up-down) == 0:
    print((v-up) // (up-down)+1)
else:
    print((v-up) // (up-down)+2)
