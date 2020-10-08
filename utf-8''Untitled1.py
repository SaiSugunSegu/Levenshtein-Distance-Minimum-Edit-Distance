#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


class Transformation:
    def edit(self,s,t):
        m = len(s)
        n = len(t)
        
        dp = np.zeros((m+1,n+1),dtype=int)  # Initialization of Distance Matrix
        
        ins_cost = 1                        # Insert Cost
        del_cost = 1                        # Delete Cost
        rep_cost = 2                        # Replace Cost
        
        for i in range(m+1):                # Initialization of column of Target
            dp[i,0] = i
        for j in range(n+1):                # Initialization of row of Source
            dp[0,j] = j
        
        for i in range(1,m + 1): 
            for j in range(1,n + 1):
                r_cost = rep_cost
                if s[i-1] == t[j-1]: 
                    r_cost = 0              # If char are same
                else:                       # If Char are different
                    dp[i][j] = min(ins_cost + dp[i,j-1], del_cost + dp[i-1,j], r_cost + dp[i-1,j-1])
        return dp
    


# In[3]:


t= Transformation()
t.edit('sugun','latika')


# In[4]:


class Transformation:
    def edit(self,s,t):
        m = len(s)
        n = len(t)
        
        dp = np.zeros((2,n+1),dtype = int)                # Initialization of Distance Matrix
        
        ins_cost = 1                                      # Insert Cost
        del_cost = 1                                      # Delete Cost
        rep_cost = 2                                      # Replace Cost

        for j in range(n+1):                              # Initialization of row of Source
            dp[0,j] = j
        
        for i in range(1,m + 1): 
            for j in range(n + 1):  
                if j == 0:                                # Min. operations = i
                    dp[i%2,j] = i; 
                elif s[i-1] == t[j-1]:                    # If char are same
                    dp[i%2,j] = dp[(i-1)%2,j-1]
                else:                                     # If char are different
                    dp[i%2,j] = min(ins_cost + dp[(i-1)%2,j], del_cost + dp[i%2,j-1], rep_cost + dp[(i-1)%2,j-1]); 
        return dp
    


# In[5]:


t= Transformation()
t.edit('sugun','latika')


# In[6]:


class Transformation:
    def edit(self,s,t):
        m = len(s)
        n = len(t)
        
        dp = np.zeros((m+1,n+1),dtype=int)  # Initialization of Distance Matrix
        
        ins_cost = 1                        # Insert Cost
        del_cost = 1                        # Delete Cost
        rep_cost = 2                        # Replace Cost
        
        for i in range(m+1):                # Initialization of column of Target
            dp[i,0] = i
        for j in range(n+1):                # Initialization of row of Source
            dp[0,j] = j
        
        for i in range(1,m + 1): 
            for j in range(1,n + 1):  
                if i == 0: 
                    dp[i,j] = j             # Min. operations = j 
                elif j == 0: 
                    dp[i,j] = i             # Min. operations = i 
                elif s[i-1] == t[j-1]: 
                    dp[i][j] = dp[i-1,j-1]  # If char are same
                else:                       # If Char are different
                    dp[i][j] = min(ins_cost + dp[i,j-1], del_cost + dp[i-1,j], rep_cost + dp[i-1,j-1])
        return dp
    


# In[7]:


t= Transformation()
t.edit('sugun','latika')


# In[8]:


with open('Human DNA.fa') as f:
    h_dna = f.read()
h_dna = h_dna.replace('\n', ' ').replace(" ", "").replace('N','')
human_dna = h_dna[53:]


# In[9]:


print(len(human_dna))


# In[10]:


human_dna = h_dna[53:553]
print(human_dna[:500])


# In[11]:


with open('Werewolf DNA.fa') as f:
    w_dna = f.read()
w_dna = w_dna.replace('\n', ' ').replace(" ",'').replace('N','')
werewolf_dna = w_dna[94:]


# In[12]:


print(len(werewolf_dna))


# In[13]:


werewolf_dna = w_dna[94:594]
print(werewolf_dna[:500])


# In[17]:


if __name__ == '__main__':
    T = Transformation()
    d = T.edit(human_dna,werewolf_dna)
    print(d)
    print("\t")
    print('Minimum Edit Distance to convet Human nuclitodes Werewolf nuclitodes into  is',d[len(human_dna),len(werewolf_dna)])


# In[ ]:




