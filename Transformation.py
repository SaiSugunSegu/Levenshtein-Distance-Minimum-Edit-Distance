import numpy as np

def edit(s,t):
    m = len(s)
    n = len(t)

    dp = np.zeros((m+1,n+1),dtype = int)
    
    for i in range(n+1):
        dp[0,i] = i
    for i in range(m+1):
        dp[i,0] = i
    
    for i in range(1,m + 1): 
        for j in range(1,n + 1):  
            if i == 0: 
                dp[i][j] = j # Min. operations = j 
            elif j == 0: 
                dp[i][j] = i # Min. operations = i 
            elif s[i-1] == t[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
            else: 
                dp[i][j] = min(1+dp[i][j-1],1+dp[i-1][j],2+dp[i-1][j-1])
    return dp
    
    
def edit(s,t):
    m = len(s)
    n = len(t)

    dp = np.zeros((2,n+1),dtype = int)
    
    for i in range(n+1):
        dp[0,i] = i; 
        
    for i in range(1,m+1):
        for j in range(n+1):
            if (j == 0):
                dp[i%2,j] = i; 
            elif s[i-1] == t[j-1]:
                dp[i % 2,j] = dp[(i - 1) % 2,j - 1]
            else:
                dp[i % 2,j] = min(1+dp[(i - 1) % 2,j], 1+ dp[i%2,j - 1], 2+dp[(i-1)%2,j - 1]); 
    return dp




