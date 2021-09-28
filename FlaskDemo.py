from flask import Flask, render_template, url_for, redirect
from Forms import CreateTweet, SearchForm, DeleteForm

import win32ui
import win32con
import tweepy
import time
from keys import *


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


@app.route("/")
@app.route("/home")
def hello():
	posts = []
	mentions = api.user_timeline()
	for mention in reversed(mentions):
		
		posts.append({
				'author': mention.user.name,
				'title': str(mention.text),
				'date_posted' : str(mention.created_at).split(" ")[0],
				'tweet_id' : mention.id
				})
	return render_template('home.html',posts=posts)

"""
@app.route("/about")
def about():
	return render_template('about.html',title='about')

"""

@app.route("/create", methods=['GET','POST'])
def create():
	form = CreateTweet()

	if form.validate_on_submit():

		tweet=form.tweet.data
		newt = api.update_status(tweet)
		return redirect(url_for('hello'))
    else:
		print

	return render_template('create.html',title='create', form=form)

"""
@app.route("/search", methods=['GET','POST'])
def search():
	form = SearchForm()
	
	if form.validate_on_submit():
		tweetId=form.userId.data
		mentions = api.user_timeline()
		for mention in mentions :
			if(mention.id==tweetId):

		return redirect(url_for('search'))

	return render_template('search.html',title='search', form=form)

"""

@app.route("/delete", methods=['GET','POST'])
def delete():
	form = DeleteForm()
	
	if form.validate_on_submit():
		deleteTweetId=form.deleteTweetId.data
		try:
			delt = api.destroy_status(deleteTweetId) win32ui.MessageBox("Message", "Title")
			return redirect(url_for('hello'))
		except:
			return redirect(url_for('delete'))
		

	return render_template('delete.html',title='delete', form=form)



if __name__ == '__main__':
	app.run(debug=False)


