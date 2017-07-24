from flask import render_template, flash, redirect, request
from app import app, db
from .forms import SearchForm, SimpleForm
from .tweet_collection import TweetCollection
# from .tweet import Tweet

# the polarity value between 0 and 1 that represents "positive sentiment"

POSITIVE = .5

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

@app.route('/')
@app.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
         flash('Searching Twitter for #%s' % (form.hashtag.data))
         return search_results(hashtag = form.hashtag.data)
    return render_template('search.html',title = 'Search', form = form)

def search_results(hashtag):
    tweets = TweetCollection(hashtag)

    form = SimpleForm()


    displayStats = {
        "hashtag": hashtag,
        "num": len(tweets.tweetList),
        "sentimentStats": tweets.by_sentiment(POSITIVE)
        }


    posTweets = [(x.twitter_id, x.text) for x in displayStats["sentimentStats"]["most_pos"]]

    negTweets = [(x.twitter_id, x.text) for x in displayStats["sentimentStats"]["most_neg"]]

    print(negTweets)

    form.pos.choices = posTweets
    form.neg.choices = negTweets

    return render_template('search_results.html', title = 'Search', displayStats = displayStats, form = form)

# @app.route('/test')
# def test(info = ""):
#     form = SimpleForm(request.form)
#     form.example.choices
#
#     # if form.validate_on_submit():
#     #      return search_results(hashtag = form.hashtag.data)
#
#     return (render_template('test.html',form=form))
