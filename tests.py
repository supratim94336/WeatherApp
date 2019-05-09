from app_controller import WeatherController

wr = WeatherController()
print(wr.get_weather_reports('2019-05-01', '2019-05-03', '52.520008', '13.404954'))
