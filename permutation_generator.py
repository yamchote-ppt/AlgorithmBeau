def perm_gen(n):
    perm = ['0']*n
    print(' '.join(perm))
    
    for i in range(2**n - 1):
        idx = -1                    # initialize
        while perm[idx] == '1':         # condition
            # if the number at this idx is 1
            # shift the index to the next left position
            idx -= 1                # update
        
        # exit from while loop: perm[idx] != 1 (i.e. it is 0)
        # that is, the first 0 is found
        
        # change this 0 (perm[idx]) to be 1
        # perm = [... ,     0      ,  1, 1, 1, 1]
        #                perm[idx]
        #               idx = -5
        perm[idx] = '1'
        # perm = [... ,     1      ,  1, 1, 1, 1]
        #                perm[idx]
        #               idx = -5
        # and then reset all number at right to be 0
        # want
        # perm = [... ,     1      ,  0,  0,   0,    0     ]
        #                perm[idx]                  perm[-1]
        #               idx = -5     -4   -3   -2   -1   0
        for i in range(idx+1, 0):
            perm[i] = '0'
        print(' '.join(perm))
    


if __name__ == "__main__":
    perm_gen(5)