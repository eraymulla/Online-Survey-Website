from email import message
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, request
from flask_sqlalchemy import SQLAlchemy
import requests


# db and app configurations

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/surveyDb'
db = SQLAlchemy(app)

# Database Table Models

class ParticipantUserModel(db.Model):
    __tablename__ = 'ParticipantUser'
    userId       =   db.Column(db.Integer, primary_key = True)
    name         =   db.Column(db.String(20), nullable=False)
    surname      =   db.Column(db.String(20), nullable=False)
    email        =   db.Column(db.String(40), nullable=False)
    password     =   db.Column(db.String(20), nullable=False)
    permissionId =   db.Column(db.Integer, nullable=False) 
    
    def __init__(self,userId,name,surname,email,password,permissionId):
        self.userId = userId
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.permissionId = permissionId

class AdminUserModel(db.Model):
    __tablename__ = 'AdminUser'
    userId       =   db.Column(db.Integer, primary_key = True)
    name         =   db.Column(db.String(20), nullable=False)
    surname      =   db.Column(db.String(20), nullable=False)
    email        =   db.Column(db.String(40), nullable=False)
    password     =   db.Column(db.String(20), nullable=False)
    permissionId =   db.Column(db.Integer, nullable=False)
    def __init__(self,userId,name,surname,email,password,permissionId):
        self.userId = userId
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.permissionId = permissionId

class UsersModel(db.Model):
    __tablename__ = 'Users'
    userId       =   db.Column(db.Integer, primary_key = True)
    permissionId =   db.Column(db.Integer, nullable=False)
    def __init__(self,userId,permissionId):
        self.userId = userId
        self.permissionId = permissionId

class PermissionModel(db.Model):
    __tablename__ = 'Permissions'
    id           =   db.Column(db.Integer, primary_key = True)
    userId       =   db.Column(db.Integer)
    permission   =   db.Column(db.String(20), nullable=False)
    def __init__(self,id,userId,permission):
        self.id = id
        self.userId = userId
        self.permission = permission


#region Admin Metodları
@app.route('/admin',methods=['GET'])  # tüm admin userları çekmek için get metodu
def getAdmin():
    allAdmins = AdminUserModel.query.all()
    output = []
    for admin in allAdmins:
        tempAdmin = {}
        tempAdmin['userId'] = admin.userId
        tempAdmin['name'] = admin.name
        tempAdmin['surname'] = admin.surname
        tempAdmin['email'] = admin.email
        tempAdmin['password'] = admin.password
        tempAdmin['permissionId'] = admin.permissionId
        output.append(tempAdmin)
    return jsonify(output)

@app.route('/admin',methods=['GET'])  # idye göre admin datası çekme metodu
def getAdminById():
    adminId = request.get_json() 
    checkAdmin = AdminUserModel.query.filter_by(userId = adminId)
    return jsonify(checkAdmin)


#region admin post metodları
@app.route('/adminLogin',methods=['POST'])  # admin kayıt için post metodu
def adminLogin():
    adminData = request.get_json()  #post requestten admin datalarını aldık
    admins = AdminUserModel.query.all()
    newId = 0
    for admin in admins:
        if admin.userId > newId:
            newId = admin.userId  
    newAdmin = AdminUserModel(newId+1,name=adminData['name'],surname=adminData['surname'],email=adminData['email'],password=adminData['password'],permissionId=2)
    db.session.add(newAdmin)
    db.session.commit()
    return newAdmin

@app.route('/adminSignin',methods=['POST'])    # admin giriş kontrol metodu
def adminSignin():
    checkAdmin = request.get_json() 
    print("-------------------")
    print(checkAdmin) 
    print("-------------------")
    allAdmins = AdminUserModel.query.all()
    for admin in allAdmins:
        print(admin.email, admin.password)    # tablodaki bütün admin değerlerinin email ve password bilgileri
    print("-------------------")
    for admin in allAdmins:
        if admin.email == checkAdmin['email'] and admin.password == checkAdmin['password']:
            #abort(201,message="Admin sign in successfully")
            return 'Giriş başarılı',201
    return 'kullanıcı adı ya da şifre yanlış',404
#endregion
#endregion








if __name__ == "__main__":
    app.run(debug=True)