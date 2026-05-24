import requests
import time
import sys

parameters = {
   "amount": 10,
   "type": "boolean"
}

question_data = []

def fetch():
   response = requests.get('https://opentdb.com/api.php', params=parameters)
   response.raise_for_status()
   data = response.json()
   return data["results"]

try:
   question_data = fetch()
except requests.exceptions.HTTPError as err:
   if err.response.status_code == 429:
      print('Rate limited by API, trying again in 5 seconds')
      time.sleep(5)
      question_data = fetch()
   else:
      print(f'An http error ocurred {err}')
      sys.exit(1)

