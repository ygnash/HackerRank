
def rotLeft(a, d):
    for _ in range(len(a)-d):
        temp = a.pop()
        a.insert(0, temp)     
    return a

if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    print(' '.join(map(str, result)))
