from app import db
from app.models import Tweet
import time


cutoff_dats = 60
now = time.time()
time_60_ago = now - 60 * 60 * 24 * 60

tweets = Tweet.query\
    .filter(Tweet.date_posted < time_60_ago)\
    .all()

for tweet in tweets:
    db.session.delete(tweet)
    db.session.commit()
