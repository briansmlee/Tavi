# Trello power-up
# starting with flask tutorial...

from flask import Flask, request
app = Flask(__name__) 

# route decorator to tell Flask which URL should trigger our function.
# i.e binds a function to a URL
@app.route('/') 
def hello_world():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/user/<username>')
def show_user_profile(username): # passed as keywd arg to fn
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>') # converter
def show_post(post_id):
    return 'Post %d' % post_id

# note trailing slash


@app.route('/login')
def login(): pass

with app.test_request_context():
    # build URL to specific fn
    print url_for('login') # name of fn as first param

@app.route('/login1', methods=['GET', 'POST'])
