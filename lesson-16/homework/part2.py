import pandas as pd
import sqlite3
import csv
import numpy as np

def problem1():
    df_iris = pd.read_json('data/iris.json')
    columns = df_iris.columns
    lowered_columns = [column.lower() for column in columns]
    df_iris.columns = lowered_columns
    
    print(df_iris[['sepallength','sepalwidth']])

def problem2():
    df_titanic = pd.read_excel('data/titanic.xlsx')
    print(df_titanic[df_titanic['Age']>30])
    print("****************************************")
    print(f"The number of male: {df_titanic.value_counts('Sex')['male']}")
    print(f"The number of female: {df_titanic.value_counts('Sex')['female']}")

def problem3():
    df_flights = pd.read_parquet('data/flights')
    print(df_flights['dest'].nunique())

def problem4():
    df_movie = pd.read_csv('data/movie.csv')
    df_movie = df_movie.query("duration > 120")
    print(df_movie['director_facebook_likes'].sort_values(ascending=False).dropna())

problem4()