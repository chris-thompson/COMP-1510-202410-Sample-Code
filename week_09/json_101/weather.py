"""
Experiment with a weather API.
"""

import requests
import json


def get_forecast(url: str) -> None:
    """
    Retrieve and print the local forecast.
    :param url: an open weather API URL as a string
    :precondition: url must be correct
    :precondition: weather API is available
    :postcondition: prints the weather
    :postcondition: save the API response as a txt file
    """
    response = requests.get(url)
    with open("weather_json.txt", "w") as file_object:
        file_object.write(response.text)
    vancouver_weather = json.loads(response.text)
    local_weather = vancouver_weather['list']
    print('Current weather in Vancouver:')
    print(local_weather[0]['weather'][0]['main'], '-', local_weather[0]['weather'][0]['description'])


def main():
    """
    Drive the program. Apply for your own API key, but go ahead and try it out using mine!
    """
    vancouver = 6173331
    api_key = "73e6dd36a2a073c414a629760ac198ce"
    url = "http://api.openweathermap.org/data/2.5/forecast?id=6173331&APPID=73e6dd36a2a073c414a629760ac198ce"
    get_forecast(url)


if __name__ == "__main__":
    main()
