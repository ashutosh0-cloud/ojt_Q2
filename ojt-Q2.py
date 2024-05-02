#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q2. Row Echelon Form: Create a 5x5 matrix, A, with entries randomly chosen integers between 0 and 9. To generate the random matrix, set the random seed as the last two digits of your roll number. Reduce matrix A to its Row Echelon Form by performing elementary row operations. 


# In[10]:


import numpy as np
A = np.random.randint(0, 10, (5, 5))
print("Matrix A:")
print(A)
A = A.astype(float)
rows, cols = A.shape
for r in range(rows):
    pivot = A[r, r]
    if pivot != 0:
        A[r] = A[r] / pivot
    for r2 in range(r + 1, rows):
        multiplier = A[r2, r]
        A[r2] = A[r2] - multiplier * A[r]

print("\nRow Echelon Form of Matrix A:")
print(A)


# In[ ]:




