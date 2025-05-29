import requests

def fetch_stormglass(lat, lon, api_key):
    url = f'https://api.stormglass.io/v2/weather/point?lat={lat}&lng={lon}&params=waveHeight,swellHeight,windSpeed'
    headers = {
        'Authorization': api_key
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def fetch_weatherapi(lat, lon, api_key):
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_combined_weather(lat, lon, stormglass_key, weatherapi_key):
    stormglass_data = fetch_stormglass(lat, lon, stormglass_key)
    weatherapi_data = fetch_weatherapi(lat, lon, weatherapi_key)

    # Example: get first hour's data from Stormglass
    stormglass_hour = stormglass_data['hours'][0] if stormglass_data.get('hours') else {}

    combined = {
        'temperature_c': weatherapi_data['current']['temp_c'],
        'humidity': weatherapi_data['current']['humidity'],
        'condition': weatherapi_data['current']['condition']['text'],
        'waveHeight_m': stormglass_hour.get('waveHeight', {}).get('sg'),
        'swellHeight_m': stormglass_hour.get('swellHeight', {}).get('sg'),
        'windSpeed_mps': stormglass_hour.get('windSpeed', {}).get('sg'),
    }
    return combined

if __name__ == "__main__":
    STORMGLASS_API_KEY = 'bdcd10e4-3c83-11f0-89da-0242ac130006-bdcd1148-3c83-11f0-89da-0242ac130006'
    WEATHERAPI_KEY = '749ef7b6d061443ca12121812252905'

    latitude = 37.7749
    longitude = -122.4194

    data = get_combined_weather(latitude, longitude, STORMGLASS_API_KEY, WEATHERAPI_KEY)
    print(data)
