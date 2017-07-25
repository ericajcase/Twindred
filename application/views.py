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

@application.route('/')
@application.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
         flash('Searching Twitter for #%s' % (form.hashtag.data))
         return search_results(hashtag = form.hashtag.data)
    return render_template('search.html',title = 'Search', form = form)

@application.route('/search_results', methods=['GET','POST'])
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

    form.pos.choices = posTweets
    form.neg.choices = negTweets

    render_template('search_results.html', title = 'Search', displayStats = displayStats, form = form)

    if form.validate_on_submit():
        return render_template('search.html',title = 'Search', form = form)
    return render_template('search.html',title = 'Search', form = form)




@application.route('/test', methods=['GET','POST'])
def test(hashtag):
    tweets = TweetCollection(hashtag)

    form = SimpleForm()


    displayStats = {
        "hashtag": hashtag,
        "num": len(tweets.tweetList),
        "sentimentStats": tweets.by_sentiment(POSITIVE)
        }


    posTweets = [(x.twitter_id, x.text) for x in displayStats["sentimentStats"]["most_pos"]]

    negTweets = [(x.twitter_id, x.text) for x in displayStats["sentimentStats"]["most_neg"]]

    form.pos.choices = posTweets
    form.neg.choices = negTweets

    return render_template('search_results.html', title = 'Search', displayStats = displayStats, form = form)
