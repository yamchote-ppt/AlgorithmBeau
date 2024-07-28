def FibLoop(n):
    one_prev = 1
    two_prev = 1
    if n==1 or n==2:
        return 1
    for i in range(n-2):
        current_sol = one_prev + two_prev
        two_prev = one_prev
        one_prev = current_sol
    return current_sol

def Fib(n):
    if n==1 or n==2:
        return 1
    one_prev = Fib(n-1)
    two_prev = Fib(n-2)
    return one_prev + two_prev

lookTable = {}

def FibMemo(n):
    global lookTable
    if n==1 or n==2:
        return 1
    # we avoid new computation by look up in lookTable before computing
    if n-1 in lookTable.keys():
        one_prev = lookTable[n-1]  # call a solution from dictionary
    else:
        one_prev = Fib(n-1) # first time computing of n-1
        lookTable[n-1] = one_prev
    
    if n-2 in lookTable.keys():
        two_prev = lookTable[n-2]  # call a solution from dictionary
    else:
        two_prev = Fib(n-2) # first time computing of n-2
        lookTable[n-2] = two_prev
    lookTable[n] = one_prev + two_prev
    return one_prev + two_prev
    

# x = 4
# def aaa():
#     global x
#     x = 2
#     return x

if __name__ == "__main__":
    # print(f'x from funtion = {aaa()}')
    # print(f'x at Line 25 = {x}')
    print(FibMemo(45))
    # for n in range(1,500):
    #     print(f'FibLoop({n}) = {FibLoop(n)}')