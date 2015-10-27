from flask import Flask, render_template
import controllers
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yaleims')
def yaleims():
	scores = controllers.overall()
	return render_template('yaleims/home.html', scores=scores)

@app.route('/habitar')
def habitar():
	return render_template('habitar/index.html')

@app.route('/narwhals')
def narwhals():
	return render_template('narwhals/index.html')

@app.route('/v2')
def v2():
	return render_template('homev2.html')

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/section50')
def section50():
	return render_template('section50.html')

@app.route('/capitalone')
def capitolone():
	posts = controllers.instagram()
	captions = posts['captions']
	likes = posts['likes']
	images = posts['images']
	users = posts['users']
	times = posts['times']
	sentiments = posts['sentiments']
	return render_template('capitalone.html', captions=captions, likes=likes, images=images, users=users, times=times, sentiments=sentiments)

@app.route('/user/<username>')
def hello(username):
	return 'hey %s!' % username

if __name__ == '__main__':
    app.run(debug=True)
