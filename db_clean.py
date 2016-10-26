from app import db
from app.models import Tweet


tweets = Tweet.query\
    .filter_by(tweeted=False)\
    .filter(Tweet.date_posted < 1476876302)\
    .all()

for tweet in tweets:
    tweet.tweeted = True
    db.session.commit()
