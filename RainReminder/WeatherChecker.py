from ApiRequester import ApiRequester as Requester
from WeatherEnums import WeatherCondition

class WeatherChecker:
  def __init__(self) -> None:
    self.__weather_condition: WeatherCondition

  def IsGonnaRain(self) -> bool:
    weather_forecast = Requester.RequestWeatherForecast()
    for weather_condition in weather_forecast:
      if (weather_condition.GetWeatherCondition() == WeatherCondition.Thunderstorm or
          weather_condition.GetWeatherCondition() == WeatherCondition.Drizzle or
          weather_condition.GetWeatherCondition() == WeatherCondition.Rain):
        self.__load_weather_condition(weather_condition)
        return True

    return False
  
  def GetWeatherCondition(self) -> WeatherCondition:
    return self.__weather_condition

  def __load_weather_condition(self, weather_condition: WeatherCondition):
    self.__weather_condition = weather_condition