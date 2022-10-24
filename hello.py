from flask import Flask
#import Flask class from flask module

app = Flask(__name__)
#create an instance of the Flask class and give it the variable name 'app'


#create a route usign the @app.route to trigger function based on endpoint
@app.route('/')
def index():
    return 'Hello this is the index route!'

#Run the application -behindthe scenes - command line would do this
#if __name__ == '__main__':
   #app.run()  with Ctrl +c to kill the server

#Add another route
@app.route('/posts')
def posts():
    return 'Posts will be evetually be on this page.'

