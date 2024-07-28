def perm_gen_rec(n):
    if n == 1:  # 2**1 = 2
        return [[1], [-1]]
    else:
        old_results = perm_gen_rec(n - 1)
        start_by_One = []
        for result in old_results:
            start_by_One.append([1] + result)
        
        start_by_NegOne = []
        for result in old_results:
            start_by_NegOne.append([-1] + result)
            
        return start_by_One + start_by_NegOne

def bal_split_ver1(arr):
    '''
    utilize the old permutation and loop over the permutation
    '''
    min_diff = sum(arr) # maximum split
    groups = perm_gen_rec(len(arr)) # the all possible groups
    for gp in groups:
        # for example, gp = [1, -1, 1, -1, 1]
        diff = 0
        for i in range(len(gp)):
            diff = diff + gp[i] * arr[i]
        diff = abs(diff)
        if diff < min_diff:
            min_diff = diff
    return min_diff
    
def bal_split_ver2_loop(arr):
    '''
                        l - r
    [5,8,13,27,14]       67          []
                67 - 2*5 = 57
                67 - 2*8 = 51
                67 - 2*13 = 41
                67 - 2*27 = 13 (**)
                67 - 2*14 = 39
    [5,8,13,14]          13         [27]
                13 - 2*5 = 3 (**)
                13 - 2*8 = -3
                13 - 2*13 = -13
                13 - 2*14 = -15
                13 + 2*27 = 67
    [8,13,14]            3          [27, 5]
                3 - 2*8  = -13
                3 - 2*13 = -23
                3 - 2*14 = -25
                3 + 2*27 = 57
                3 + 2*5  = 13  
    '''
    n = len(arr)
    current = [arr,[]]
    curr_diff = sum(arr)
    
    temp_idx = 0
    while True:
        temp_dif = curr_diff
        temp_idx = n
        for i in range(len(current[0])):
            if abs(curr_diff - 2*current[0][i]) < abs(temp_dif):
                temp_dif = curr_diff - 2*current[0][i]
                temp_idx = i
        
        for j in range(-1,-len(current[1])-1):
            if abs(curr_diff + 2*current[1][i]) < abs(temp_dif):
                temp_dif = curr_diff + 2*current[1][i]
                temp_idx = j
        
        if temp_idx == n:
            break
        elif temp_idx >= 0:
            current[1].append(current[0].pop(temp_idx))
        else:
            current[0].append(current[1].pop(temp_idx))
        
        
        curr_diff = temp_dif
        print(current, curr_diff)
    
    # return current, curr_diff
# for loop

def bal_split_ver2_rec(arr):
    ...
    
if __name__ == "__main__":
    # print(bal_split_ver2_loop([5,8,13,27,14]))
    print(bal_split_ver2_loop([2627,67536,70013,14133,64027]))
    # print(bal_split_ver2_loop([40269,57181,56421,76170,10867,76502,70083,1854,16234,25843]))
    # print(bal_split_ver2_loop([30564,72006,71139,75308,45713,24080,25868,75274,10798,15761]))
    # print(bal_split_ver2_loop([96376,2440,88670,35340,78458,33025,25029,85335,10950,20313]))
    # print(bal_split_ver2_loop([82653,33778,55465,31910,85718,45085,12259,61348,58509,97506]))
    
    '''
    [2627, 67536, 14133]     -49744     [70013, 64027]
                    -49744 - 2*2627   = ...
                    -49744 - 2*67536  = ...
                    -49744 - 2*14133  = ...
                    -49744 + 2*70013  = 90282
                    -49744 + 2*64027  = 
    '''