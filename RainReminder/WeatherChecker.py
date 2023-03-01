from ApiRequester import ApiRequester as Requester
from WeatherEnums import WeatherCondition

class WeatherChecker:
  def __init__(self) -> None:
    pass

  @classmethod
  def ForecastRainyWeather(self) -> WeatherCondition:
    weather_forecast = Requester.RequestWeatherForecast()
    for weather_condition in weather_forecast:
      if (weather_condition.GetWeatherCondition() == WeatherCondition.Thunderstorm or
          weather_condition.GetWeatherCondition() == WeatherCondition.Drizzle or
          weather_condition.GetWeatherCondition() == WeatherCondition.Rain):
        return weather_condition

    return None