from flask import render_template, flash, redirect, request
from application import application, db
from .forms import SearchForm, SimpleForm
from .tweet_collection import TweetCollection
# from .tweet import Tweet

# the polarity value between 0 and 1 that represents "positive sentiment"

POSITIVE = .5

@application.route('/index')

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

@application.route('/', methods=['GET','POST'])
@application.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
         flash('Searching Twitter for #%s' % (form.hashtag.data))
         return search_results(hashtag = form.hashtag.data)
    return render_template('search.html',title = 'Search', form = form)
@application.route('/', methods = ['GET','POST'])
@application.route('/search_results', methods=['GET','POST'])
def search_results(hashtag):
    tweets = TweetCollection(hashtag)

    form = SimpleForm(request.form)


    displayStats = {
        "hashtag": hashtag,
        "num": len(tweets.tweetList),
        "sentimentStats": tweets.by_sentiment(POSITIVE)
        }

    posTweets = [(x.twitter_id, x.text) for x in displayStats["sentimentStats"]["most_pos"]]

    negTweets = [(x.twitter_id, x.text) for x in displayStats["sentimentStats"]["most_neg"]]

    form.displayStats = displayStats
    form.pos.choices = posTweets
    form.neg.choices = negTweets
    return render_template('search_results.html', displayStats=displayStats, title = 'Search', form = form)

    # if form.validate_on_submit():
    #     return render_template('search.html',title = 'Search', form = form)
    # return render_template('search_results.html', title = 'Search', displayStats = displayStats, form = form)

@application.route('/like_minds', methods=['GET','POST'])
def like_minds():
    good_tweets = request.form.getlist('pos',       type=int)

    hashtags = Tweet.query.filter_by(search_term = self.hashtag).

    return render_template('like_minds.html', test = good_tweets)
