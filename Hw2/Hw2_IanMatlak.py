arr = [1, 7, 8, 5, 4, 9]
def LDS(arr):
    max = 1
    last = arr[0]
    LDS = [arr[0]]
    # iterate 1-array length
    for x in range(1, len(arr)):
        # is index less then last lowest sequence value
        if arr[x] <= last:
            # increment maxs
            max += 1
            # last equals the new lowest sequence value
            last = arr[x]
            # add that value to array
            LDS.append(last)
        # if LDS is at 0 index
        elif(len(LDS) == 1):
            # check index 2 is less than index 3 
            # ex. 1 5 6
            # LDS = 1, arr[x] = 5, arr[x+1] = 6
            # Probably wrongs
            # checks if the two values infront of the first follow
            # a lowest sequence order, if yes then index 1 in your
            # new last
            if(arr[x + 1] < arr[x]):
                last = arr[x + 1]
            else:
                LDS[0] = arr[x]
    print(max, LDS)
LDS(arr)