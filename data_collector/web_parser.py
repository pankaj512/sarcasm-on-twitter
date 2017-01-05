import tweepy
from twitter_connection import twitterUrl


def parse_by_id(id, page,sarcastic):
    api = twitterUrl.getapi()
    tweet_list = []
    user_list = []
    sarcastic_value = []
    sarcasm_user_timeline_pages = tweepy.Cursor(api.user_timeline, id=id).pages(page)
    page_count = 1
    print("Page :",end=' ')
    for ans_page in sarcasm_user_timeline_pages:
        for tweet in ans_page:
            tweet_list.append(tweet.text)
            user_list.append(id)
            sarcastic_value.append(sarcastic)
        print(page_count,end=' ')
        page_count+=1
    return tweet_list, user_list, sarcastic_value


def parse_by_tag(tag, page,sarcastic):
    api = twitterUrl.getapi()
    tweet_list = []
    user_list = []
    sarcastic_value = []
    pages_with_tag_tweets = tweepy.Cursor(api.search, q=tag, show_user=True).pages(page)

    page_count = 1
    print("Page :",end=' ')
    for ans_page in pages_with_tag_tweets:
        for tweet in ans_page:
            offset = str(tweet.text).find(':')
            offset2 = str(tweet.text).find('@')
            if offset != -1:
                tweet_list.append(tweet.text[offset+1:])
                user_list.append(tweet.text[offset2:offset])
            else:
                tweet_list.append(tweet.text)
                user_list.append("None")
            sarcastic_value.append(sarcastic)
        print(page_count,end=' ')
        page_count += 1

    return tweet_list, user_list, sarcastic_value
