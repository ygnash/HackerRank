############################################################################
#    PROBLEM - Diagonal Difference
#---------------------------------------------------------------------------

def diagonal_difference(n, arr):
    sum_diagonal_1 = 0
    sum_diagonal_2 = 0

    for i in range(n):
        sum_diagonal_1 += arr[i][i]
        sum_diagonal_2 += arr[n-1][i]
        n -= 1
    
    return abs(sum_diagonal_1 - sum_diagonal_2)

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(n,arr)
    print(result)

#---------------------------------------------------------------------------
