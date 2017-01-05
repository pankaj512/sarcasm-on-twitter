import pandas as pd
from data_collector import web_parser
from data_process import data_refresh

# Search with morality tag and first 2 page
tweet_text = []
user_name = []
sarcastic_value = []

tweet_text, user_name, sarcastic_value = web_parser.parse_by_tag(tag='goodthoughts', page=30,sarcastic='No')

# process tweets of tweet_text
tweet_text,user_name = data_refresh.myrefresher(tweet_text,user_name)
sarcastic_value = sarcastic_value[0:len(tweet_text)]

# Create data frame
df_dict = {'User': user_name,'Tweet Text': tweet_text, 'Sarcastic': sarcastic_value}
df_data_1 = pd.DataFrame(df_dict)

# Search with normal  account username and first 2 page

normal_account_1 = ['RealTalk','GreatestQuotes','Inspire_Us','lnspire_me','InspiringThinkn','MotivatedWorld_','MotivatedLiving','RobinSharma','InspowerMinds','DavidRoads','successmagazine']
normal_account_2= ['DeepLifeQuotes','DailyQuotes10','PositiveMinds__','LifelnWords','motivational','itslifethought','Positivevibe101','MotivatinQuotes','ReallyGoodIdea']
normal_account =normal_account_1 + normal_account_2

id = 1
for user in normal_account:
    print('Processing User #'+str(id)+'/'+str(len(normal_account))+' '+user)
    tweet_list , user_list , sarcastic_list = web_parser.parse_by_id(user,23,sarcastic='No')
    tweet_text += tweet_list
    user_name += user_list
    sarcastic_value += sarcastic_list
    print("Done ")
    id += 1

print("Done with All Users")

# process tweets of tweet_text
tweet_text,user_name = data_refresh.myrefresher(tweet_text,user_name)
sarcastic_value = sarcastic_value[0:len(user_name)]

# Create data frame
df_dict_2 = {'User': user_name,'Tweet Text': tweet_text, 'Sarcastic': sarcastic_value}
df_data_2 = pd.DataFrame(df_dict_2)
#df_data_2.to_excel('new_normal.xlsx',sheet_name='sheet 1',index=False)

# Combine both data frame
frames = [df_data_1 , df_data_2]
full_data = pd.concat(frames)

import os
os.chdir("../data/")

#full_data.to_excel('Data_normal.xlsx', sheet_name='sheet 1', index=False)
