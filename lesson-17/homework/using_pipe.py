import pandas as pd

def problem1():
    df_titanic = pd.read_excel('data/titanic.xlsx')
    def filter_survived(df):
        return df[df['Survived'] == 1]
    
    def fill_missing_age(df):
        df['Age'] = df['Age'].fillna(df['Age'].mean())
        return df
    
    def create_fare_per_age(df):
        df['Fare_Per_Age'] = df['Fare'] / df['Age']
        return df
    df_titanic = (
        df_titanic
        .pipe(filter_survived)
        .pipe(fill_missing_age)
        .pipe(create_fare_per_age)
    )
    print(df_titanic)

def problem2():
    df_flights = pd.read_parquet('data/flights')
    
    def filter_delayed_flights(df):
        return df[df['DepDelay'] > 30]
    
    def add_delay_per_hour(df):
        df['Delay_Per_Hour'] = df['DepDelay'] / (df['AirTime'] / 60) 
        return df
    
    df_flights = (
        df_flights
        .pipe(filter_delayed_flights)
        .pipe(add_delay_per_hour)
    )
    
    print(df_flights)

problem2()