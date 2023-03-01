import json

class ParametersReader:
  def __init__(self) -> None:
    pass

  @classmethod
  def RetrieveApiEndpoint(self) -> str:
    with open(file="parameters.json", mode="r") as file:
      data = json.load(file)
      return data["api_endpoint"]
  
  @classmethod
  def RetrieveApiKey(self) -> str:
    with open(file="parameters.json", mode="r") as file:
      data = json.load(file)
      return data["api_key"]
  
  @classmethod
  def RetrieveHoursRange(self) -> int:
    with open(file="parameters.json", mode="r") as file:
      data = json.load(file)
      return int(data["hours_range"])
  
  @classmethod
  def RetrieveCurrentPosition(self) -> dict:
    with open(file="parameters.json", mode="r") as file:
      data = json.load(file)
      current_position = {
        "lat" : data["current_position"]["latitude"],
        "lon" : data["current_position"]["longitude"]
      }
      return current_position