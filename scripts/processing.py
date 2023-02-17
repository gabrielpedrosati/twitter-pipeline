import tweepy
import pandas as pd
from config.credentials import *
import boto3

def _extract_data():
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    query = 'Brasil'
    tweets = [tweet for tweet in tweepy.Cursor(api.search_tweets, q=query, lang='pt', result_type='mixed', count=100, tweet_mode='extended').items(100)]

    tweet_dict = []
    for tweet in tweets:
        tweet_dict.append(tweet._json)

    tweets_df = pd.DataFrame(columns=['create_at','text','user_id','user_name','text_no_retweet','text_no_likes'])

    for index, tweet in enumerate(tweet_dict):
        tweets_df.loc[index] = [tweet['created_at'],tweet['full_text'],tweet['user']['screen_name'],tweet['user']['name'],tweet['retweet_count'],tweet['favorite_count']]

    tweets_df.to_csv('/opt/airflow/dags/data/tweets.csv', index=False)

def _upload_to_s3(filename, bucket, key):
    s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY)
    s3.meta.client.upload_file(filename, bucket, key)