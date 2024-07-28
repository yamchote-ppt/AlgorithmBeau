# import numpy as np
# x = np.infty
# Assume we have coin 1 which make all value possible to change

def mincoin_without_memo(v: int, coinValue: list[int]):
    #base case
    if v == 0:
        return 0
    elif v in coinValue:
        return 1
    
    #recursion case
    '''
    Assume we fix coinValue [1, 3, 4, 5]
    a = mincoin(........)
    b = mincoin(........)
    c = mincoin(........)
    d = mincoin(........)
    -----> min([a,b,c,d])
    -----> min([5,3,2,1])
    result = 1

    '''
    #loop to find the minimum of the recursive solutions from smaller v's (v - coinValue[i])
    minResult = v
    for coin in coinValue:
        if v - coin >= 0:
            x = mincoin_without_memo(v - coin, coinValue) # mincoin(currentCoinValue - coinValue's index, list)
            # find minimum coins
            if minResult > x:
                minResult = x

    return minResult + 1


def mincoin_with_memo(v: int, coinValue: list[int], memo={}):
    #base case
    if v == 0:
        memo[0] = 0
        return 0
    elif v in coinValue:
        memo[v] = 1
        return 1
    
    #recursion case
    '''
    Assume we fix coinValue [1, 3, 4, 5]
    a = mincoin(........)
    b = mincoin(........)
    c = mincoin(........)
    d = mincoin(........)
    -----> min([a,b,c,d])
    -----> min([5,3,2,1])
    result = 1

    '''
    #loop to find the minimum of the recursive solutions from smaller v's (v - coinValue[i])
    minResult = v
    for coin in coinValue:
        if v - coin >= 0:
            if v - coin not in memo.keys():
                #--------------memo----------------
                memo[v - coin] = mincoin_with_memo(v - coin, coinValue,memo) # mincoin(currentCoinValue - coinValue's index, list)
                x = memo[v - coin]
                #--------------memo----------------
                # find minimum coins
            else:
                x = memo[v-coin]
                    
            if minResult > x:
                minResult = x

    return minResult + 1

if __name__ == "__main__":
    # assert mincoin(7, [1, 3, 4, 5]) == 2, f"Wrong answer for mincoin(7, [1, 3, 4, 5]), expected 2 but got {mincoin(7, [1, 3, 4, 5])}"
    # n = 100
    # print(mincoin_without_memo(n, [1, 3, 4, 5]))
    # print(mincoin_with_memo(n, [1, 3, 4, 5]))
    # print(mincoin_without_memo(n, [5,4,3,1]))
    # print(mincoin_with_memo(n, [5,4,3,1]))
    
    
    # print(mincoin_with_memo(3377, [1,2,5,10,13]))
    print(mincoin_with_memo(33770, [13,10,5,2, 1]))
    
    print("pass all test case")