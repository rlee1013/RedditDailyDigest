import praw
import os

def create_reddit_instance():
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent=os.getenv("USER_AGENT"),
        username=os.getenv("USERNAME"),
        password=os.getenv("PASSWORD")
    )
    return reddit

def get_top_posts(subreddit):
    return subreddit.top(time_filter="day", limit=5)
