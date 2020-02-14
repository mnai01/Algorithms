
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


print(Fibonacci(3))

# You have 20 M&Ms bags. 19 bags have 1.0 gram pieces, but one has pieces of weight  1.1 grams.
# Given a scale that provides an exact measurement, how would you find the heavy bag? You can only use the scale once.
# 20% Please describe your solution using a MS Word document.

# It can not be done with a one time use of the scale.
# You must split the balls into 3 planes then weigh two of same plans for example 4-8-8.
# If they both weigh the same then you know the heavier ball is in the 1st plane.
# You then split the 1st plan in half 2-2, find out which is heavier then weight again 1-1.
# The best case for this algorithm would be 3 chnaces
# 1111 11111111 11111111
