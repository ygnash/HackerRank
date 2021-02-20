############################################################################
#    Compress the String using itertools groupby 
"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. 
Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

IP --> 1222311
OP --> (1, 1) (3, 2) (1, 3) (2, 1)
"""
#---------------------------------------------------------------------------
from itertools import groupby


print(*[ (len(list(g)),int(k)) for k, g in groupby('1222311')])
 
#---------------------------------------------------------------------------