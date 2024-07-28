p = list(map(int, input().split()))
L = len(p)
p = [0] + p

def maxRev(l):
    if l == 0:
        return 0
    else:
        mxp = 0
        for c in range(1,1+1):
            mxp = max(mxp, p[c] + maxRev(l-c))
        return mxp

print(maxRev(L))