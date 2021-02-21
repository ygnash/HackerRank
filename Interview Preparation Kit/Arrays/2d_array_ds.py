ar = [[0, -4, -6, 0, -7 ,-6],
      [-1, -2, -6, -8 ,-3, -1],
      [-8, -4, -2, -8, -8, -6],
      [-3, -1 ,-2 ,-5, -7, -4],
      [-3, -5, -3, -6, -6, -6],
      [-3, -6, 0, -8 ,-6, -7]]

def hourglassSum(arr):
    for i in range(4):
        for j in range(4):
            sum_val = arr[i][j]+ arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if i==0 and j ==0:
                max_sum = sum_val
            if sum_val > max_sum:
                max_sum = sum_val
    
    return max_sum


print(hourglassSum(ar))