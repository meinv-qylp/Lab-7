import requests


API_KEY = "balabala"


CITY = input(
    "Select city(for example:Beijing, Moscow, London) :"
)


url = "https://api.openweathermap.org/data/2.5/weather"


canshu = {
    "appid": API_KEY,
    "q": CITY,
}

def output():
    global i, data
    main_data = data['main']
    weather_data = data['weather'][0]
    sys_data = data['sys']
    
    print(f"{i}. Weather in {data['name']}, {sys_data.get('country', '')}")
    print(f"   Temperature: {main_data['temp']}°C")
    print(f"   Humidity: {main_data['humidity']}%")
    print(f"   Air pressure: {main_data['pressure']} hPa")
    print(f"   Weather: {weather_data['description']}")

    
try:
    response = requests.get(url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        main_data = data['main']
        weather_data = data['weather'][0]
        wind_data = data['wind']
        sys_data = data['sys']
        
        print("\n" + "="*50)
        print(f"city: {data['name']}, {sys_data.get('country', '')}")
        print("="*50)
        print(f"temperature: {main_data['temp']}K")
        print(f"humidity: {main_data['humidity']}%")
        print(f"air pressure: {main_data['pressure']}hPa")
        print(f"weather: {weather_data['description']}")
        print("="*50)
        
    else:
        error_msg = data.get('message', 'error')
        print(f"failed: {error_msg}")


except Exception as e:
    print(f"Program error: {e}")