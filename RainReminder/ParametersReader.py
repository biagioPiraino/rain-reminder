import json
import os
from pathlib import Path

class ParametersReader:
  def __init__(self) -> None:
    pass

  @classmethod
  def RetrieveApiEndpoint(self) -> str:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    with open(file=Path(current_directory, "parameters.json"), mode="r") as file:
      data = json.load(file)
      return data["api_endpoint"]
  
  @classmethod
  def RetrieveApiKey(self) -> str:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    with open(file=Path(current_directory, "parameters.json"), mode="r") as file:
      data = json.load(file)
      return data["api_key"]
  
  @classmethod
  def RetrieveHoursRange(self) -> int:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    with open(file=Path(current_directory, "parameters.json"), mode="r") as file:
      data = json.load(file)
      return int(data["hours_range"])
  
  @classmethod
  def RetrieveCurrentPosition(self) -> dict:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    with open(file=Path(current_directory, "parameters.json"), mode="r") as file:
      data = json.load(file)
      current_position = {
        "lat" : data["current_position"]["latitude"],
        "lon" : data["current_position"]["longitude"]
      }
      return current_position
  
  @classmethod
  def RetrieveExcludeData(self) -> str:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    with open(file=Path(current_directory, "parameters.json"), mode="r") as file:
      data = json.load(file)
      return data["exclude_data"]

  @classmethod
  def RetrieveConnectionString(self) -> str:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    with open(file=Path(current_directory, "parameters.json"), mode="r") as file:
      data = json.load(file)
      return data["connection_string"]
    
  @classmethod
  def RetrieveRecipientEmail(self) -> str:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    with open(file=Path(current_directory, "parameters.json"), mode="r") as file:
      data = json.load(file)
      return data["recipient_email"]
    
  @classmethod
  def RetrieveSenderCredentials(self) -> dict:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    with open(file=Path(current_directory, "parameters.json"), mode="r") as file:
      data = json.load(file)
      credentials = {
        "email"    : data["credentials"]["email"],
        "password" : data["credentials"]["password"] 
      }
      return credentials