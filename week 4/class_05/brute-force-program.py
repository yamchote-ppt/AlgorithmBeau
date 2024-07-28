import sys
sys.setrecursionlimit(10000)

p = input().split()
length = len(p)
for i in range(length):
    p[i] = int(p[i])

p.insert(0,0)

def maxRev(l):
    global p,L

    if l == 0:
        return 0
    else:
        mx = 0
        for i in range(1,l+1):
            mx = max(mx, p[i]+maxRev(l-i))
    return mx

print(maxRev(length))

# speeding brute force
calls = [0] * (1 + length)
print(maxRev(length))