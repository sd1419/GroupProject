
import gather_keys_oauth2 as Oauth2
import fitbit
import pandas as pd 
import datetime

CLIENT_ID='2398RL'
CLIENT_SECRET='00148b3850f9852fe64e5eff7b41d161'

server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)

# This is the date of data that I want. 
# You will need to modify for the date you want
oneDate = pd.datetime(year = 2023, month = 1, day = 25)
oneDayData = auth2_client.intraday_time_series('activities/heart', oneDate, detail_level='1sec')

# The first part gets a date in a string format of YYYY-MM-DD
starttime = pd.datetime(year = 2023, month = 1, day = 24)
endtime= pd.datetime.today().date() 
import time
date_list = []
df_list= []
allDates = pd.date_range(start=starttime, end=endtime)

for oneDate in allDates:
    oneDate = oneDate.date().strftime("%Y-%m-%d")
    oneDayDta = auth2_client.intraday_time_series('activities/heart', base_date = '',detail_level='1sec')
    df = pd.DataFrame(oneDayDta['activities-heart-intraday']['dataset'])
    date_list.append(oneDate)
    df_list.append(df)

final_df_list=[]
print(df_list)


##print(df.iloc[-1:])

#time.sleep(5)
    
    # date_list.append(oneDate)
    # df_list.append(df)
    
#final_df_list = []

#for date, df in zip(date_list, df_list):
#    if len(df)==0:
#        continue
#    df.loc[:, 'date'] = pd.to_datetime(date)
#    final_df_list.append(df)
#final_df = pd.concat(final_df_list, axis=0)

#print(final_df.tail())