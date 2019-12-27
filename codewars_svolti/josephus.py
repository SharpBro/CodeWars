import sys
sys.setrecursionlimit(5000)
def joseph_2(n,k):
    if n == 1:
        return 1
    else:
        return ((joseph_2(n-1,k) + k - 1) % n) + 1


print(joseph_2(3000,19))
