from flask_jwt_extended import jwt_required, get_jwt_identity # jwt_required is a decorator
from init import db
from models.user import User

# Route decorator - ensure JWT user is an admin
def admin_only(fn):
    @jwt_required() # admin_only requires jwt
    def inner():
        # Ensure the user is an admin
        user_id = get_jwt_identity()
        # Query: Fetch a user based on JWT token subject
        stmt = db.select(User).where(User.id == user_id, User.is_admin)
        # Execute query (scalar)
        user = db.session.scalar(stmt)
        # If (user) return cards else return error
        if user:
            return fn()
        else:
            return {'error': 'You must be an admin to access this resource'}, 403

    return inner