from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, request
from flask_sqlalchemy import SQLAlchemy


#region flask configurations
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/surveyDb'
db = SQLAlchemy(app)
#endregion

#region Database User Table Models
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
#endregion

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

@app.route('/admin/<int:id>',methods=['GET'])  # idye göre admin datası çekme metodu
def getAdminById(id):
    
    checkAdmin = AdminUserModel.query.filter_by(userId = id).first_or_404()
    return checkAdmin.name,201


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
    return "Kullanıcı ekleme işlemi başarılı",201

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

#region Participant Metodları

@app.route('/participant',methods=['GET'])  # tüm participant userları çekmek için get metodu
def getParticipant():
    allParticipants = ParticipantUserModel.query.all()
    output = []
    for admin in allParticipants:
        tempParticipant = {}
        tempParticipant['userId'] = admin.userId
        tempParticipant['name'] = admin.name
        tempParticipant['surname'] = admin.surname
        tempParticipant['email'] = admin.email
        tempParticipant['password'] = admin.password
        tempParticipant['permissionId'] = admin.permissionId
        output.append(tempParticipant)
    return jsonify(output)

@app.route('/participant/<int:id>',methods=['GET'])  # idye göre admin datası çekme metodu
def getParticipantById(id):
    print("------------metoddan gelen id değeri : ",id,"-------------")
    checkParticipant = ParticipantUserModel.query.filter_by(userId = id).first_or_404()
    return checkParticipant.name,201

#region participant post metodları
@app.route('/participantLogin',methods=['POST'])  # admin kayıt için post metodu
def participantLogin():
    participantData = request.get_json()  #post requestten admin datalarını aldık
    participants = ParticipantUserModel.query.all()
    newId = 0
    for participant in participants:
        if participant.userId > newId:
            newId = participant.userId  
    newParticipant = ParticipantUserModel(newId+1,name=participantData['name'],surname=participantData['surname'],email=participantData['email'],password=participantData['password'],permissionId=2)
    db.session.add(newParticipant)
    db.session.commit()
    return "Kullanıcı ekleme işlemi başarılı",201

@app.route('/participantSignin',methods=['POST'])    # admin giriş kontrol metodu
def participantSignin():
    checkParticipant = request.get_json() 
    print("-------------------")
    print(checkParticipant) 
    print("-------------------")
    allParticipants = ParticipantUserModel.query.all()
    for participant in allParticipants:
        print(participant.email, participant.password)    # tablodaki bütün admin değerlerinin email ve password bilgileri
    print("-------------------")
    for participant in allParticipants:
        if participant.email == checkParticipant['email'] and participant.password == checkParticipant['password']:
            #abort(201,message="Admin sign in successfully")
            return 'Giriş başarılı',201
    return 'kullanıcı adı ya da şifre yanlış',404
#endregion
#endregion



#region question database modelleri
class QuestionModel(db.Model):
    __tablename__ = 'Questions'
    questionId       =   db.Column(db.Integer, primary_key = True, )
    question         =   db.Column(db.String(), nullable=False)
    answerType       =   db.Column(db.Integer, nullable=False)
    categoryId       =   db.Column(db.Integer, nullable=True)
    adminId          =   db.Column(db.Integer, nullable=False) 
    
    def __init__(self,questionId,question,answerType,categoryId,adminId):
        self.questionId = questionId
        self.question = question
        self.answerType = answerType
        self.categoryId = categoryId
        self.adminId = adminId

class AnswerModel(db.Model):
    __tablename__ = 'Answers'
    answerId         =   db.Column(db.Integer, primary_key = True)
    questionId       =   db.Column(db.Integer, nullable=False)
    answer           =   db.Column(db.String(), nullable=False)
    answerType       =   db.Column(db.Integer, nullable=False)
    categoryId       =   db.Column(db.Integer, nullable=True)
    adminId          =   db.Column(db.Integer, nullable=False) 
    
    def __init__(self,answerId,questionId,answer,answerType,categoryId,adminId):
        self.answerId = answerId
        self.questionId = questionId
        self.answer = answer
        self.answerType = answerType
        self.categoryId = categoryId
        self.adminId = adminId
#endregion


#region question metodları
@app.route('/addQuestion',methods=['POST'])
def addQuestionAndAnswer():
    questionAndAnswerData = request.get_json()
    print("------------",questionAndAnswerData,"---------------")
    # alınacak datada bulunacak değişkenler :  
    # questionId (AutoIncrement)
    # question(String), 
    # answerType(answerType tablosuna da yazılacak)
    # categoryId (category tablosundan matchlemek için)
    # adminId (hangi adminin yazdığını bilebilmek için)
    # answerId 
    # answer
    questionData = QuestionModel(questionId=questionAndAnswerData['questionId'],question=questionAndAnswerData['question'],answerType=questionAndAnswerData['answerType'],categoryId=questionAndAnswerData['categoryId'],adminId=questionAndAnswerData['adminId'])
    answerData = AnswerModel(answerId=questionAndAnswerData['answerId'],questionId=questionAndAnswerData['questionId'],answer=questionAndAnswerData['answer'], answerType=questionAndAnswerData['answerType'],categoryId=questionAndAnswerData['categoryId'], adminId=questionAndAnswerData['adminId'])
    print(questionData.questionId,questionData.question,"\n",answerData.answerId,answerData.questionId,answerData.answer)
    db.session.add(questionData)
    db.session.commit()
    db.session.add(answerData)
    db.session.commit()
    return "Soru eklendi",201


@app.route('/getQuestion',methods=['GET'])
def getAllQuestionAndAnswers():
    questions = QuestionModel.query.all()
    output = []
    for question in questions:
        tempQuestion = {}
        tempQuestion['questionId'] = question.questionId
        tempQuestion['question'] = question.question
        tempQuestion['answerType'] = question.answerType
        tempQuestion['categoryId'] = question.categoryId
        tempQuestion['adminId'] = question.adminId
        output.append(tempQuestion)
    
    answers = AnswerModel.query.all()
    for answer in answers:
        tempAnswer = {}
        tempAnswer['answerId'] = answer.answerId
        tempAnswer['questionId'] = answer.questionId
        tempAnswer['answer'] = answer.answer
        tempAnswer['categoryId'] = answer.categoryId
        tempAnswer['adminId'] = answer.adminId
        output.append(tempAnswer)
    
    return jsonify(output)

@app.route('/getQuestionById/<int:questionId>',methods=['GET'])   # question id parametresi ile soru ve o soruya ait cevapları döndürür
def getQuestionAndAnswerById(questionId):
    output = []
    question = QuestionModel.query.filter_by(questionId = questionId).first_or_404()
    tempQuestion = {}
    tempQuestion['questionId'] = question.questionId
    tempQuestion['question'] = question.question
    tempQuestion['answerType'] = question.answerType
    tempQuestion['categoryId'] = question.categoryId
    tempQuestion['adminId'] = question.adminId
    output.append(tempQuestion)
    #return jsonify(tempQuestion)
    answer = AnswerModel.query.filter_by(questionId = questionId).first_or_404()
    tempAnswer = {}
    tempAnswer['answerId'] = answer.answerId
    tempAnswer['questionId'] = answer.questionId
    tempAnswer['answer'] = answer.answer
    tempAnswer['categoryId'] = answer.categoryId
    tempAnswer['adminId'] = answer.adminId
    output.append(tempAnswer)
    return jsonify(output)
    
    
    
    
        
    

#endregion


if __name__ == "__main__":
    app.run(debug=True)
