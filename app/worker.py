from app import app, db
from app.models import TwitterAccount, Tweet
from twitter.api import Twitter
from twitter.oauth import OAuth
import praw
from app.utils import create_tweet


# create Reddit session
r = praw.Reddit(app.config['REDDIT_USER_AGENT'])
r.set_oauth_app_info(client_id=app.config['REDDIT_APP_ID'],
                     client_secret=app.config['REDDIT_APP_SECRET'],
                     redirect_uri=app.config['OAUTH_REDIRECT_URI'])
r.refresh_access_information(app.config['OAUTH_REFRESH_TOKEN'])

# for each user, crawl sources, add tweets to database and tweet one
for user in TwitterAccount.query.all():

    for source in user.sources:
        subreddit = r.get_subreddit(source.subreddit)
        for thread in \
                subreddit.get_new(limit=int(app.config['REDDIT_CRAWL_COUNT'])):
            if (thread.score >= source.threshold):
                tweet = Tweet.query\
                    .filter_by(source_id=source.id)\
                    .filter_by(reddit_id=thread.id)\
                    .first()
                if tweet is None:
                    tweet_text = create_tweet(thread.title, thread.permalink)
                    new_tweet = Tweet(
                        reddit_id=thread.id,
                        date_posted=thread.created_utc,
                        tweet=tweet_text,
                        twitter_user_id=user.id,
                        source_id=source.id
                    )
                    db.session.add(new_tweet)

    next_tweet = Tweet.query\
        .filter_by(twitter_user_id=user.id)\
        .filter_by(tweeted=False)\
        .order_by(Tweet.date_posted.asc())\
        .first()

    if next_tweet is not None:

        try:
            t = Twitter(
                auth=OAuth(user.oauth_token,
                           user.oauth_secret,
                           app.config['TWITTER_CONSUMER_KEY'],
                           app.config['TWITTER_CONSUMER_SECRET']
                           )
            )
            tweet_response = t.statuses.update(status=next_tweet.tweet)
            if tweet_response.headers.get('status') == '200 OK':
                next_tweet.tweeted = True
        except:
            continue

    db.session.commit()
