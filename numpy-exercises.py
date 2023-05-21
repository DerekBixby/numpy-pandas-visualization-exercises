# 1. Negative numbers: 4

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

a<0
a[a<0]
a[a<0].shape[0] 
len(a[a<0])

# 2. positive numbers: 5

a>0
a[a>0]
len(a[a>0])
a[a>0].shape[0]

# 3. Even positive numbers: 3

even = a[a % 2 ==0]
even.shape[0]
even[even>0]
len(even[even>0])
how_many = a[(a>0) & (a%2==0)]
len(how_many)

# 4. add 3 to each data point, how many positive numbers: 10

add_three = a+3
add_three.shape[0]
len(a[(a+3)>0])

# 5. mean and SD after squaring each number. SD: 144.02, Mean: 74

np.mean(a**2), np.std(a**2)

# 6. subtract mean from each data point. 

a.mean()
centered_a = a - a.mean()

# 7. z-score for each data point

import scipy.stats as stats
stats.zscore(a)