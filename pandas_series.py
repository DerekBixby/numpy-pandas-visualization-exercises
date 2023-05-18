# Part I

# 1. number of elements in fruits 

import pandas as pd
import numpy as np
from pydataset import data

fruits_series = pd.Series(fruits_list)

fruits_series.count()
17

# 2. output only index from fruits

fruits_series.index

RangeIndex(start=0, stop=17, step=1)

# 3. output only the values from fruits

fruits_series.values

array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
       'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',
       'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',
       'papaya'], dtype=object)

# 4. data type of values in fruits

fruits_series.dtype

dtype('O')

# 5. first 5 values from fruits, last 3 values, two random values

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

fruits_series.sample(2)

14    blackberry
10          kiwi
dtype: object

# 6. run describe on fruits

fruits_series.describe()

count       17
unique      13
top       kiwi
freq         4
dtype: object

# 7. produce only unique string values from fruits

fruits_series.unique()

array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
       'honeycrisp apple', 'tomato', 'watermelon', 'honeydew',
       'blueberry', 'blackberry', 'gooseberry', 'papaya'], dtype=object)


# 8. determine how many times each string value occurs in fruits

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

# 9. string value that occurs most frequently in fruits

fruits_series.mode()

0    kiwi
dtype: object

# 10. string value that occurs least frequently in fruits

order_fruits.nsmallest(n=1, keep='all')

# Part II

# 1. Capitalize all string values in fruits

fruits_series.str.upper()
fruits_series.str.Capitalize()

# 2. count the letter 'a' in all string values

fruits_series.str.count('a')

# 3. output the number of vowels in each string value

vowels = list('aeiouy')

fruits_series.isin(vowels).value_counts()

fruits.str.count('[aeiou]')

# 4. longest string value in fruits

fruits_series[fruits_series.str.len().idxmax()]


# 5. string values with 5 or more letters

fruits_series[fruits_series.str.len() >= 5]

# 6. find fuits containing letter 0

fruits_series[fruits.str.count('o') >=2]

# 7. strings containing substring berry

fruits_series[fruits_series.str.contains('berry')]

# 8. string containing substring apple

fruits_series[fruits_series.str.contains('apple')]

# 9. string that contains most vowels

fruits_series[fruits_series.str.count(r' [aeiou]').nlargest(n=1, keep ='all')]




# part III



# Section 1



# 1. which letter occurs the most frequently in the letter series? 

letters_list = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')

letters = pd.Series(letters_list)

letters.mode()

# 2. which letter occurs the least frequently?

frequency = letters.value_counts()
min(frequency)

letters,str.lower().apply(is_vowel).sum()
# 3. How many vowels in the series? 


letters,str.lower().apply(is_vowel).sum()


# 4. How man consonants are in the series

(~letters,str.lower().apply(is_vowel).sum())

# 5. Create a series that has all the same letters but uppercased

letters.str.capitalize()

# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters

letters.value_counts().head(6).plot.bar()


#Section 2



# 1. data type of numbers series

number_list = list(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
numbers = pd.Series(number_list)

type(numbers)
numbers.dtype

# 2. number of elements in numbers series

numbers.count()

# 3. convert numbers series to numeric data type

numbers2 = numbers.str.replace('$', '').str.replace(',','').astype(float)

# 4. Find max value

max(numbers2)

# 5. find min value

numbers2 = numbers.str.replace('$', '').str.replace(',','').astype(float)

min(numbers2)

# 6. find range of values

def range_series(s):
    return s.max() - s.min()
    print(range_series)

range_series(numbers2)

# 7. bin values into 4 equally sized intervals and find how many values are in each bin

numbers_bin = pd.cut(numbers2, 4)

numbers_bin.value_counts()

# 8. 

numbers_bin.value_counts().sort_index().plot.bar()



# Section 3



# 1. # of exam scores

exam_scores_list = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]

exam_scores = pd.Series(exam_scores_list)

exam_scores.count()

# 2. min, max, median, mean of exam scores

min(exam_scores)
max(exam_scores)
exam_scores.mean()
exam_scores.median()

# 3. plot series in meaningful way

exam_scores.value_counts(bins=5).sort_index().plot.bar(title='Grade Range Frequency', rot=0, color='firebrick', ec='black', width=.9) .set(xlabel='Grade Range', ylabel='Frequency')

# 4. make curved grades. Top score converted to 100 and all other scores moved up by same amount

curved_grades = exam_scores + (100 - max(exam_scores))

# 5 convert each numeric grade into a letter grade

def letter_grader(n):
        if n >= 90:
            return 'A'
        elif n >= 80:
            return 'B'
        elif n >= 70:
            return 'C'
        elif n >= 60:
            return 'D'
        elif n < 60:
            return 'F'

letter_grades = curved_grades.apply(letter_grader).sort_values()

letter_grades

# 6. plot this in meaningful way with title and axis labels 

letter_grades.value_counts().plot.bar(title='Grade Frequency', rot=0, color='firebrick', ec='black', width=.9) .set(xlabel='Grade', ylabel='Frequency')


