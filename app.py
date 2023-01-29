from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/me')
def me_api():
    return {
        "user": "John Doe",
        "location": "the Moon",
        "profile_image": "eagle",
    }


