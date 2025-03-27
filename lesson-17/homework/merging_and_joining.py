import pandas as pd
import sqlite3

def problem1():
    connector = sqlite3.connect('data/chinook.db')
    df_customers = pd.read_sql('SELECT * FROM customers',con=connector)
    df_invoices = pd.read_sql('SELECT * FROM invoices',con=connector)
    result = pd.merge(df_customers,df_invoices,on='CustomerId',how='inner')
    total_invoices = result.groupby('CustomerId')['Total'].sum().reset_index()
    total_invoices.rename(columns={'Total': 'Total_Invoices'}, inplace=True)
    df_customers = pd.merge(df_customers, total_invoices, on='CustomerId', how='left')
    print(df_customers[['FirstName', 'LastName', 'Total_Invoices']])

def problem2():
    df_movie = pd.read_csv('data/movie.csv')
    df1 = df_movie[['director_name','color']]
    df2 = df_movie[['director_name','num_critic_for_reviews']]
    left_join = pd.merge(df1,df2,on = 'director_name',how='left')
    outer_join = pd.merge(df1,df2,on = 'director_name',how='outer')
    print(f"Number of rows in left_join: {len(left_join)}")
    print(f"Number of rows in outer_join: {len(outer_join)}")

