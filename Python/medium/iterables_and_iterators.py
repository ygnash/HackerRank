######################################################################################
# PROBLEM - Iterators and Iterables
"""
You are given a list of  lowercase English letters. For a given integer , you can select
 any  indices (assume -based indexing) with a uniform probability from the list.
Find the probability that at least one of the  indices selected will contain the letter: ''.
"""

######################################################################################
from itertools import combinations

n = int(input())
ls =input().split()
count = 0
c = list(combinations(ls, int(input())))
for item in c:
    if 'a' in item:
        count += 1

print(f'{count/len(c):.4f}')

#--------------------------------------------------------------------------------------