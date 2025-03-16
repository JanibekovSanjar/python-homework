from bs4 import BeautifulSoup

# Read the HTML file
with open('weather.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
rows = soup.find('tbody').find_all('tr')

def display_weather_data():  
    for row in rows:
        columns = row.find_all('td')  
        day = columns[0].text.strip()
        temperature = columns[1].text.strip()
        condition = columns[2].text.strip()
        
        print(f"Day: {day}, Temperature: {temperature}, Condition: {condition}")

def find_highest_temperature():
    temperatures = []
    for row in rows:
        columns = row.find_all('td')
        temp = columns[1].text.strip()
        numeric_value = int(''.join(filter(str.isdigit, temp)))
        temperatures.append(numeric_value)
    print(max(temperatures))

def find_specific_condition():
    Days = []
    for row in rows:
        columns = row.find_all('td')
        condition = columns[2].text.strip()
        if condition == "Sunny":
            Days.append(columns[0].text.strip())
    print("Sunny days:", ", ".join(Days))

def calculate_average_temperature():
    temperatures = []
    for row in rows:
        columns = row.find_all('td')
        temp = columns[1].text.strip()
        numeric_value = int(''.join(filter(str.isdigit, temp)))
        temperatures.append(numeric_value)
    print(f"Average temperature of the week: {sum(temperatures)//len(temperatures)}°C")

def main():
    display_weather_data()
    find_highest_temperature()
    find_specific_condition()
    calculate_average_temperature()

if __name__ == "__main__":
    main()


    
