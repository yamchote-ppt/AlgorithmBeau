def maxCut(length, priceList,i=0):
    #base case
    # if i == 0:
    #     print(f"from length = {length}")
    if length == 0:
        return 0
    
    #recursive case
    '''max_cut_1 = priceList[0] + maxCut(length - 1, priceList) # price for each length + maxCut(remaining length, priceList is the reference)
    max_cut_2 = priceList[1] + maxCut(length - 2, priceList)
    max_cut_3 = priceList[2] + maxCut(length - 3, priceList)
    max_cut_length = priceList[length-1] + maxCut(length - length, priceList)'''
    max_cut_n = 0
    for n in range(1, length + 1):      # n = 1, 2, 3, ..., length                 range(5) = 0,1,2,3,4
        temp = priceList[n-1] + maxCut(length - n, priceList,i+1)
        # if i == 0:
        #     print(f"we're going to consider to cut length {n:2d} whose price is {priceList[n-1]:3d} and max of the rest is {temp - priceList[n-1]:3d} and get {temp}")
        if max_cut_n < temp:
            max_cut_n = temp # where 1<n<L
    # return temp
    return max_cut_n

memo = {}
#################
#
# dct = dict(..................)    key:value
#       dct[key]      -> value
#       dct[key] = assignValue
#       dct.get(key, default_if_key_not_in)
#       dct.keys()    -> list of keys
#       dct.values()  -> list of values
#
##################

def maxCut_memo(length, priceList, i=0):
    global memo
    #base case
    # if i == 0:
    #     print(f"from length = {length}")
    if length == 0:
        return 0
    elif length in memo.keys():
        return memo[length]
    
    #recursive case
    '''max_cut_1 = priceList[0] + maxCut(length - 1, priceList) # price for each length + maxCut(remaining length, priceList is the reference)
    max_cut_2 = priceList[1] + maxCut(length - 2, priceList)
    max_cut_3 = priceList[2] + maxCut(length - 3, priceList)
    max_cut_length = priceList[length-1] + maxCut(length - length, priceList)'''
    max_cut_n = 0
    for n in range(1, length + 1):      # n = 1, 2, 3, ..., length                 range(5) = 0,1,2,3,4
        temp = priceList[n-1] + maxCut_memo(length - n, priceList,i+1)
        # if i == 0:
        #     print(f"we're going to consider to cut length {n:2d} whose price is {priceList[n-1]:3d} and max of the rest is {temp - priceList[n-1]:3d} and get {temp}")
        if max_cut_n < temp:
            max_cut_n = temp # where 1<n<L
    # return temp
    memo[length] = max_cut_n
    return max_cut_n





if __name__ == "__main__":
    '''
    1.in (L = 10) : 29
    2.in (L = 20) : 52
    3.in (L = 40) : 160
    4.in (L = 100): 366
    '''
    # print(maxCut(10, [1,5,8,12,14,16,17,20,24,27 ]))
    
    import time
    import matplotlib.pyplot as plt
    # start = time.time()
    # print(maxCut(20, [1,4,8,9,12,14,15,16,17,18,21,25,26, 27, 28, 31, 35, 37, 40, 41 ]+[17,18,21,25,26, 27, 28, 31, 35, 37]))
    # end = time.time()
    # print(f'used time = {end - start} seconds')
    
    # start = time.time()
    # print(maxCut_memo(20, [1,4,8,9,12,14,15,16,17,18,21,25,26, 27, 28, 31, 35, 37, 40, 41 ]+[17,18,21,25,26, 27, 28, 31, 35, 37]))
    # end = time.time()
    # print(f'used time = {end - start} seconds')
    time_memo = []
    for l in range(1,800):
        start = time.time()
        print(maxCut_memo(l, [4,5,6,7,9,10,12,13,17,19,20,24,26,28,29,30,32,33,36,41,43,46,50,54,55,57,59,62,65,68,71,74,76,77,81,85,89,91,95,96]*100))
        end = time.time()
        print(f'used time = {end - start} seconds')
        time_memo.append(end - start)
    plt.plot(time_memo, label='with memo')

    
    time_no_mem = []
    for l in range(1,20):
        start = time.time()
        print(maxCut(l, [4,5,6,7,9,10,12,13,17,19,20,24,26,28,29,30,32,33,36,41,43,46,50,54,55,57,59,62,65,68,71,74,76,77,81,85,89,91,95,96]*100))
        end = time.time()
        print(f'used time = {end - start} seconds')
        time_no_mem.append(end - start)
    plt.plot(time_no_mem, label='no memo')
    plt.legend()
    plt.show()
    
    # start = time.time()
    # print(maxCut_memo(40, [4,5,6,7,9,10,12,13,17,19,20,24,26,28,29,30,32,33,36,41,43,46,50,54,55,57,59,62,65,68,71,74,76,77,81,85,89,91,95,96]))
    # end = time.time()
    # print(f'used time = {end - start} seconds')
    
    
    # for l in range(1,40):
    #     print(f'memo is {memo}')
    #     start = time.time()
    #     print(maxCut_memo(l, [4,5,6,7,9,10,12,13,17,19,20,24,26,28,29,30,32,33,36,41,43,46,50,54,55,57,59,62,65,68,71,74,76,77,81,85,89,91,95,96]))
    #     end = time.time()
    #     print(f'used time for length = {l} is {end - start} seconds')
