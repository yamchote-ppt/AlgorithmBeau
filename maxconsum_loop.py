
def maxconsum(arr):
    n = len(arr)
    tempMax = arr[0]
    count = 0
    for i in range(0, n):
        for j in range(i, n):
            # newSum = sum(arr[i:j+1])
            newSum = 0
            for k in range(i,j+1):
                newSum += arr[k]
                count = count + 1
            if newSum > tempMax:
                tempMax = newSum
    return tempMax, count


if __name__ == "__main__":
    arr = [-2,-3,4,-1,-2,1,5,-3]*100
    
    print(maxconsum(arr))