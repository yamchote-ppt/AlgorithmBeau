memo_female = {}
memo_male = {}

def nGenMale(n):
    if n == 0:
        memo_male[0] = 1
        return 1
    elif n == 1:
        memo_male[1] = 0
        return 0
    elif n-1 in memo_female.keys():
        return memo_female[n-1]
    else:
        return nGenFemale(n-1)
    
def nGenFemale(n):
    if n == 0:
        memo_female[0] = 0
        return memo_female[0]
    elif n == 1:
        memo_female[1] = 1
        return memo_female[1]
    elif (n-1 in memo_female.keys()) and (n-2 in memo_female.keys()):
        return memo_female[n-1] + memo_female[n-2]
    elif (n-1 not in memo_female.keys()) and (n-2 in memo_female.keys()):
        memo_female[n-1] = nGenFemale(n-1)
        return  memo_female[n-1] + memo_female[n-2]
    elif (n-1 in memo_female.keys()) and (n-2 not in memo_female.keys()):
        memo_female[n-2] = nGenFemale(n-2)
        return  memo_female[n-1] + memo_female[n-2]
    else:
        memo_female[n-1] = nGenFemale(n-1)
        memo_female[n-2] = nGenFemale(n-2)
        return  memo_female[n-1] + memo_female[n-2]

def nGenCount(n):
    nMale = nGenMale(n)
    nFemale = nGenFemale(n)
    # print(f'{nFemale} + {nMale}')
    return nMale + nFemale
'''
More explanation:
Let f(n) = the number of female in the gen n above Pel
    m(n) = the number of male in the gen n above Pel
Since a male drone give birth only one female to the next generation,
the number of male in the n gen above Pel must be equal to the number of female in the n-1 gen above Pel.
i.e.    m(n) = f(n-1)
In the other hands, a female must be given a birth from one male and one female,
        f(n) = f(n-1) + m(n-1)
             = f(n-1) + f(n-2)
'''

if __name__ == "__main__":
    # for i in range(10):
    #     nGenCount(i)
    print(nGenCount(28))
    print(nGenCount(97))
    