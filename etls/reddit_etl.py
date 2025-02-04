import praw
from praw import Reddit
import sys

def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = praw.reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)
        print('connected to Reddit')
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)
