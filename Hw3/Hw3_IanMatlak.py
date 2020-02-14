
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)+Fibonacci(n-3)


def fibonacci(n):
    first = 0
    second = 1
    length = n
    itreration = 0
    if length == 1:
        return 1
    else:
        while itreration < length:
            temp = first + second
            first = second
            second = temp
            itreration += 1
            print(temp)


print(fibonacci(10))
