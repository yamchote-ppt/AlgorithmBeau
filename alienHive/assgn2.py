#%%
memo = {}
def assignment2(N,K,priceList,i=0):
    global memo
    if N == 0 or K == 0:
        memo[(N,K)] = 0
        return memo[(N,K)]
    if (N,K) in memo.keys():
        return memo[(N,K)]
    else:
        mn = float("inf")
        for k in range(1,min(K+1,len(priceList)+1)):
            currentPrice = priceList[k-1]
            if i==0:
                print(f'currentPrice = {currentPrice}', end='')
            if currentPrice != -1:
                prev = assignment2(N-1,K-k,priceList,i+1)
                if i==0:
                    print(f' | prev = {prev}', end ='')
                if currentPrice!=-1 and prev != -1:
                    if i ==0:
                        print('   update   ', end='')
                    if mn > currentPrice + prev:
                        mn = currentPrice + prev
            if i==0:
                print(f' | mn = {mn}')
        if mn == float("inf"):
            memo[(N,K)] = -1
            return memo[(N,K)]
        else:
            memo[(N,K)] = mn
            return memo[(N,K)]

# assignment2(3, 5, [-1,-1,4,5,-1])
assignment2(51, 53, [-1, 3, -1, 2, 8, 10, -1, 19])

# %%
