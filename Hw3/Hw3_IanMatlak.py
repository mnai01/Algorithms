# Problem 1

# Time Complexity
# O(3n)
# Ω(1) < (Θ) ≤ O(3n)


def Fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        # recussion with 1 step, 2 step or 3 steps taken
        return Fibonacci(n-1)+Fibonacci(n-2)+Fibonacci(n-3)

# Time Complexity
# Ω(1) < (Θ) ≤ O(n)


def fibonacci(n):
    previousNumber = 1
    nextNumber = 0
    total = 0
    for x in range(0, n):
        if x == 3:
            total += 1
        sum = previousNumber + nextNumber
        previousNumber = nextNumber
        nextNumber = sum
        total += sum
    return total


# Problem 2
# C++ code
# This problem has a big O(n^2) this is because the while loop will iterate n times and
# the if statement will also run n times because of iterate2 = iterate1.
# (n-1)(n-2) (n-3)....(n-size)
arr = [3, 4, 5, 6, 7, 8, 9]
sz = 7


def question2(sz, arr):
    iterate1 = 0
    iterate2 = 0
    largest = 0
    while(iterate1 < sz - 1):
        iterate2 += 1
        if(iterate2 == sz):
            iterate1 += 1
            iterate2 = iterate1
            continue
        product = arr[iterate1] * arr[iterate2]
        if(product > largest):
            largest = product
    return largest


print('recursive statement: ', Fibonacci(3))
print('--------------')
print('Forloop statement: ', fibonacci(3))


# Problem 3
# You have 20 M&Ms bags. 19 bags have 1.0 gram pieces, but one has pieces of weight  1.1 grams.
# Given a scale that provides an exact measurement, how would you find the heavy bag? You can only use the scale once.
# 20% Please describe your solution using a MS Word document.

# Each bag you will have to take n + 1 amount of M&Ms out,
# for instance the 1st bag you take out 1 M&Ms, the 2nd bag you take out 2 M&Ms and so on.
# Now when you weight it on the scale depending what the denth value will tell you what bag is it.
# for instance if you're total M&Ms weight comes out to #.8 then you know the eighth bag is the heaviest.
