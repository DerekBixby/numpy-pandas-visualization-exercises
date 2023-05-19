# 1. import pandas, numpy, pydataset data. Create pandas dataset from student grades 

import pandas as pd
import numpy as np
from pydataset import data

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

# a. create new column called 'passing_english' that gives boolean for if a student is passing

df['passing_english'] = df.english > 70

# b. sort values by colum 'passing_english'

df.sort_values(by='passing_english')

# duplicates are put in order of index

# c. sort values so that all student are listed grouped by if they're failing and in alphabetical order in each group

df.sort_values(by='name').sort_values(by='passing_english')

# d. sort so that all students are listed grouped by if they're failing and by increasing numerical grade

df.sort_values(by='english').sort_values(by='passing_english')

# e. calculate each student's overall grade by taking average of numerical grades in all 3 classes

df['overall_grade'] = df.math + df.english + df.reading // 3

# 2. load mpg data set from pydatasets

mpg = data('mpg', show_doc=True) 



# a. how many rows and columns are in mpg dataset

mpg.shape

# 234 rows, 11 columns

# b. data types of each column

mpg.dtypes

manufacturer     object
model            object
displ           float64
year              int64
cyl               int64
trans            object
drv              object
cty               int64
hwy               int64
fl               object
class            object
dtype: object

# c. summarize data with .info and .describe

mpg.info

mpg.describe

# d. rename cty column to city

mpg.rename(columns={'cty': 'city'})

# e. rename hwy column to highway

mpg.rename(columns={'hwy': 'highway'})

# add mpg = to make name change permanent

# f. do any cars have better city mileage than highway mileage?

mpg['city_higher'] = mpg.cty > mpg.hwy

mpg.sort_values(by='city_higher')

# no

# g. create column named mileage_difference (hwy - cty)

mpg['mileage_difference'] = mpg.hwy - mpg.cty

# h. highest mileage difference

mpg.sort_values(by='mileage_difference', ascending = False).head(1)

# Honda Civic

# i. compact car with lowest mileage and highest



mpg[mpg['class'].str.match('compact')].sort_values(by='mileage_difference').tail(1)

mpg[mpg['class'].str.match('compact')].sort_values(by='mileage_difference').head(1)

# can also use: compact_cars = mpg[mpg['class'] == 'compact']

#highest: Audi A4 lowest Subaru Impreza

# j. create column named average_mileage (mean of city and highway mileage)

mpg['average_mileage'] = mpg.hwy + mpg.cty // 2

# k. Find dodge car with best and worst mileage

mpg[mpg['manufacturer'].str.match('dodge')].sort_values(by='average_mileage').tail(1)

mpg[mpg['manufacturer'].str.match('dodge')].sort_values(by='average_mileage').head(1)

# can also do .min() or .max() to get all values with lowest or highest

# Highest: Dodge Caravan 2WD    Lowest: Dodge Ram 1500 4WD

# 3. Load mammals dataset

mammals = data('Mammals', show_doc=True)

#a. How man rows and columns

mammals.shape

# 62, 2

#b. data types

mammals.dtypes

#c. summarize with .info and .describe

mammals.info()

mammals.describe()

#d. weight of fastest mammal

mammals.sort_values(['speed]']).tail

# weights is 55

#e. overall percentage of specials

percent_specials = (mammals['specials'].value_counts())/len(mammals)

#9.3%

#f. number of hopper mammals above median speed? Percentage of the same?

median = mammals['speed'].median()

mammals[(mammals.hoppers == True) & (mammals.speed > mammals.speed.median())]