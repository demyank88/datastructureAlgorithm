def Fibonacci(v):

    if v == 1 or v == 2:
        return 1

    return Fibonacci(v - 1) + Fibonacci(v -2)


if __name__ == '__main__':
    print(Fibonacci(9))