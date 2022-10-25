from flask import render_template
from hello import app

# Create routes for our app
@app.route('/')
def index():
    user_info = {
        'username': 'sbabu',
        'email': 'loudnclear@gyoke.com'
    }
    food = ['fries', 'bananasplit', 'warheads', 'greeneggs', 'ham', 'babycarrots', 'liver']
    return render_template('index.html', user=user_info, food=food)


@app.route('/posts')
def posts():
    return 'Hi this is Posts!'