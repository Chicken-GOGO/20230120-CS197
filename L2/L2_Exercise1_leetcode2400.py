from math import factorial
# LeetCode 2400
# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/description/

def numberOfWays(startPos: int, endPos: int, k: int):
    ss = abs(endPos-startPos) # shorest_step
    if k<ss or (k-ss)%2:
        return 0 # no solution
    n = (k-ss)//2
    return (factorial(ss+2*n)//(factorial(ss+n)*factorial(n))) % (10 ** 9 + 7)

print(numberOfWays(989,1000,99))
