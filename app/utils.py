from app import app
from ttp import ttp


def create_tweet(title, link):
    app.config['TWITTER_LINK_LEN_HTTPS']
    max_title_len = 139 - int(app.config['TWITTER_LINK_LEN'])
    p = ttp.Parser(include_spans=True)
    result = p.parse(title)
    urlcount = len(result.urls)
    if urlcount > 0:
        urlchars = 0
        for url in result.urls:
            urlchars = urlchars + (url[1][1] - url[1][0])
        max_title_len = max_title_len\
            - (urlcount * int(app.config['TWITTER_LINK_LEN']))\
            + urlchars
    title_len = len(title)
    if title_len > max_title_len:
        title = title[:max_title_len - 1] + u"\u2026"
    return title + ' ' + link
