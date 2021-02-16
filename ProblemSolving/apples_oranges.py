############################################################################
#    PROBLEM - Apples and Oranges
'''Sample input
7 11
5 15
3 2
-2 2 1
5 -6
'''
#---------------------------------------------------------------------------
# solution 1
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apple = sum([ ((f+a)>=s and (f+a)<=t) for f in apples])
    count_oranges = sum([ ((o+b)>=s and (o+b)<=t) for o in oranges])
    print(count_apple, count_oranges, sep = '\n')


# Solution 2
def countApplesAndOranges2(s, t, a, b, apples, oranges):
    print(sum(s <= a + d <= t for d in apples))
    print(sum(s <= b + d <= t for d in oranges))


if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)

#---------------------------------------------------------------------------