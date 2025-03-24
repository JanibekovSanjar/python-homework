import pandas as pd
import numpy as np

def problem1():
    df_iris = pd.read_json('data/iris.json')
    print("Mean value of each column:")
    print(df_iris.select_dtypes('number').mean())
    print("Median value of each column:")
    print(df_iris.select_dtypes('number').median())
    print("Standart deviation of each column:")
    print(df_iris.select_dtypes('number').std())

def problem2():
    df_titanic = pd.read_excel('data/titanic.xlsx')
    print(f'Minimum age: {df_titanic['Age'].min()}')
    print(f'Maximum age: {df_titanic['Age'].max()}')
    print(f'Sum of all passengers age: {df_titanic['Age'].sum()}')

def problem3():
    df_movie = pd.read_csv('data/movie.csv')
    print(df_movie[['director_name','director_facebook_likes']].sort_values(by = 'director_facebook_likes',ascending=False).head(1)['director_name'])
    print(df_movie[['director_name','duration']].sort_values(by='duration',ascending=False).head())

def problem4():
    df_flights = pd.read_parquet('data/flights')
    for column in df_flights.select_dtypes('number').columns:
        df_flights[column].fillna(df_flights[column].mean(), inplace=True)
problem4()