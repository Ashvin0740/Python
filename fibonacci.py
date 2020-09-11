def fib(n):
    a = 0
    b = 1

    if (n == 1):
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2, n):
            x = a + b
            a = b
            b = x
            print(x)

n = int(input("Enter Number: "))
fib(n)