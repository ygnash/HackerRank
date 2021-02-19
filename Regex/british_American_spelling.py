############################################################################
#    The British and American Style of Spelling
"""American English and British English differ in several aspects which are 
reflected in their spelling. One difference frequently observed, is that words
 written in American English, which have a suffix ze often end in se in British 
 English. Given the American-English spelling of a word which ends in ze your
  task is to find the total count of all its British and American variants in 
  all the given sequences of words. i.e. you need to account for the cases where 
  the word occurs as it is given to you (i.e. the version ending in -ze) and you 
  also need to find the occurances of its British-English counterparts 
  (i.e, the version ending in -se).
"""
#---------------------------------------------------------------------------
import re

string = ' '.join([input() for _ in range(int(input()))])

for _ in range(int(input())):
    print(len(re.findall(input()[:-2]+'[zs]e', string)))




#---------------------------------------------------------------------------
