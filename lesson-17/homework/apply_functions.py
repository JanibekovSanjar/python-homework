import pandas as pd
from sklearn.preprocessing import normalize
import numpy as np

def problem1():
    df_titanic = pd.read_excel('data/titanic.xlsx')
    def func(x):
        if x>=18:
            return 'Adult'
        else:
            return 'Child'
    df_titanic['Age_Group']=df_titanic['Age'].apply(func)
    print(df_titanic)

def problem2():
    df_employee = pd.read_csv('data/employee.csv')
    def normalize_salaries(group):
        group['Normalized_Salary'] = (group['BASE_SALARY'] - group['BASE_SALARY'].min()) / (group['BASE_SALARY'].max() - group['BASE_SALARY'].min())
        return group
    result = df_employee.groupby('DEPARTMENT').apply(normalize_salaries)
    print(result)

def problem3():
    df_movie = pd.read_csv('data/movie.csv')
    def func(x):
        if x>60:
            return 'Short'
        elif x<120:
            return 'Medium'
        else:
            return 'Long'
    print(df_movie['duration'].apply(func))
problem3()
    
