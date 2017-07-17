from flask import render_template, flash, redirect
from app import app, db
from .forms import SearchForm
from .tweet import Tweet
from .twitter_api_wrapper import TwitterApiWrapper

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
        twit_search = TwitterApiWrapper()
        results = twit_search.all(hashtag, bigSearch = False)
        hashtag = "test"

        return render_template('index.html', hashtag = "test")
