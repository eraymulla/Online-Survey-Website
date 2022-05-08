from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, request
from flask_sqlalchemy import SQLAlchemy
import requests


# db and app configurations

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/surveyDb'
db = SQLAlchemy(app)

#db.create_all()     # use this code line just one times.
# Database Table Models

class ParticipantUserModel(db.Model):
    __tablename__ = 'ParticipantUser'
    userId       =   db.Column(db.Integer, primary_key = True)
    name         =   db.Column(db.String(20), nullable=False)
    surname      =   db.Column(db.String(20), nullable=False)
    email        =   db.Column(db.String(40), nullable=False)
    password     =   db.Column(db.String(20), nullable=False)
    permissionId =   db.Column(db.Integer, nullable=False) 
    
    def __init__(self, userId, name, surname, email, password, permissionId):
        self.userId = userId
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.permissionId = permissionId

class AdminUserModel(db.Model):
    userId       =   db.Column(db.Integer, primary_key = True)
    name         =   db.Column(db.String(20), nullable=False)
    surname      =   db.Column(db.String(20), nullable=False)
    email        =   db.Column(db.String(40), nullable=False)
    password     =   db.Column(db.String(20), nullable=False)
    permissionId =   db.Column(db.Integer, nullable=False)

class UsersModel(db.Model):
    userId       =   db.Column(db.Integer, primary_key = True)
    permissionId =   db.Column(db.Integer, nullable=False)

class PermissionModel(db.Model):
    id           =   db.Column(db.Integer, primary_key = True)
    userId       =   db.Column(db.Integer)
    permission   =   db.Column(db.String(20), nullable=False)



# CRUD Arguments
user_put_args = reqparse.RequestParser()
user_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
user_put_args.add_argument("surname", type=str, help="Name of the views is required", required=True)
user_put_args.add_argument("email", type=str, help="Name of the likes", required=True)
user_put_args.add_argument("password", type=str, help="Name of the views is required", required=True)
user_put_args.add_argument("permissionId", type=int, help="Name of the likes", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("name", type=str, help="Name of the video is required", required=True)
user_update_args.add_argument("surname", type=str, help="Name of the views is required", required=True)
user_update_args.add_argument("email", type=str, help="Name of the likes", required=True)
user_update_args.add_argument("password", type=str, help="Name of the views is required", required=True)
user_update_args.add_argument("permissionId", type=int, help="Name of the likes", required=True)

#----------------

resource_fields = {   # jsona serialize eder.
    'id' : fields.Integer,
    'name' : fields.String,
    'surname' : fields.String,
    'email' : fields.String,
    'password' : fields.String,
    'permissionId' : fields.Integer
}

# Vue da çözülecek

class ParticipantUser(Resource):
    @marshal_with(resource_fields)
    def get(self, user_id):
        result = ParticipantUserModel.query.filter_by(userId=user_id).first()
        if not result:
            abort(404,message="Could Not Find a user with that user id")
        return result
    
    @marshal_with(resource_fields)
    def put(self, user_id):
        args = user_put_args.parse_args()
        result = ParticipantUserModel.query.filter_by(userId=user_id).first()
        if result :
            abort(409, message="User id is taken")
        user = ParticipantUser(userId = user_id, name=args['name'],surname=args['surname'],email=args['email'],password=args['password'],permissionId=args['permissionId'])
        db.session.add(user)
        db.session.commit()
        return user,201


    @marshal_with(resource_fields)
    def post(self):
        user = request.get_json()
        print(user)
        name = user['name']
        surname = user['surname']
        email = user['email']
        password = user['password']
        permissionId = user['permissionId']
        if not user:
            abort(409, message='Parametreler eksik ve ya hatalı')
        admin = ParticipantUserModel(name = name,surname = surname,email = email,password = password,permissionId = permissionId)
        db.session.add(admin)
        db.session.commit()
        return user,201
    



@app.route('/test',method=['GET'])
def test():
    return {
        "test" : "test1"
    }



if __name__ == "__main__":
    app.run(debug=True)