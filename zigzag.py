
# coding: utf-8

# In[91]:

###########################################
# Sort a list of distinct integers
# such that: a < b > c < d > e <
#
# e.g input: [4,3,7,8,6,2,1]
# e.g result: [1,3,2,6,4,8,7]
# 
# Daniel Kristiyanto
###########################################


# In[92]:

def zigzag(a):
    a.sort()
    if not a or len(a) < 3: return a
    for i in range(0,len(a)-2,2):
        a[i+1], a[i+2] = a[i+2], a[i+1]
    return a


# In[97]:

s = [4,2,90,1]
zigzag(s)


# In[ ]:



