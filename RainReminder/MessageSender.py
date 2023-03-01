from WeatherCondition import WeatherCondition
from MessageOriginator import MessageOriginator as Originator

class MessageSender:
  def __init__(self) -> None:
    pass

  @classmethod
  def SendMessage(self, weather_condition: WeatherCondition) -> None:
    print(Originator.OriginateMessage(weather_condition))
