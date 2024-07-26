import requests

api_key = '0ece958fa3930e44b6be4fc179dfaf5c'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp_f = round(weather_data.json()['main']['temp'])
    temp_c = round((temp_f - 32) * 5/9, 1)


    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp_f}ºF ({temp_c})ºC")