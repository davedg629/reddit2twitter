from app import db


class TwitterAccount(db.Model):

    __tablename__ = "twitter_accounts"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    oauth_token = db.Column(db.String, nullable=False)
    oauth_secret = db.Column(db.String, nullable=False)

    sources = db.relationship(
        'Source',
        backref='twitter_account',
        lazy='dynamic'
    )

    tweets = db.relationship(
        'Tweet',
        backref='twitter_account',
        lazy='dynamic'
    )

    def __unicode__(self):
        return self.username


class Source(db.Model):

    __tablename__ = "sources"

    id = db.Column(db.Integer, primary_key=True)
    subreddit = db.Column(db.String, nullable=False)
    threshold = db.Column(db.Integer, nullable=False)

    twitter_user_id = db.Column(
        db.Integer,
        db.ForeignKey('twitter_accounts.id'),
        nullable=False
    )

    tweets = db.relationship(
        'Tweet',
        backref='source',
        lazy='dynamic'
    )

    def __unicode__(self):
        return self.subreddit + ' - ' + str(self.twitter_user_id)


class Tweet(db.Model):

    __tablename__ = "tweets"

    id = db.Column(db.Integer, primary_key=True)
    reddit_id = db.Column(db.String, nullable=False)
    date_posted = db.Column(
        db.Integer,
        nullable=False
    )
    tweet = db.Column(db.String, nullable=False)

    twitter_user_id = db.Column(
        db.Integer,
        db.ForeignKey('twitter_accounts.id'),
        nullable=False
    )

    source_id = db.Column(
        db.Integer,
        db.ForeignKey('sources.id'),
        nullable=False
    )

    tweeted = db.Column(db.Boolean, nullable=False, default=False)

    def __unicode__(self):
        return self.tweet + ' - ' + str(self.twitter_user_id)
