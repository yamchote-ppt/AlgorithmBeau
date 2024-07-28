import sys
sys.setrecursionlimit(10000)

A = input()
B = input()

def edist(i,j):
    if i == len(A) and j < len(B):
        return len(B) - j
    if i < len(A) and j == len(B):
        return len(B) - i
    if i == len(A) and j == len(B):
        return 0
    
    else:
        if A[i] == B[j]:
            return edist(i+1, j+1)
        else:
            ins = 1 + edist(i, j+1)
            dlt = 1 + edist(i+1, j)
            chg = 1 + edist(i+1, j+1)
            return min(ins, dlt, chg)
        
print(edist(0,0))
