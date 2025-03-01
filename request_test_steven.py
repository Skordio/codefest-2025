import requests

headers = {
    'Content-Type': 'application/json',
}
r = requests.get("http://developer.phila.gov/api/phila/calendars/v1?format=json", headers=headers)
print(dir(r))
print(r.status_code)