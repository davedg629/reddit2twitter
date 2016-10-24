from app import app, db
from flask import request, session
from app.models import TwitterAccount
from twitter.api import Twitter
from twitter.oauth import OAuth
from twitter.oauth_dance import parse_oauth_tokens


# homepage
@app.route("/twitter-login/")
def twitter_login():
    twitter = Twitter(
        auth=OAuth('', '',
                   app.config['TWITTER_CONSUMER_KEY'],
                   app.config['TWITTER_CONSUMER_SECRET']
                   ),
        format='', api_version=None)
    session['oauth_token'], session['oauth_token_secret'] = parse_oauth_tokens(
        twitter.oauth.request_token(
            oauth_callback=app.config['TWITTER_CALLBACK'])
    )
    oauth_url = ('https://api.twitter.com/oauth/authorize?oauth_token=' +
                 session['oauth_token'])
    return '<a href="' + oauth_url + '">Login with Twitter</a>'


# TWITTER AUTHORIZE
@app.route('/twitter-authorize/')
def twitter_authorize():
    twitter = Twitter(
        auth=OAuth(session['oauth_token'], session['oauth_token_secret'],
                   app.config['TWITTER_CONSUMER_KEY'],
                   app.config['TWITTER_CONSUMER_SECRET']
                   ),
        format='', api_version=None)
    oauth_token, oauth_token_secret = parse_oauth_tokens(
        twitter.oauth.access_token(
            oauth_verifier=request.args.get('oauth_verifier'))
    )
    if oauth_token and oauth_token_secret:
        t = Twitter(
            auth=OAuth(oauth_token,
                       oauth_token_secret,
                       app.config['TWITTER_CONSUMER_KEY'],
                       app.config['TWITTER_CONSUMER_SECRET'])
        )
        user_info = t.account.settings()
        user = TwitterAccount.query\
            .filter_by(username=user_info['screen_name'])\
            .first()
        if user:
            user.oauth_token = oauth_token
            user.oauth_secret = oauth_token_secret
            db.session.commit()
            return '@' + user_info['screen_name'] + ' was updated.'
        else:
            new_user = TwitterAccount(
                username=user_info['screen_name'],
                oauth_token=oauth_token,
                oauth_secret=oauth_token_secret
            )
            db.session.add(new_user)
            db.session.commit()
            return '@' + user_info['screen_name'] + ' was added.'
    else:
        return 'Twitter Account was not added.'
