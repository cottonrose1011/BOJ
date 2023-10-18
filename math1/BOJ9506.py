while True:
    n = int(input())

    if n == -1:
        break
    else:
        array = []

        for i in range(1, n):
            if n % i == 0:
                array.append(i)

        if sum(array) == n:
            print('%d = ' % n, end="")
            for i in range(len(array)):
                if i != len(array) - 1:
                    print(array[i], '+', end=" ")
                else:
                    print(array[i])
        else:
            print(n, "is NOT perfect.")
