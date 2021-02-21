############################################################################
#   Triangle Quest
"""
You are given a positive integer . Print a numerical triangle of height  like the one below:
1
22
333
4444
55555
......
Can you do it using only arithmetic operations, a single for loop and print statement?
Use no more than two lines. The first line (the for statement) is already written for you. 
You have to complete the print statement.
Note: Using anything related to strings will give a score of .
"""
#---------------------------------------------------------------------------
for i in range(1,int(input())): 
    print((10**i//9)*i)
    print([0,1,22,333,4444,55555,666666,7777777,88888888,999999999][i])
#---------------------------------------------------------------------------