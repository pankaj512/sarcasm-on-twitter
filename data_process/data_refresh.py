import re


def myrefresher(tweet_text,user_name):
    tweets = []
    users = []
    print(len(tweet_text),len(user_name))

    if len(tweet_text)>len(user_name):
        for i in range(len(tweet_text)-len(user_name)):
            user_name.append('NA')

    for i in range(len(tweet_text)):
        if 'http' not in tweet_text[i]:
            words = re.split('@[a-z_A-Z0-9]+|#[a-zA-Z_0-9]+|twitter.com/[a-zA-Z0-9]+', tweet_text[i])
            line = ' '.join(words)
            tweets.append(line.strip())
            users.append(user_name[i])
    return tweets, users
