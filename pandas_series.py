# 1. 

import pandas as pd
import numpy as np
from pydataset import data

fruits_series = pd.Series(fruits_list)

fruits_series.count()
17

# 2. 

fruits_series.index

RangeIndex(start=0, stop=17, step=1)

# 3.

fruits_series.values

array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
       'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',
       'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',
       'papaya'], dtype=object)

# 4. 

fruits_series.dtype

dtype('O')

# 5. 

fruits_series.head()

0          kiwi
1         mango
2    strawberry
3     pineapple
4    gala apple
dtype: object

fruits_series.tail(3)

14    blackberry
15    gooseberry
16        papaya
dtype: object

fruits_series.sample(3)

1          mango
14    blackberry
10          kiwi
dtype: object

# 6. 

fruits_series.describe()

count       17
unique      13
top       kiwi
freq         4
dtype: object

# 7. 

fruits_series.unique()

array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
       'honeycrisp apple', 'tomato', 'watermelon', 'honeydew',
       'blueberry', 'blackberry', 'gooseberry', 'papaya'], dtype=object)


# 8. 

fruits_series.value_counts()

kiwi                4
mango               2
strawberry          1
pineapple           1
gala apple          1
honeycrisp apple    1
tomato              1
watermelon          1
honeydew            1
blueberry           1
blackberry          1
gooseberry          1
papaya              1
dtype: int64

# 9. 

fruits_series.mode()

0    kiwi
dtype: object

# 10. 

s = fruits_series.value_counts()

s.index[-1]

'papaya'