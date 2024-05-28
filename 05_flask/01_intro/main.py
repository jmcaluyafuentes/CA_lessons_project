from flask import Flask, request

app = Flask(__name__)

msg = 'Hello world!'
person = {'name': 'John', 'age': 21}

@app.route('/') # root end point
def home():
    return f'<h3>{msg}</h3>'

@app.route('/spam')
def spam():
    return person, 201

@app.route('/hello/<name>')
def hello(name):
    # name = request.args.get('name')
    # name = 'Mary'
    return {'message': f'Hello, {name}!'}

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return {'result': a + b}
    
# @app.route('/add/<int:a>/<int:b>')
# def add(a, b):
#     try:
#         # num1 = int(request.args.get('a'))
#         # num2 = int(request.args.get('b'))
#         return {'result': a + b}
#     except (ValueError, TypeError):
#         return {'error': 'a and b are required and must be integers'}, 400


@app.errorhandler(Exception)
def value_error(err):
    return {'error': str(err)}, 400

@app.errorhandler(404)
def not_found(err):
    print(err)
    return {'error': str(err)}, 404

app.run(debug=True)
