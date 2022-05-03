# checks monotonocity of a function
def isMonotonic(arr):
    if (all(arr[i] <= arr[i+1] for i in range(len(arr)-1))):
        print ("Monotonically increasing")
    elif (all(arr[i] >= arr[i+1] for i in range(len(arr)-1))):
        print("Monotonically decreasing")
    else:
        print("Exception Occured")

#def isConvex(x, y):
