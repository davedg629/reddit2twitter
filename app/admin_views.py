from app import db, models
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView


# Admin constructor
admin = Admin(
    name='reddit2twitter',
    index_view=AdminIndexView()
)

# add admin views
admin.add_view(ModelView(
    models.TwitterAccount,
    db.session,
    name='Twitter Accounts',
    endpoint='twitter_account_model_view'
))
admin.add_view(ModelView(
    models.Source,
    db.session,
    name='Sources',
    endpoint='source_model_view'
))
admin.add_view(ModelView(
    models.Tweet,
    db.session,
    name='Tweets',
    endpoint='tweet_model_view'
))
