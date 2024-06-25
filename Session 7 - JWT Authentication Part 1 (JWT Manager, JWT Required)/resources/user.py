from flask import request 
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import UserSchema

from models import UserModel
from db import db
from sqlalchemy.exc import SQLAlchemyError

from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, create_refresh_token

from blocklist import BLOCKLIST

blp = Blueprint("users", __name__, description="Operations on users.")

'''
/register   - POST create new user
/user/<id>  - GET     (testing)
/user/<id>  - DELETE  (testing)
/login      - POST


/refresh    - POST
/logout     - POST
'''

@blp.route('/register')
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, acc_info):
        if UserModel.query.filter(
            UserModel.username == acc_info["username"]
        ).first():
            abort(400, message="A user with that username already exists.")
        
        user = UserModel(
            username=acc_info["username"],
            password=pbkdf2_sha256.hash(acc_info["password"])
        )

        db.session.add(user)
        db.session.commit()

        return user

@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, login_cred):
        user = UserModel.query.filter(
            UserModel.username == login_cred["username"]
        ).first()

        if user and pbkdf2_sha256.verify(login_cred["password"], user.password):
            # Create access token
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}
        
        abort(401, message="Invalid credentials.")

@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        # GET JTI
        jti = get_jwt()["jti"]

        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out."} 

@blp.route("/refresh")
class TokenRefresh(MethodView):
    # Only accepts refresh tokens
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt()["sub"]

        # Create a new non-fresh access token
        new_token = create_access_token(identity=current_user, fresh=False)

        return {"access_token": new_token}


@blp.route("/user/<int:user_id>")
class User(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, user_id):
        access_token = get_jwt()
        if access_token["is_admin"] == True:
            user = UserModel.query.get_or_404(user_id)        
            return user
        else:
            abort(400, message="You are not an admin. Please do this request with an admin authorization.")

    @jwt_required()
    def delete(self, user_id):
        access_token = get_jwt()
        if access_token["is_admin"] == True:
            user = UserModel.query.get_or_404(user_id)
            db.session.delete(user)
            db.session.commit()
            return {"message": "User Deleted."}, 200
        else:
            abort(400, message="You are not an admin. Please do this request with an admin authorization.")

