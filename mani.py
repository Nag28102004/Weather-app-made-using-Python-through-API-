import requests
import json 

    
API_KEY = '35657ae8134ec10677567502d0525a10'

city = input("enter the name of the city ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try : 

    r = requests.get(url)
    r.raise_for_status()
    data = r.json()

    print(f"""
    ====================================================================
    {city.upper()}

    Temperature : {data['main']['temp']}°C
    Actually feels like : {data['main']['feels_like']}°C
    Weather : {data['weather'][0]['description'].title()}
    Wind Speed : {data['wind']['speed']} m/s
    """)

except requests.exceptions.HTTPError:

    if r.status_code == 404:
        print("City not found ")

    elif r.status_code == 401:
        print("Invalid Api key ")

    else:
        print(f"HTTP error : {r.status_code}")
    
except requests.exceptions.ConnectionError:
    print("connection not found ")

except requests.exceptions.Timeout:
    print("Connection time out")
except requests.exceptions.RequestException as e :
    print("Something went wrong ")
    