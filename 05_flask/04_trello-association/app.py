from marshmallow.exceptions import ValidationError
from init import app
from blueprints.cli_bp import db_commands
from blueprints.cards_bp import cards_bp
from blueprints.users_bp import users_bp

app.register_blueprint(db_commands)
app.register_blueprint(cards_bp)
app.register_blueprint(users_bp)

@app.route('/')
def index():
    return 'Hello world'

@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    return {'error': 'Not Found'}

@app.errorhandler(ValidationError)
def invalid_request(err):
    return {'error': vars(err)['messages']}

print(app.url_map)