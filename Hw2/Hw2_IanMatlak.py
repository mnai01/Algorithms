arr = [1, 7, 8, 5, 4, 9]


# Time Complexity: O(n)
def LDS(arr):
    count = 1
    last = arr[0]
    # this is just an array which holds the 0 index of arr[0] and can hold more
    LDS = [arr[0]]
    # iterate 1-array length
    for x in range(1, len(arr)):
        # is index less then last lowest sequence value
        if arr[x] <= last:
            # increment maxs
            count += 1
            # last equals the new lowest sequence value
            last = arr[x]
            # add that value to array
            # append time complexity of O(1)
            # Reference https://wiki.python.org/moin/TimeComplexity
            LDS.append(last)
        # if LDS is at 0 index
        elif(len(LDS) == 1):
            # check index 2 is less than index 3
            # ex. 1 5 6
            # LDS = 1, arr[x] = 5, arr[x+1] = 6
            # checks if the two values infront of the first follow
            # a lowest sequence order, if yes then index 1 in your
            # new last
            if(arr[x + 1] < arr[x]):
                last = arr[x + 1]
            else:
                LDS[0] = arr[x]
    print(count, LDS)


# Time Complexity O(√n)
def sqrt(num):
    # create a variable to iterate through all the square roots
    index = 0
    # if index mutliplied by index is higher then number
    # that means the last index was the floor squareroot of num
    while (index*index <= num):
        # used to increment
        index += 1
        # sets sqrt to the answer
        # -1 is required because the last iteration of this loop happens
        # when index is +1 infront of the real squareroot
        sqrt = index - 1
    print(sqrt)


LDS(arr)
sqrt(100)
