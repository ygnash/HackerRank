import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    c = Counter(ar)
    return sum(v//2 for v in c.values())

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    print(sockMerchant(n, ar))
