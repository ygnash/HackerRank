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

ls = [ 3, 2, 1]
d = deque(ls)

while len(d) is not 1:
    left = d.popleft()
    right = d.pop()
    if left < right:
        top = left
        bottom = right
    else:
        top = right
        bottom = left
    






#---------------------------------------------------------------------------