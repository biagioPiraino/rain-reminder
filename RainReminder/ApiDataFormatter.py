from WeatherCondition import WeatherCondition
from datetime import datetime as dt

class ApiDataFormatter:
  def __init__(self) -> None:
    pass

  @classmethod
  def FormatWeatherCondition(self, data: dict) -> WeatherCondition:
    weather_condition = WeatherCondition(
      dt.fromtimestamp(data["dt"]),
      data["weather"][0]["id"],
      data["weather"][0]["description"]
    )
    return weather_condition  