from math import gcd

n = int(input())
ring = list(map(int, input().split()))
first_ring = ring[0]

for r in ring[1:]:
    if first_ring == r:
        print('1/1')
    elif first_ring % r == 0:
        print(str(first_ring//r)+'/'+'1')
    else:
        a = first_ring // gcd(first_ring, r)
        b = r // gcd(first_ring, r)
        print(str(a)+"/"+str(b))
