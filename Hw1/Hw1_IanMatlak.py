from time import perf_counter
# input data
arr = [1,2,3,4,5,43,64,23,436,73,234,75,345,500];

# The Runtime of this function is O(n)
def LargestAlgorithm(arr):
    # sets variables to default values
    largest = arr[0];
    secondlargest = arr[1];
    # perf_counter uses cpu tme
    start = perf_counter();
    # iterates throught list
    for i in range(len(arr)):
        # compares values, if new largest is found
        if(largest < arr[i]):
            # secondlargest hold the current largest
            secondlargest = largest;
            # largest changed and is now a new larger value
            largest = arr[i];
        # if value isnt largest, check if its second largest
        elif(arr[i] != largest and secondlargest < arr[i]):
            secondlargest = arr[i];
    stop = perf_counter();
    print(stop-start)
    return largest * secondlargest;

print(LargestAlgorithm(arr))
