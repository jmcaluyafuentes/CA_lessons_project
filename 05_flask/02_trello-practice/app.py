from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to my first Flask app!</h1>'

@app.errorhandler(404)
def error(e):
    return f'Error: {e}', 404

# if __name__ == '__main__':
#     app.run(debug=True)
