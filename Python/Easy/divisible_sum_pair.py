############################################################################
#    DIVISIBLE SUM PAIRS
"""Given an array of integers and a positive integer 'k', determine the number 
of  pairs where i < j and  ar[i]+ar[j]  is divisible by 'k'.

Example
ar = [1,2,3,4,5,6]
k = 5
Three pairs meet the criteria:[1,4], [2,3]  and [4,6] .
"""
#---------------------------------------------------------------------------
def divisibleSumPairs(n, k, ar):
    return sum([(ar[i]+ar[j])%k==0 for i in range(n) for j in range(n) if i < j])

#---------------------------------------------------------------------------
