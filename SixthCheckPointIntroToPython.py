#!/usr/bin/env python
# coding: utf-8

# In[54]:


# Write a Pandas program to create and display a DataFrame from the following dictionary data which has index labels.
import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

exam_dataframe = pd.DataFrame(exam_data , index=labels)
print("exam data frame")
print(exam_dataframe)
print('--------------------------------------------')
# Print the three first rows using head() method
three_first_row = exam_dataframe.head(3) 
print("the three first rows using head() method")
print(three_first_row)
print('--------------------------------------------')
# Delete rows with Nan values
print('Delete rows with Nan values')
exam_dataframe_withoutnan=exam_dataframe.dropna()
print(exam_dataframe_withoutnan)
print('--------------------------------------------')
# Extract the 'name' and 'score' columns from the DataFrame.
print('Extract the name and score columns from the DataFrame')
print(exam_dataframe_withoutnan.iloc[:, 0:2] )
print('--------------------------------------------')
# Write a Pandas program to append a new row 'k' to data frame with these values(name : "Suresh", score: 15.5, attempts: 1, qualify: "yes")
exam_dataframe_withoutnan.loc['k'] = ['Suresh', 15.5, 1, 'yes']
print('inserted k')
print(exam_dataframe_withoutnan)
print('--------------------------------------------')
# Write a Pandas program to delete the 'attempts' column from the DataFrame.
exam_dataframe_withoutnan.pop('attempts')
print('the attempts column deleted')
print(exam_dataframe_withoutnan)
print('--------------------------------------------')
# Add a new column "Success" : if the score is higher than 10 we will have 1 else we will have 0
def conditions (row):
   if row['score'] >= 10 :
      return 1
   else :
      return 0
exam_dataframe_withoutnan['Success'] = exam_dataframe_withoutnan.apply (lambda row: conditions(row), axis=1)
print("new column Success is added")
print(exam_dataframe_withoutnan)


# In[ ]:




