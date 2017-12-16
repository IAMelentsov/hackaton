import requests
import json
from hakaton import MessageProvider
from time import time
from datetime import datetime, timedelta


class WeatherProvider(MessageProvider):
    __yandex_api = 'https://yandex.ru/pogoda/front/maps/balloon?' \
                   'lat={}&lon={}&ts={}'

    def __init__(self, lat, lon):
        super().__init__()
        self.lat = lat
        self.lon = lon

    def get_yandex_weather(self):
        dt = datetime.fromtimestamp(time())
        dt = dt - timedelta(minutes=dt.minute, microseconds=dt.microsecond,
                            seconds=dt.second)
        dt = int(dt.timestamp())
        resp = requests.get(self.__yandex_api.format(self.lat, self.lon,
                                                     dt)).content
        js = json.loads(resp)
        forecast_from_ya = js['forecasts'][str(dt)]
        forecast = dict()
        forecast['temp'] = forecast_from_ya['temp']
        forecast['wind_speed'] = forecast_from_ya['wind_speed']
        forecast['pressure_mm'] = forecast_from_ya['pressure_mm']
        return forecast

    @property
    def get_message(self):
        yandex_forecast = self.get_yandex_weather()

        forecast = dict()
        forecast['temp'] = yandex_forecast['temp']
        forecast['wind_speed'] = yandex_forecast['wind_speed']
        forecast['pressure_mm'] = yandex_forecast['pressure_mm']
        return \
            'Сводка погоды - Температура: {} C; скорость ветра: {} м/с; ' \
            'давление: {} мм ртутного столба'.format(
                forecast['temp'],
                forecast['wind_speed'],
                forecast['pressure_mm']
            )


if __name__ == '__main__':
    w = WeatherProvider(58.46386865370605, 48.84027962499996)
    print(w.get_message)
