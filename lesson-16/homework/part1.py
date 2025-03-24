import pandas as pd
import sqlite3
import csv
import numpy as np

def problem1():
    with sqlite3.connect('data/chinook.db') as connector:
        df_customers = pd.read_sql(
            "Select * FROM customers",
            con = connector
        )
    print(df_customers.head(10))

def problem2():
    df_iris = pd.read_json('data/iris.json')
    print(f"The shape of dataset is {df_iris.shape[0]}x{df_iris.shape[1]}")
    column_names = df_iris.columns
    print("Column names:")
    for column in column_names:
        print(column)

def problem3():
    df_titanic = pd.read_excel('data/titanic.xlsx')
    print(df_titanic.head())

def problem4():
    df_flights = pd.read_parquet('data/flights')
    print(df_flights.info())
    
def problem5():
    df_movie = pd.read_csv('data/movie.csv')
    print(df_movie.sample(10))
problem5()
