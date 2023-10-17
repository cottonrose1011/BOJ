t = int(input())

for _ in range(t):

    quarter, dime, nickel, penny = 0, 0, 0, 0
    c = int(input())

    if c // 25 >= 1:
        quarter += c // 25
        c = c % 25
    if c // 10 >= 1:
        dime += c // 10
        c = c % 10
    if c // 5 >= 1:
        nickel += c // 5
        c = c % 5
    if c // 1 >= 1:
        penny += c // 1

    print(quarter, dime, nickel, penny)
