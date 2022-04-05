import json
import tweepy
import os
from random import choice, randint
import time
from dotenv import load_dotenv
load_dotenv()


def get_client():
    """Activate sputnik to make requests to the api"""
    client = tweepy.Client(
        consumer_key=os.getenv("api_key"),
        consumer_secret=os.getenv("api_secret"),
        access_token=os.getenv("access_token"),
        access_token_secret=os.getenv("access_secret"),
        bearer_token=os.getenv("bearer_token"),
        wait_on_rate_limit=True)
    return client


def new_tweet(text):
    """Create a new tweet for Larry Anderson"""
    sputnik.create_tweet(text=text)
    print("success")


def get_user_details(username):
    """Get twitter ID, Name and Username for chosen account, username=string twitter handle without @ """
    user_info = sputnik.get_users(usernames=username)
    print(user_info)


def get_last_tweet_id(user_id):
    """Return the last tweet id from a chosen user as an integer, user_id is the user int id number"""
    last_tweet = sputnik.get_users_tweets(user_id, exclude=["retweets", "replies"])
    tweet_meta = last_tweet.meta
    result = int(tweet_meta['newest_id'])
    print(result)
    return result


def get_mention():
    """Return the tweet id number for the last person who mentioned Larry"""
    mentions = sputnik.get_users_mentions(1503766612519706627)
    mention_data = mentions.data

    results = []
    if mention_data:
        for tweet in mention_data:
            results.append(int(tweet.id))
        print(results[0])
        return results[0]


def respond_to_tweet(tweet_id_number):
    """Respond to a tweet that mentions Larry"""
    # Get the user's information who sent the tweet
    username = sputnik.get_tweet(id=tweet_id_number, expansions=["author_id"])
    # gets just the username of the person who sent a message to Larry
    ids = username.includes["users"][0]

    with open("insult_info.json", "r") as f:
        data = json.load(f)
        text = choice(data)

        with open("template1.txt") as letter:
            contents = letter.read()
            contents = contents.replace("[NAME]", str(ids))
            contents = contents.replace("[TEXT]", text)

    sputnik.create_tweet(in_reply_to_tweet_id=tweet_id_number, text=contents)


# Activate Sputnik
sputnik = get_client()


respond_to_tweet(1511195457581592580)


