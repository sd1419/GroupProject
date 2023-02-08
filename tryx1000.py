import gather_keys_oauth2 as Oauth2
import fitbit
import pandas as pd
import datetime
import requests
import json # Fitbit API endpoint to retrieve real-time heart rate data

CLIENT_ID='2398RL'
CLIENT_SECRET='00148b3850f9852fe64e5eff7b41d161'


server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)


heart_rate_endpoint = "https://api.fitbit.com/1/user/-/devices/tracker/[tracker-id]/heart-rate/current.json" # Replace [tracker-id] with the ID of the Fitbit tracker
heart_rate_endpoint = heart_rate_endpoint.replace("[tracker-id]", "CLIENT_ID") # Access token obtained from OAuth 2.0 authorization
access_token =  ACCESS_TOKEN # Request header with authorization
header = {
"Authorization": "Bearer " + access_token
} # Make GET request to retrieve real-time heart rate data:
response = requests.get(heart_rate_endpoint, headers=header)
# Check if request was successful with code 200
if response.status_code == 200:
    # Parse JSON response
    heart_rate_data = json.loads(response.text)
    # Access heart rate data
    print("Heart rate data: ", heart_rate_data)
else: # Handle error
    print("Request failed with status code: ", response.status_code)



