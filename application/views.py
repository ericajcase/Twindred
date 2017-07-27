from flask import render_template, flash, redirect, request
from application import application, db
from .forms import SearchForm, SimpleForm, AutoSearch
from .tweet_collection import TweetCollection
import logging
from logging.handlers import RotatingFileHandler
from .tweet import Tweet

# the polarity value between 0 and 1 that represents "positive sentiment"

POSITIVE = .5

@application.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
         flash('Searching Twitter for #%s' % (form.hashtag.data))
         return search_results(hashtag = form.hashtag.data)
    return render_template('search.html',title = 'Search', form = form)

@application.route('/', methods = ['GET','POST'])
@application.route('/search_results', methods=['GET','POST'])
def search_results(hashtag = None ):
    if hashtag == None:
        hashtag = request.form.get("hashtag")
    tweets = TweetCollection(hashtag)
    if len(tweets.tweetList)==0:
         flash('Search yielded no results!  Try a different search')
         return render_template('search.html',title = 'Search', form = form)


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

    return render_template('search_results.html', displayStats=displayStats, title = 'Search', form = form, test = tweets)


@application.route('/like_minds', methods=['GET','POST'])
def like_minds():
    tweet_ids = request.form.getlist('pos', type=int)
    tweet_ids = tweet_ids + (request.form.getlist('neg', type=int))

    form = AutoSearch(request.form)

    tweets = (Tweet.query.filter(Tweet.twitter_id.in_(tweet_ids)).all())

    if len(tweets)==0:
        flash('Search yielded no results!  Try a different search')
        return render_template('search.html',title = 'Search', form = form)

    hashtags = []
    locations = []

    for tweet in tweets:
        hashtags = hashtags + tweet.get_hashtags()
        locations.append(tweet.location)

    return render_template('like_minds.html', hashtags = hashtags, locations = locations, form = form, hashtag = tweets[0].search_term)
