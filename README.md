## POST
Я отправляю GET-запрос к /posts на JSONPlaceholder. Из ответа беру первые пять постов и вывожу заголовок и текст каждого.
```
python3 posts.py
```
## Weather
Сначала я ввожу название города, например Москва. По названию скрипт находит координаты города в OpenWeather, а потом по ним запрашивает погоду. На экране вижу температуру в градусах Цельсия и описание погоды на русском.

Для запуска нужен ключ OpenWeather. Вместо ваш_ключ подставьте свой ключ.

**MacOS & Linux**

```
export OPENWEATHER_API_KEY="ваш_ключ"
python3 weather.py
```

**Windows / PowerShell**
```
$env:OPENWEATHER_API_KEY = "ваш_ключ"
py weather.py
```
