#DSC 510
#Week 10
#Weather Program Final
#Author Danish Khan
#8/12/2023

import requests


def get_zip(api):
    #zip look up
    print("\nLook Up By: ZIP")
    user_zip = input("Enter 5-Digit Zip Code:").replace(" ", "")
    while True:
        #zip code length/numeric error check
        if len(user_zip) != 5 or not user_zip.isnumeric():
            user_zip = input("Try Again:").replace(" ", "")
        else:
            break
    user_state = input("Enter 2-Letter State Code:").upper().replace(" ", "")
    while True:
        #state code length/alpha error check
        if len(user_state) != 2 or not user_state.isalpha():
            user_state = input("Try Again:").upper().replace(" ", "")
        else:
            break
    user_country = input("Enter 2-Letter Country Code:").upper().replace(" ", "")
    while True:
        #country code length/alpha error check
        if len(user_country) != 2 or not user_country.isalpha():
            user_country = input("Try Again:").upper().replace(" ", "")
        else:
            break
    url = 'http://api.openweathermap.org/geo/1.0/zip'
    payload = {'zip': user_zip + ',' + user_country, 'appid': api}
    #url check and exceptions
    try:
        response = requests.get(url, params=payload, timeout=5)
        print("...connection <zip api> successful...")
    except requests.exceptions.Timeout:
        print("\nTimeout Error - Restart")
        exit()
    except requests.exceptions.ConnectionError:
        print("\nConnection Error - Restart")
        exit()
    data = response.json()
    if response.status_code == 404:
        print("\nInvalid User Data Entered - Restart")
        exit()
    else:
        lat = (data['lat'])
        lon = (data['lon'])
        return get_weather(lat, lon, user_state, api)


def get_city(api):
    #city look up
    print("\nLook Up By: CITY")
    user_city = input("Enter City Name:").lower().replace(" ", "")
    while True:
        #city alpha error check
        if not user_city.isalpha():
            user_city = input("Try Again:").lower().replace(" ", "")
        else:
            break
    user_state = input("Enter 2-Letter State Code:").upper().replace(" ", "")
    while True:
        #state code length/alpha error check
        if len(user_state) != 2 or not user_state.isalpha():
            user_state = input("Try Again:").upper().replace(" ", "")
        else:
            break
    user_country = input("Enter 2-Letter Country Code:").upper().replace(" ", "")
    while True:
        #country code length/alpha error check
        if len(user_country) != 2 or not user_country.isalpha():
            user_country = input("Try Again:").upper().replace(" ", "")
        else:
            break
    url = 'http://api.openweathermap.org/geo/1.0/direct'
    payload = {'q': user_city + ',' + user_state + ',' + user_country, 'appid': api}
    #url check and exceptions
    try:
        response = requests.get(url, params=payload, timeout=5)
        print("...connection <city api> successful...")
    except requests.exceptions.Timeout:
        print("\nTimeout Error - Restart")
        exit()
    except requests.exceptions.ConnectionError:
        print("\nConnection Error - Restart")
        exit()
    data = response.json()
    if not data:
        print("\nInvalid User Data Entered - Restart")
        exit()
    else:
        for item in data:
            lat = item['lat']
            lon = item['lon']
            return get_weather(lat, lon, user_state, api)


def get_weather(lat, lon, user_state, api):
    #weather look up by lat/lon
    unit_sign = ()
    user_unit = input("Select Weather Data Units (Imperial/Metric/Standard):").lower().replace(" ", "")
    while True:
        if user_unit == 'standard':
            unit_sign = 'K'
            break
        elif user_unit == 'imperial':
            unit_sign = 'F'
            break
        elif user_unit == 'metric':
            unit_sign = 'C'
            break
        elif user_unit != 'standard' or 'imperial' or 'metric':
            #selection error check
            user_unit = input("Try Again:").lower().replace(" ", "")
    url = 'https://api.openweathermap.org/data/2.5/weather'
    payload = {'units': user_unit, 'lat': lat, 'lon': lon, 'appid': api}
    #url check and exceptions
    try:
        response = requests.get(url, params=payload, timeout=5)
        print("...connection <weather api> successful...")
    except requests.exceptions.Timeout:
        print("\nTimeout Error - Restart")
        exit()
    except requests.exceptions.ConnectionError:
        print("\nConnection Error - Restart")
        exit()
    data = response.json()
    if response.status_code != 200:
        print("\nInvalid User Data Entered - Restart")
        exit()
    else:
        return print_weather(data, user_state, unit_sign)


def print_weather(data, user_state, unit_sign):
    #string format for printing data
    print("\n\n\nCURRENT FORECAST")
    print(f"{'Category':15}", "Data")
    print("_"*30)
    print(f"{'Location':15}", data['name']+",", user_state, "\n"
          f"{'Temperature':15}", data['main']['temp'], f'\u00b0{unit_sign}', "\n"
          f"{'Feels Like':15}", data['main']['feels_like'], f'\u00b0{unit_sign}', "\n"
          f"{'High':15}", data['main']['temp_max'], f'\u00b0{unit_sign}', "\n"
          f"{'Low':15}", data['main']['temp_min'], f'\u00b0{unit_sign}', "\n"
          f"{'Pressure':15}", data['main']['pressure'], "hPa", "\n"
          f"{'Humidity':15}", data['main']['humidity'], "%")
    for item in data['weather']:
        print(f"{'Sky':15}", item['main'].title(), "\n"
              f"{'Sky Desc.':15}", item['description'].title())
    print("_" * 30, "\n\n\n")


def main():
    #main code
    api = 'ad04c63a71b630dc986df404da34f584'
    print("\nWELCOME TO Danish Khan WEATHER PROGRAM")
    select = input("\nSelect (Zip/City) to Look Up Weather Data or (Exit) to Quit:").lower().replace(" ", "")
    while True:
        #loop for multiple weather look up
        if select == 'zip':
            get_zip(api)
            select = input("Select (Zip/City) to Look Up Additional Weather Data or (Exit) to Quit:"
                           ).lower().replace(" ", "")
        elif select == 'city':
            get_city(api)
            select = input("Select (Zip/City) to Look Up Additional Weather Data or (Exit) to Quit:"
                           ).lower().replace(" ", "")
        elif select == 'exit':
            break
        elif select != 'zip' or 'city' or 'exit':
            #selection error check
            select = input("Try again:").lower().replace(" ", "")
    print("\nTHANK YOU FOR USING Danish Khan WEATHER PROGRAM")
    exit()


if __name__ == "__main__":
    main()
