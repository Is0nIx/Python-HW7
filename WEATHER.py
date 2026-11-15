import json
import os
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen


def get_json(path, params):
    query = urlencode(params)
    url = f"https://api.openweathermap.org{path}?{query}"
    with urlopen(url, timeout=10) as response:
        return json.load(response)


def main():
    city = input("Введите название города: ").strip()
    if not city:
        print("Название города не может быть пустым.")
        return 1

    api_key = os.getenv("OPENWEATHER_API_KEY", "").strip()
    if not api_key:
        print("Укажите ключ OpenWeather в переменной OPENWEATHER_API_KEY.")
        return 1

    try:
        locations = get_json("/geo/1.0/direct", {
            "q": city,
            "limit": 1,
            "appid": api_key,
        })
        if not locations:
            print(f"Город «{city}» не найден.")
            return 1

        location = locations[0]
        weather = get_json("/data/2.5/weather", {
            "lat": location["lat"],
            "lon": location["lon"],
            "appid": api_key,
            "units": "metric",
            "lang": "ru",
        })
        temperature = weather["main"]["temp"]
        description = weather["weather"][0]["description"]
    except HTTPError as error:
        if error.code == 401:
            print("OpenWeather отклонил ключ API. Проверьте, что ключ указан верно и активирован.")
        else:
            print(f"OpenWeather вернул ошибку HTTP {error.code}.")
        return 1
    except (URLError, TimeoutError):
        print("Не удалось подключиться к OpenWeather.")
        return 1
    except (ValueError, KeyError, IndexError, TypeError):
        print("OpenWeather вернул данные в неожиданном формате.")
        return 1

    print(f"Текущая температура: {temperature} °C")
    print(f"Погода: {description}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
