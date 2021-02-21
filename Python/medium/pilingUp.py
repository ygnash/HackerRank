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


# def left_greater(d):
#     top = d.pop()
#     bottom = d.popleft()
#     return top, bottom

# def right_greater(d):
#     bottom = d.pop()
#     top = d.popleft()
#     return top, bottom

# def validate_pileup(d, method):
#     stack = []
#     while len(d) > 1:
#         t, b = method(d)
#         stack.append(b)
#         stack.append(t)

#         if len(d) == 1:
#             stack.append(d.pop())

#     return all([ stack[i]>=stack[i+1] for i in range(len(stack)-1)])

# if __name__ == '__main__':
#     for _ in range(int(input())):
#         n,ls = int(input()), list(map(long, input().split()))
#         deq = deque(ls)
#         if ls[0] >= ls[n-1]:
#             print('Yes' if validate_pileup(deq, left_greater) else 'No')
#         else:
#             print('Yes' if validate_pileup(deq, right_greater) else 'No')
    


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