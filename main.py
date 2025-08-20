import email_utils
import gemini_utils
import os
import reddit_utils
import utils
from dotenv import load_dotenv

def main():
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")
    reddit = reddit_utils.create_reddit_instance()
    subreddits = reddit.user.subreddits()

    summaries = []

    for subreddit in subreddits:
        if subreddit.display_name != "announcements":
            top_posts = reddit_utils.get_top_posts(subreddit)

            prompt = utils.create_prompt(subreddit.display_name, top_posts)

            response = gemini_utils.call_gemini_api(prompt, API_KEY)

            summaries.append([subreddit.display_name, response])

    # Create and send message
    email_utils.email(summaries)


if __name__ == "__main__":
    main()

