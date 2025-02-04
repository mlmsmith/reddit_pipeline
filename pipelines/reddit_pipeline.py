def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit:None):
    #connecting to Reddit instance
    instance = reddit_connection(CLIENT_ID, SECRET, 'Airscholar agent')
    #extraction
    #transformation
    #loading to csv