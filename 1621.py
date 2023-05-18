import numpy as np

def numberOfSets(n: int, k: int):
    dp = np.zeros((k+1,n+1),dtype=int)
    c = (10**9+7)
    for i in range(n+1):
        dp[0][i] = 1
    for i in range(k+1):
        for j in range(n+1):
            a = 0 
            for z in range(i,j):
                a = a + dp[i-1][z] % c
            a = a + dp[i][j-1] % c
            dp[i][j] = a
    return dp[k][n] 

print(numberOfSets(4,2))