from flask import render_template, flash, redirect
from app import app, db
from .forms import SearchForm
from .tweet_collection import TweetCollection
# from .tweet import Tweet

# the polarity value between 0 and 1 that represents "positive sentiment"

POSITIVE = .5

@app.route('/')
@app.route('/index')

def index(hashtag):
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
    {
    'author': {'nickname': 'John'},
    'body': 'Beautiful day in Portland!'
    },
    {
    'author': {'nickname': 'Susan'},
    'body': 'The Avengers movie was so cool!'
    }
    ]
    return render_template('index.html',
    title = "Erica's Flask",
    user=user,
    posts = posts)

@app.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
         flash('Searching Twitter for #%s' % (form.hashtag.data))
         return search_results(hashtag = form.hashtag.data)
    return render_template('search.html',title = 'Search', form = form)

def search_results(hashtag):
    tweets = TweetCollection(hashtag)

    displayStats = {
        "hashtag": hashtag,
        "num": len(tweets.tweetList),
        "sentimentStats": tweets.by_sentiment(POSITIVE)
        }

    return render_template('search_results.html', hashtag = displayStats["sentimentStats"])
