def perm_gen_rec(n):
    
    if n == 1:  # 2**1 = 2
        return ['0', '1']
    else:
        old_results = perm_gen_rec(n - 1) #['00...000', '00...001', ...., '11...111']
        #['000...000', '000...001', ...., '011...111']
        # 'abc' + 'def' ----> 'abcdef'
        start_by_0 = []
        for result in old_results:
            start_by_0.append('0' + result)
        
        #['100...000', '100...001', ...., '111...111']
        start_by_1 = []
        for result in old_results:
            start_by_1.append('1' + result)
            
        return start_by_0 + start_by_1
    
if __name__ == "__main__":
    print(perm_gen_rec(3))
    