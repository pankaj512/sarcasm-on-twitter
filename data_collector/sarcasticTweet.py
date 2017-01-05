import pandas as pd
from data_collector import web_parser
from data_process import data_refresh

# Search with #sarcasm and first 2 page

tweet_text, user_name, sarcastic_value = web_parser.parse_by_tag(tag='Sarcasm', page=50,sarcastic='Yes')

# process tweets of tweet_text
tweet_text,user_name = data_refresh.myrefresher(tweet_text,user_name)
sarcastic_value  = sarcastic_value[0:len(tweet_text)]

# Create data frame
df_dict = {'User': user_name,'Tweet Text': tweet_text, 'Sarcastic': sarcastic_value}
df_data_1 = pd.DataFrame(df_dict)

print("Done with tag :Sarcastic ")

# Search with sarcastic account username and first 2 page
sarcastic_account = ['SarcasmProfile','ItsHumorTruth','SarcasmPage','OneMoreJoke','TheFunnyTeens','FunnySayings','TheTumblrPosts','sarcasquotes','sarcasticquotes','FunnyQuotes428']

sarcastic_account = ['Sarcasm_So']
id = 1
tweet_text = []
user_name = []
sarcastic_value = []

for user in sarcastic_account:
    print('Processing User #'+str(id)+'/'+str(len(sarcastic_account))+' '+user)
    tweet_list , user_list , sarcastic_list = web_parser.parse_by_id(user,25,sarcastic='Yes')
    tweet_text += tweet_list
    user_name += user_list
    sarcastic_value += sarcastic_list
    print(" Done ")
    id += 1

print("Done with All Users")

# process tweets of tweet_text
tweet_text,user_name = data_refresh.myrefresher(tweet_text,user_name)
sarcastic_value = sarcastic_value[0:len(user_name)]

# Create data frame
df_dict_2 = {'User': user_name,'Tweet Text': tweet_text, 'Sarcastic': sarcastic_value}
df_data_2 = pd.DataFrame(df_dict_2)

# combine both data frame
frames = [df_data_1 , df_data_2]
full_data = pd.concat(frames)

#df_data_2.to_excel('new_sarcastic_2.xlsx',sheet_name='sheet 1',index=False)


import os
os.chdir("../data/")

#full_data.to_excel('data/train_Data_sarcastic.xlsx', sheet_name='sheet 1', index=False)