import pandas as pd

def problem1():
    df_titanic = pd.read_excel('data/titanic.xlsx')
    new_df = df_titanic.groupby('Pclass').agg({
        'Age':'mean',
        'Fare':'sum',
        'Name':'count'
    })
    new_df.rename(columns={'Age':'average_age','Fare':'total_fare','Name':'count_of_passengers'},inplace=True)
    print(new_df)

def problem2():
    df_movie = pd.read_csv('data/movie.csv')
    grouped = df_movie.groupby(['color', 'director_name'])
    
    result = grouped.agg({
        'num_critic_for_reviews': 'sum',
        'duration': 'mean'
    })
    print(result)

def problem3():
    df_flights = pd.read_parquet('data/flights')
    group = df_flights.groupby(['Year','Month'])
    df_flights['ArrDelay'] = pd.to_numeric(df_flights['ArrDelay'], errors='coerce')

    result = group.agg({
        'FlightDate': 'size',       
        'ArrDelay': 'mean',        
        'DepDelay': 'max'          
    }).reset_index()
    
    result.rename(columns={
        'FlightDate': 'Total_Flights',
        'ArrDelay': 'Average_Arrival_Delay',
        'DepDelay': 'Max_Departure_Delay'
    }, inplace=True)
    print(result)
