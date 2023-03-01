import smtplib as smt
from WeatherCondition import WeatherCondition
from MessageOriginator import MessageOriginator as Originator
from ParametersReader import ParametersReader as PR

class MessageSender:
  def __init__(self) -> None:
    pass

  @classmethod
  def SendMessage(self, weather_condition: WeatherCondition) -> None:
    try:
      with self.__connect() as connection:
        connection.sendmail(
          from_addr=connection.user, 
          to_addrs=PR.RetrieveRecipientEmail(), 
          msg=Originator.OriginateMessage(weather_condition))
    except (smt.SMTPHeloError, smt.SMTPAuthenticationError,
      smt.SMTPConnectError, smt.SMTPException) as error:
      print(error)

  @classmethod
  def __connect(self) -> smt.SMTP:
    smtp_connection = smt.SMTP(PR.RetrieveConnectionString())
    smtp_connection.starttls()
    credentials = PR.RetrieveSenderCredentials() 
    smtp_connection.login(user=credentials["email"], password=credentials["password"])
    return smtp_connection