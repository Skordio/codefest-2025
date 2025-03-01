import requests

response = requests.get("http://api.phila.gov/phila/calendars/v1?format=json")
print(response.text)