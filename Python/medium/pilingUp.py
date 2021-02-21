############################################################################
#    piling up
"""
There is a horizontal row of  cubes. The length of each cube is given. 
You need to create a new vertical pile of cubes.
 The new pile should follow these directions: if cube2 is on top of cube1 then side length of cube1 >= cube2.

When stacking the cubes, you can only pick up either the leftmost or 
the rightmost cube each time. Print "Yes" if it is possible to stack the cubes.
 Otherwise, print "No". Do not print the quotation marks.
"""
#---------------------------------------------------------------------------
from collections import deque


def check(d):
    while d:
        big = d.popleft() if d[0]>d[-1] else d.pop()
        print(len(d), 'big >>>', big)
        if not d:
            return "Yes"
        if d[-1]>big or d[0]>big:
            return "No"
    
for i in range(int(input())):
    int(input())
    d = deque(map(int,input().split()))
    print(check(d))
#---------------------------------------------------------------------------