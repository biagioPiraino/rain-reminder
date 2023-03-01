from WeatherCondition import WeatherCondition
from ParametersReader import ParametersReader as PR

class MessageOriginator:
  def __init__(self) -> None:
    pass

  @classmethod
  def OriginateMessage(self, weather_condition: WeatherCondition) -> str:
    if (weather_condition == None):
      return self.__originate_no_rain_msg()
    return self.__originate_rain_msg(weather_condition)
  
  @classmethod
  def __originate_no_rain_msg(self) -> str:
    return f"No rain is expected in the following {str(PR.RetrieveHoursRange())} hours"

  @classmethod
  def __originate_rain_msg(self, weather_condition: WeatherCondition) -> str:
    return f"Remember to take an umbrella.\nIt is expected {weather_condition.GetDescription()} at {str(weather_condition.GetForecastTime())}"