import requests
import config

# Получение прогноза по городу
def get_location(city):
    url = f"http://api.openweathermap.org/data/2.5/find"
    params = {
        "q": city,
        "appid": config.apitoken,
        "units" : "metric"
    }
    response = requests.get(url, params).json()
    return response

# Получение прогноза по координатам
def get_from_coords(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": config.apitoken,
        "units": "metric"
    }
    response = requests.get(url, params).json()
    return response

def format_answer(response):
    answer = ''
    for loc in response['list']:
            answer +=   f'Страна: {loc['sys']['country']}\n'\
                        f'Город: {loc['name']}\n'\
                        f'Координаты: {loc['coord']['lat']} {loc['coord']['lon']}\n'\
                        f'Температура: {loc['main']['temp']}C\n'\
                        f'Ощущается как: {loc['main']['feels_like']}C\n\n'
    return answer

if __name__ == "__main__":
    city = input()
    print(format_answer(get_location(city)))


