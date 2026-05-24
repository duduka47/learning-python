import requests
import sys
from twilio.rest import Client
import os

API_KEY=os.environ.get("API_KEY")
LAT=os.environ.get("LAT")
LONG=os.environ.get("LONG")
OWM_ENDPOINT=os.environ.get("OWM_ENDPOINT")
ACCOUNT_SID =os.environ.get("ACCOUNT_SID")
ACCOUNT_TOKEN =os.environ.get("ACCOUNT_TOKEN")
PHONE = os.environ.get("PHONE")
TO_PHONE = os.environ.get("TO_PHONE")

parameters = {
   "lat": LAT,
   "lon": LONG,
   "appid": API_KEY,
   "cnt": 4
}

try:
   response = requests.get(url=OWM_ENDPOINT, params=parameters)
   response.raise_for_status()
   data = response.json()

   needs_umbrella = False

   for item in data["list"]:
      if int(item["weather"][0]["id"]) < 700:
         needs_umbrella = True
         client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)
         message = client.messages.create(body="Vai chover hoje fiote, traz um guarda chuva 🌧️", to=TO_PHONE, from_=PHONE)
         print(message.status)
         break

except requests.exceptions.HTTPError as error:
   if error.response.status_code == 401:
      print("You're not allowed to use the API with this key yet. Try again later or use another key.")
      sys.exit(1)
   else:
      print("Error not treated", error)
      sys.exit(1)