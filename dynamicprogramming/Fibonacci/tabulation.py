def Fibonacci(v):
    table = [1, 1] + [0] * (v-2)

    for i in range(2, len(table)):
        table[i] = table[i - 1] + table[i - 2]

    return table[-1]


if __name__ == '__main__':
    print(Fibonacci(9))