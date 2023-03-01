from WeatherChecker import WeatherChecker
from MessageSender import MessageSender

class Program:

  @classmethod
  def RunProgram(self) -> None:
    forecast_rainy_weather = WeatherChecker.ForecastRainyWeather()
    MessageSender.SendMessage(forecast_rainy_weather)