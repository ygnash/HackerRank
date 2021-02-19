############################################################################
#   UK and US: Part 2
"""
We've already seen how UK and US words differ in their spelling.
 One other difference is how UK has kept the usage of letters our in 
 some of its words and US has done away with the letter u and uses just or. 
 Given the UK format of the word that has our in it, find out the total number 
 of occurrences of both its UK and US variants in a given sequence of words.
"""
#---------------------------------------------------------------------------
import re

string = ' '.join([input() for _ in range(int(input()))])
for _ in range(int(input())):
    print(len(re.findall(input().replace('our','ou?r')+r'\b', string)))


