def create_prompt(subreddit, posts):  
    prompt = f"In a paragraph or two, summarize these posts about {subreddit} for me: "
    for post in posts:
        prompt += f"{post.title}: {post.selftext}"
    return prompt
