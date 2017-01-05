import pandas as pd
import os
import re

def get_training_data_list():

    os.chdir('../data/')

    df_sarcastic = pd.read_excel(io='Refine_sarcastic.xlsx',sheetname='Sheet 1')
    df_normal = pd.read_excel(io='Refine_normal.xlsx',sheetname='Sheet 1')


    # sarcastic tweets and labels
    sarcastic_tweets = df_sarcastic['Tweet Text'].tolist()
    sarcastic_labels = []
    for i in range(len(sarcastic_tweets)):
        sarcastic_labels.append(1)

    #normal tweets and labels
    normal_tweets = df_normal['Tweet Text'].tolist()
    normal_labels = []
    for i in range(len(normal_tweets)):
        normal_labels.append(0)

    # full tweets dataframe
    full_tweets_list = sarcastic_tweets + normal_tweets

    #full tweet labels
    full_labels_list = sarcastic_labels + normal_labels

    return full_tweets_list, full_labels_list

get_training_data_list()