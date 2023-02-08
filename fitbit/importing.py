#OAuth 2.0 Client 
#ID2398RLClient Secret00148b3850f9852fe64e5eff7b41d161
import fitbit 
import pandas as pd
import datetime


CLIENT_ID = '2398RL'
CLIENT_SECRET = '00148b3850f9852fe64e5eff7b41d161'

server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)