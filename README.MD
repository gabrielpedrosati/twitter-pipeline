# Extracting Tweets From Twitter And Storing Into S3 Bucket

## Goal
Extract 100 tweets every 10 minutes that have embraced the word "Brazil" in their body. It could be any other topic, but for this example I want to store what people are saying about Brazil. It's a great tool for discover what people are saying about your business.

## Technologies
For this project I'm working with Apache Airflow for the orchestration and monitoring of my pipeline. Tweepy for interacting with the Twitter API. Boto3 to interact with my AWS account.

## Requirements
- Apache Airflow;
- Twitter Developer Account;
- Tweepy;
- Boto3;
- AWS Credentials;
- Pandas.

## DAG
!["DAG"](/imgs/etl-twitter.png)

## Tweets
!["Tweets"](/imgs/tweets.png)