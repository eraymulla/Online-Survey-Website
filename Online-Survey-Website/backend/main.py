import re
from secrets import choice
from flask import Flask, jsonify,Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from sqlalchemy.sql import text
#from users import users

#import questions  
from flask_mail import Mail,Message
from sqlalchemy import JSON



#region flask configurations
app = Flask(__name__)


#app.register_blueprint(users, url_prefix="")


#app.register_blueprint(questions.questions, url_prefix="")
mail = Mail(app)
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/surveyDb'
db = SQLAlchemy(app)

CORS(app,resources={r"/*":{'origins':"*"}})



#endregion
@app.route("/mailSend",methods=['GET'])
def index():

    msg = Message("Deneme mail",
                  sender="eraymulla0@gmail.com",
                  recipients=["nezihcan.turgut@gmail.com"])

    mail.send(msg)
#region Database User Table Models

class ParticipantUserModel(db.Model):
    __tablename__ = 'ParticipantUser'
    userId       =   db.Column(db.Integer, primary_key = True, autoincrement=True)
    name         =   db.Column(db.String(20), nullable=False)
    surname      =   db.Column(db.String(20), nullable=False)
    email        =   db.Column(db.String(40), nullable=False)
    phone        =   db.Column(db.String(20),nullable=False)
    password     =   db.Column(db.String(20), nullable=False)
    permissionId =   db.Column(db.Integer, nullable=False) 
    studentOrEmployee = db.Column(db.Integer, nullable=False)  # 1 değeri öğrenci 2 değeri çalışanı temsil eder
    def __init__(self,name,surname,email,phone,password,permissionId,studentOrEmployee):
        #self.userId = userId
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.password = password
        self.permissionId = permissionId
        self.studentOrEmployee = studentOrEmployee

class AdminUserModel(db.Model):
    __tablename__ = 'AdminUser'
    userId       =   db.Column(db.Integer, primary_key = True, autoincrement=True)
    name         =   db.Column(db.String(20), nullable=False)
    surname      =   db.Column(db.String(20), nullable=False)
    email        =   db.Column(db.String(40), nullable=False)
    phone        =   db.Column(db.String(20),nullable=False)
    password     =   db.Column(db.String(20), nullable=False)
    permissionId =   db.Column(db.Integer, nullable=False)  # 2 değeri admin olduğunu belirtir
    studentOrEmployee = db.Column(db.Integer, nullable=False)  # 1 değeri öğrenci 2 değeri çalışanı temsil eder
    
    def __init__(self,name,surname,email,phone,password,permissionId,studentOrEmployee):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.password = password
        self.permissionId = permissionId
        self.studentOrEmployee = studentOrEmployee

# admin kullanıcı bir öğrenci ya da bir çalışan olabilir bu yüzden tablolarda permissionId de tutulmaktadır.

#region student info tabloları 
class StudentUserInfoModel(db.Model):
    __tablename__ = 'StudentUserInfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId       =   db.Column(db.Integer, nullable = False)
    permissionId =   db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    educationStatus = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(50), nullable=True) # üniversite ise bölümü
    year = db.Column(db.String(10), nullable=True) # üniversite kaçıncı sınıf olduğu bilgisini tutar

    def __init__(self,userId,permissionId,age,educationStatus,department,year):
        self.userId = userId
        self.permissionId = permissionId
        self.age = age
        self.educationStatus = educationStatus
        self.department = department
        self.year = year

class EducationStatusModel(db.Model):  # NORMALİZASYON TABLOSU (ortaokul, lise, üniversite değelerini tutar)
    __tablename__ = 'EducationStatus'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    educationStatus = db.Column(db.String(20), nullable=False)
    educationStatusTitle = db.Column(db.String(30),nullable=False)
    def __init__(self,educationStatus,educationStatusTitle):
        self.educationStatus = educationStatus
        self.educationStatusTitle = educationStatusTitle
#endregion

#region employee info tabloları
class EmployeeUserInfoModel(db.Model):
    __tablename__ = 'EmployeeUserInfo'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    userId       =   db.Column(db.Integer, nullable=False)
    permissionId =   db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Integer, nullable=True)  # kullanıcılara açılacak anketlerde maaş aralığına göre kullanıcı seçebilmek için ZORUNLU DEĞİL
    experience = db.Column(db.Integer, nullable=False) # kullanıcının kaç yıllık deneyimi olduğunu tutar ZORUNLU
    
    def __init__(self,userId,permissionId,age,salary,experience):
        self.userId = userId
        self.permissionId = permissionId
        self.age = age
        self.salary = salary
        self.experience = experience

class PermissionModel(db.Model):  # NORMALİZASYON TABLOSU
    __tablename__ = 'Permissions'
    id           =   db.Column(db.Integer, primary_key = True, autoincrement=True)
    userId       =   db.Column(db.Integer)
    permission   =   db.Column(db.String(20), nullable=False)
    def __init__(self,userId,permission):
        self.userId = userId
        self.permission = permission
#endregion
#endregion

#region Database Survey Table Models
#class SurveyModel(db.Model):

#endregion

#region  PARTICIPANT VE ADMIN ORTAK METODLARI


@app.route('/Login',methods=['POST'])    # participant ve admin ortak giriş kontrol metodu
def Login():
    checkUser = request.get_json() 
    print("-------------------")
    print(checkUser) 
    print("-------------------")
    allParticipants = ParticipantUserModel.query.all()
    allSurveyParticipants = SurveyParticipantModel.query.all()
    allSurvey = SurveyModel.query.all()
    userPermissionId = 0
    for participant in allParticipants:
        if participant.email == checkUser['email'] and participant.password == checkUser['password']:
            userPermissionId = participant.permissionId
            message = "Katılımcı Girişi Başarılı"
            allSurvey = SurveyModel.query.all()
            dataDict = {"loginCheck" : True, "surveyDatas" : [] , "message":message, "userPermissionId": userPermissionId,"email": participant.email, "name":participant.name, "surname":participant.surname, "phone":participant.phone}
            for surveyParticipant in allSurveyParticipants:
                if participant.userId == surveyParticipant.participantId:
                    for survey in allSurvey:
                        if survey.surveyId == surveyParticipant.surveyId:
                            surveyDataDict = {"surveyId" : survey.surveyId, "surveyName" : survey.surveyName, "surveyDescription" : survey.surveyDescription}
                            dataDict["surveyDatas"].append(surveyDataDict)
            dataJSON = json.dumps(dataDict)
            print(dataJSON)
            return dataDict,201
        #else:
            #userPermissionId = -1
    #if userPermissionId == -1:
    allAdmins = AdminUserModel.query.all()
    adminCheck = False
    for admin in allAdmins:
        if admin.email == checkUser['email'] and admin.password == checkUser['password']:
            adminCheck = True
            userPermissionId = admin.permissionId
            allSurvey = SurveyModel.query.all()
            surveyData = {}
            message = "Admin Girişi Başarılı"
            dataDict = {"loginCheck" : True,"surveyData" : [], "message":message, "userPermissionId": userPermissionId,"email": admin.email, "name":admin.name, "surname":admin.surname, "phone":admin.phone}
            for surv in allSurvey:
                if surv.adminId == admin.userId:
                    surveyData = {
                    "surveyId" : surv.surveyId,
                    "surveyName" : surv.surveyName,
                    "surveyDescription" : surv.surveyDescription 
                    }
                dataDict["surveyData"].append(surveyData)
                print("********SurveyData",surveyData)      
                surveyData = {}
            #for survey in allSurvey:
                #if survey.adminId == admin.userId:
                    #surveyData.pop(survey)
    if adminCheck == True:
        print(surveyData)
        #dataJSON = json.dumps(dataDict)
        #print(dataJSON)
        return dataDict,201
    message = 'kullanıcı emaili ya da şifre yanlış'
    dataDict = {"loginCheck" : True, "message":message}
    dataJSON = json.dumps(dataDict)
    return dataJSON,201

# admine ve participant kayıt olma metodu
@app.route('/Signup', methods=['POST'])  # ortak kayıt olma metodu
def Signup():
    data = request.get_json()
    print(data["name"],data["surname"],data["email"],data["phone"],data["password"],data["permissionId"],data["studentOrEmployee"])
    admins = AdminUserModel.query.all()
    participants = ParticipantUserModel.query.all()
    newId = -1
    if data['permissionId'] == "2":
        for admin in admins:
            if admin.email == data['email']:
                if admin.phone == data['phone']:
                    return "Bu telefon numarası zaten kayıtlı",200
                return "Bu email zaten kayıtlı",200
        newAdmin = AdminUserModel(name=data['name'],surname=data['surname'],email=data['email'],phone=data['phone'],password=data['password'],permissionId=2,studentOrEmployee=data['studentOrEmployee'])
        db.session.add(newAdmin)
        db.session.commit()
        dataDict = {"message":"Adminin diğer bilgileri alınabilir","check": True,"userId": newAdmin.userId}
        dataJson = json.dumps(dataDict)
        return dataJson,201
    if data['permissionId'] == "1":
        for participant in participants:
            if participant.email == data['email']:
                if participant.phone == data['phone']:
                    return "Bu telefon numarası zaten kayıtlı",200
                return "Bu email zaten kayıtlı",200
        newParticipant = ParticipantUserModel(name=data['name'],surname=data['surname'],email=data['email'],phone=data['phone'],password=data['password'],permissionId=1,studentOrEmployee=data['studentOrEmployee'])
        db.session.add(newParticipant)
        db.session.commit()
        dataDict = {"message":"Katılımcının diğer bilgileri alınabilir","check": True, "userId": newParticipant.userId}
        dataJson = json.dumps(dataDict)
        return dataJson,201
    return "kullanıcı ekleme başarısız",202
    

@app.route('/addInfo',methods=['POST'])
def addInfo():
    data = request.get_json()
    #
    # Kullanıcın email ve phone nosuna göre idsini al #
    print(data['permissionId'])
    if data['studentOrEmployee'] == 1:  # 1 değeri öğrenci olduğunu belirtir
        studentInfo = StudentUserInfoModel(userId=data['userId'],permissionId=data['permissionId'],age=data['age'],educationStatus=data['educationStatus'],department=data['department'],year=data['grade'])
        db.session.add(studentInfo)
        db.session.commit()
        return "Öğrenci user ekleme işlemi başarıyla tamamlandı",201
    elif data['studentOrEmployee'] == 2: # 2 değeri çalışan olduğunu belirtir
        employeeInfo = EmployeeUserInfoModel(userId=data['userId'],permissionId=data['permissionId'],age=data['age'],salary=data['salary'],experience=data['experience'])
        db.session.add(employeeInfo)
        db.session.commit()
        return "Çalışan user ekleme işlemi başarıyla tamamlandı",201
    else:
        return "user ekleme işlemi başarısız",200


@app.route('/verifyEmail', methods=['POST'])
def verifyEmail():
    data = request.get_json()
    isEmailExist = 0
    participantEmails = ParticipantUserModel.query.all()
    adminEmails = AdminUserModel.query.all()
    dataDict = {}

    for email in adminEmails:
        if email.email == data['email']:
            isEmailExist = 1

            dataDict = {"isVerifyEmail" : isEmailExist, "email": email.email, "name":email.name, "surname":email.surname, "phone":email.phone}
            dataJSON = json.dumps(dataDict)
            print(dataJSON)
            return dataJSON,201
        else:
            isEmailExist = 0
    if isEmailExist != 1:
        for email in participantEmails:
            if email.email == data['email']:
                isEmailExist = 1
                dataDict = {"isVerifyEmail" : True, "email": email.email, "name":email.name, "surname":email.surname, "phone":email.phone}
                dataJSON = json.dumps(dataDict)
                print(dataJSON)
                return dataJSON,201
            else:
                dataDict = {"isVerifyEmail" : False, "message": "kayıt bulunamadı."}
                dataJSON = json.dumps(dataDict)
                return dataJSON,202

@app.route('/changePassword',methods=['POST'])
def changePassword():
    data = request.get_json()
    participantEmails = ParticipantUserModel.query.all()
    adminEmails = AdminUserModel.query.all()
    for pEmail in participantEmails:
        if data['email'] == pEmail.email:
            pEmail.password = data['newPassword']
            db.session.add(pEmail)
            db.session.commit()
            dataDict = {"isMatchedPassword" : True}
            dataJSON = json.dumps(dataDict)
            return dataJSON,201
    for aEmail in adminEmails:
        if data['email'] == aEmail.email:
            aEmail.password = data['newPassword']
            db.session.add(aEmail)
            db.session.commit()
            dataDict = {"isMatchedPassword" : True}
            dataJSON = json.dumps(dataDict)
            return dataJSON,201
    return "Şifre değiştirilemedi.",202
    
    

#endregion
#-------------------------------------------------------- QUESTION ANSWER SECTION

#region question-answer-choice ve survey database modelleri
class QuestionModel(db.Model):
    __tablename__ = 'Questions'
    questionId       =   db.Column(db.Integer, primary_key = True, autoincrement=True )
    question         =   db.Column(db.String(), nullable=False)
    answerType       =   db.Column(db.Integer, nullable=False)
    categoryId       =   db.Column(db.Integer, nullable=True) # kullanılmayacak
    adminId          =   db.Column(db.Integer, nullable=False) 
    
    def __init__(self,question,answerType,categoryId,adminId):
        self.question = question
        self.answerType = answerType
        self.categoryId = categoryId
        self.adminId = adminId

#region Survey tabloları
class SurveyModel(db.Model):  # Anketlere ait spesifik bilgiler bu tabloda tutulur
    __tablename__ = 'Survey'
    surveyId  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surveyName = db.Column(db.String(), nullable=False)
    surveyDescription = db.Column(db.String(), nullable=False)
    adminId = db.Column(db.Integer, nullable=False)
    def __init__(self,surveyName,surveyDescription,adminId):
        self.surveyName = surveyName
        self.surveyDescription = surveyDescription
        self.adminId = adminId


class SurveyQuestionsModel(db.Model): # Anket idsi ile soru idleri ortak kullanılarak ankete ait sorular tutulacak
    __tablename__ = 'SurveyQuestions' 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surveyId = db.Column(db.Integer, nullable=False)
    questionId = db.Column(db.Integer, nullable=False)
    adminId = db.Column(db.Integer, nullable=False)

    def __init__(self,surveyId,questionId,adminId):
        self.surveyId=surveyId
        self.questionId=questionId
        self.adminId=adminId

class SurveyParticipantModel(db.Model): # Anket idsi ile soru idleri ortak kullanılarak ankete ait sorular tutulacak
    __tablename__ = 'SurveyParticipant' 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surveyId = db.Column(db.Integer, nullable=False)
    participantId = db.Column(db.Integer, nullable=False)
    adminId = db.Column(db.Integer, nullable=False)
    def __init__(self,surveyId,participantId,adminId):
        self.surveyId=surveyId
        self.participantId=participantId
        self.adminId=adminId
#endregion

class AnswerModel(db.Model):
    __tablename__ = 'Answers'
    answerId         =   db.Column(db.Integer, primary_key = True, autoincrement=True)
    questionId       =   db.Column(db.Integer, nullable=False)
    answers           =   db.Column(db.String(), nullable=True)  # soru açık uçlu değilse diğer tablolarda tutulacağı için nullable = true fakat soru çoktan seçmeliyse null değer alamaz!
    answerType       =   db.Column(db.Integer, nullable=False)   # 1 değeri çoktan seçmeli , 2 değeri yes-no , 3 değeri açık uçlu
    categoryId       =   db.Column(db.Integer, nullable=True)
    adminId          =   db.Column(db.Integer, nullable=False) 
    surveyId         =   db.Column(db.Integer, nullable=False)
    
    def __init__(self,questionId,answers,answerType,categoryId,adminId,surveyId):
        self.questionId = questionId
        self.answers = answers
        self.answerType = answerType
        self.categoryId = categoryId
        self.adminId = adminId
        self.surveyId = surveyId

class AnswerTypeModel(db.Model):
    __tablename__ = 'AnswerTypes'
    id         =   db.Column(db.Integer, primary_key = True, autoincrement=True)
    answerType = db.Column(db.String(10), nullable=False)  #sorunun çoktan seçmeli, yes-no, açık uçlu bilgilerinin normalizasyon tablosu  - 1 çoktan seçmeli , 2 yes-no , 3 açık uçlu

    def __init__(self,answerType):
        self.answerType = answerType


class CloseEndedAnswerModel(db.Model): # Şıklı sorular için bütün şıkların tutulduğu tablo
    __tablename__ = 'AnswersOfQuestion'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answerId =   db.Column(db.Integer, nullable=False)
    questionId = db.Column(db.Integer, nullable=False)
    optionId = db.Column(db.Integer, nullable=False) # a şıkkı b şıkkı bilgisi
    answer = db.Column(db.String(), nullable=False) # seçilen şıkka ait cevap

    def __init__(self,answerId,questionId,optionId,answer):
        self.answerId = answerId
        self.questionId = questionId
        self.optionId = optionId
        self.answer = answer


class OptionModel(db.Model): # Şıkların tutulduğu normalizasyon tablosu ( a, b, c, d, e şıkları ve ya 1, 2, 3, 4, 5 şeklinde şıklar tutulacak ve AnswersOfQuestions tablosunda idlerine göre kullanılacak)
    __tablename__ = 'Options'
    optionId =   db.Column(db.Integer, primary_key=True, autoincrement=True)
    option =     db.Column(db.String(), nullable=False) # a şıkkı b şıkkı bilgisi

    def __init__(self,option):
        self.option = option


                            # kullanıcının verdiği cevaplar "choice", soruya ait bütün şıkların her biri "answer" olarak adlandırılmıştır.
                            # multiplechoice için her bir şıkların ayrı ayrı tutulduğu bir şıklar tablosu olacak multipleChoiceId ve questionId ile sorunun şıkları çekilecek
  

class ChoiceModel(db.Model):  # kullanıcının verdiği cevaplar cevap şekline göre aşağıda ki üç tabloda tutulacak
    __tablename__ = 'Choices'
    id =   db.Column(db.Integer, primary_key=True, autoincrement=True)
    questionId = db.Column(db.Integer, nullable=False)  # cevabın hangi soruya ait olduğunun bilgisini tutacak
    participantId = db.Column(db.Integer, nullable=False) # cevabın hangi katılımcıya ait olduğu bilgisini tutacak
    answerTypeId = db.Column(db.Integer, nullable=False)  # answerTypeId ile cevabın hangi tabloya yazılacağı seçilecek

    def __init__(self,questionId,participantId,answerTypeId):
        self.questionId = questionId
        self.participantId = participantId
        self.answerTypeId = answerTypeId    #  1 çoktan seçmeli , 2 yes-no , 3 açık uçlu

class YesNoChoiceModel(db.Model):   # kullanıcının evet hayır soru cevapları
    __tablename__ = 'YesNoChoices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    questionId = db.Column(db.Integer, nullable=False)  # cevabın hangi soruya ait olduğunun bilgisini tutacak
    participantId = db.Column(db.Integer, nullable=False) # cevabın hangi katılımcıya ait olduğu bilgisini tutacak
    choice  = db.Column(db.Boolean, nullable = False)   # evetse 1 hayırsa 0

    def __init__(self,questionId,participantId,choice):
        self.questionId = questionId
        self.participantId = participantId
        self.choice = choice

class OpenEndedChoiceModel(db.Model):  # kullanıcının açık uçlu soru cevapları
    __tablename__ = 'OpenEndedAnswers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    questionId = db.Column(db.Integer, nullable=False)  # cevabın hangi soruya ait olduğunun bilgisini tutacak
    participantId = db.Column(db.Integer, nullable=False) # cevabın hangi katılımcıya ait olduğu bilgisini tutacak
    choice  = db.Column(db.String(400), nullable = False)   # kullanıcının açık uçlu soru cevabının tutulacağı kolon

    def __init__(self,questionId,participantId,choice):
        self.questionId = questionId
        self.participantId = participantId
        self.choice = choice


class CloseEndedChoiceModel(db.Model): # kullanıcının çok şıklı sorulara verdiği cevapların tutulduğu tablo
    __tablename__ = 'CloseEndedChoices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    questionId = db.Column(db.Integer, nullable=False)  # cevabın hangi soruya ait olduğunun bilgisini tutacak
    participantId = db.Column(db.Integer, nullable=False) # cevabın hangi katılımcıya ait olduğu bilgisini tutacak
    choice  = db.Column(db.Integer, nullable = False)   # kullanıcının şıklı sorulara vereceği cevap tutulacak (optionId ile hangi şık olduğunu tutacak)

    def __init__(self,questionId,participantId,choice):
        self.questionId = questionId
        self.participantId = participantId
        self.choice = choice

#endregion


#region question metodları
@app.route('/addQuestion',methods=['POST'])  #soru ekleme post metodu KOMPLE DEĞİŞECEK
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

@app.route("/getParticipants", methods=["GET"])
def getParticipants():
    respDatas = ParticipantUserModel.query.all()
    participantList = {"data" : []}
    for respData in respDatas:
        data = {
        "participantId" : respData.userId,
        "name" : respData.name,
        "surname" : respData.surname,
        "email" : respData.email,
        "phone" : respData.phone
        }
        participantList["data"].append(data)
    return participantList,201
    
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
    


@app.route('/addSurvey',methods=['POST'])
def addSurvey():
    data = request.get_json()
    survey = SurveyModel(surveyName=data['surveyName'],surveyDescription=data['surveyDescription'],adminId=data['adminId'])
    db.session.add(survey)
    db.session.commit()
    dataDict = {"message": "Anket eklendi","surveyId":survey["surveyId"]}
    dataJSON = json.dumps(dataDict)
    return dataJSON,201

# Sadece katılımcıları ekleme kısmı yapılmadı.
@app.route('/addSurveyQuestions', methods=['POST']) # gelen soru dataları question, cevap dataları answers ve anket dataları survey tablosuna doldurulacak 
def addSurveyQuestion():
    data = request.get_json()
    questions = data["questions"]
    answers = data["answers"]
    print("questions : ",questions)
    survey = SurveyModel(surveyName=data["surveyName"],surveyDescription=data["surveyDescription"],adminId=data["adminId"])
    
    db.session.add(survey)
    db.session.commit()
    newSurvey = db.session.query(SurveyModel).from_statement(text("""SELECT "surveyId" FROM "public"."Survey" ORDER BY "surveyId" DESC LIMIT 1;""")).all()
    lastSurveyId = newSurvey[0].surveyId # son eklenen surveyId
    
    #ankete eklenen katılımcılar döngü içerisinde eklenecek
    #surveyParticipant = SurveyParticipantModel(surveyId=lastSurveyId,participantId=data["participantId"],adminId=data["adminId"])    
    for question in questions:
        surveyQuestions = SurveyQuestionsModel(surveyId=lastSurveyId,questionId=question["questionId"],adminId=data['adminId'])
        surveyQuestionData = QuestionModel(question=question["question"],answerType=question["answerType"],categoryId=question["categoryId"],adminId=data["adminId"])
        if question["answerType"] != 1:
            for answer in answers:
                if question["questionId"] == answer["questionId"]:
                    answerM = AnswerModel(questionId=question["questionId"],answers=answers[0]["answers"],answerType=question["answerType"],categoryId=1,adminId=data["adminId"],surveyId=lastSurveyId)
                    db.session.add(answerM)
                    db.session.commit()
        elif question["answerType"] == 1:
            for answer in answers: # 1 değeri çoktan seçmeli
                if question["questionId"] == answer["questionId"]:
                    answerM = AnswerModel(questionId=question["questionId"],answers=answer["answers"],answerType=question["answerType"],adminId=data["adminId"],categoryId=question["categoryId"],surveyId=lastSurveyId)
                    db.session.add(answerM)
                    db.session.commit()
                    newAnswerId = db.session.query(AnswerModel).from_statement(text("""SELECT "answerId" FROM "public"."Answers" ORDER BY "answerId" DESC LIMIT 1;""")).all()
                    lastAnswerId = newAnswerId[0].surveyId # son eklenen surveyId
                    print("son eklenen answer id : ",lastAnswerId)
                    closeEnded = CloseEndedAnswerModel(answerId=lastAnswerId,questionId=question["questionId"],optionId=answer["optionId"],answer=answer["answers"])
                    print("***CloseEnded End")
                    db.session.add(closeEnded)
                    db.session.commit()
    db.session.add(surveyQuestions)
    #db.session.add(surveyParticipant)
    db.session.add(surveyQuestionData)
    db.session.commit()
    print(data)
    print("***return data")
    respData = {"errorCheck" : True}
    return respData,201

@app.route('/getSurveyAdmin', methods=['POST'])
def getSurveyAdmin():
    data = request.get_json()
    surveys = SurveyModel.query.all()
    surveyDataIds = []
    for survey in surveys:
        if survey.adminId == data["adminId"]:
            surveyDataIds.append(survey.surveyId)
    surveyQuestions = SurveyQuestionsModel.query.all()
    questionIds = []
    for survQuestion in surveyQuestions:
        for survAdminId in surveyDataIds:
            if survQuestion.adminId == survAdminId:
                questionIds.append(survQuestion.questionId)
    questions = QuestionModel.query.all()
    questionDataDict = {"data" : []}
    for question in questions:
        for quest in questionIds:
            if question.questionId == quest:
                questionDataDict["data"].append(question.question)
    return questionDataDict,201

@app.route('/getSurveyParticipant', methods=['POST'])
def getSurveyParticipant():
    data = request.get_json()
    particiEmails = ParticipantUserModel.query.all()
    uniqParticiId = 0
    for particiEmail in particiEmails:
        if particiEmail.email == data["email"]:
            uniqParticiId = particiEmail.email
    surveys = SurveyParticipantModel.query.all()
    surveyDataIds = []
    for survey in surveys:
        if survey.participantId == uniqParticiId:
            surveyDataIds.append(survey.surveyId)
    surveyQuestions = SurveyQuestionsModel.query.all()
    questionIds = []
    for survQuestion in surveyQuestions:
        for survParticipantId in surveyDataIds:
            if survQuestion.surveyId == survParticipantId:
                questionIds.append(survQuestion.questionId)
    questions = QuestionModel.query.all()
    questionDataDict = {"data" : []}
    for question in questions:
        for quest in questionIds:
            if question.questionId == quest:
                questionDataDict["data"].append(question.question)
    return questionDataDict,201

@app.route('/addSurveyParticipants', methods=['POST']) # tamamlandı
def addSurveyParticipants():
    data = request.get_json()
    print(data)
    print("----------------------------------------------------")
    participants = data['participants']
    print(participants)
    print("-------------------------------")
    print(participants[0])
    
    for participant in participants:
        print(participant['participantId'])
        reqData = SurveyParticipantModel(surveyId=data['surveyId'],participantId=participant['participantId'],adminId=data['adminId'])
        db.session.add(reqData)
        db.session.commit()
        dataDict = {"message": "anket seçili katılımcılara atandı."}
        dataJSON = json.dumps(dataDict)
    return dataJSON,201

@app.route('/addChoices', methods=['POST'])
def addChoices():
    data = request.get_json()
    print(data)
    print("-----------")
    print(data['choiceIds'])
    choices = data['choices']
    for choice in choices:
        choiceModel = ChoiceModel(questionId=choice['questionId'],participantId=data['participantId'],answerTypeId=choice['answerTypeId'])
        db.session.add(choiceModel)
        db.session.commit()
        if choice['answerTypeId'] == 3:  # 3 çoktan seçmeli
            openEndedModel = OpenEndedChoiceModel(questionId=choice['questionId'],participantId=data['participantId'],choice=choice['choice'])
            db.session.add(openEndedModel)
            db.session.commit()
        elif choice['answerTypeId'] == 2: # 2 yes no
            yesNoModel = YesNoChoiceModel(questionId=choice['questionId'],participantId=data['participantId'],choice=choice['choice'])
            db.session.add(yesNoModel)
            db.session.commit()
        elif choice['answerTypeId'] == 1: # 1 açık uçlu
            closeEndedModel = CloseEndedChoiceModel(questionId=choice['questionId'],participantId=data['participantId'],choice=choice['choice'])
            db.session.add(closeEndedModel)
            db.session.commit()

    dataDict = {"message":"Katılımcının cevapları kaydedildi.", "check" : True}
    dataJSON = json.dumps(dataDict)
    return dataJSON,201
#endregion

#--------------------------------------------------------------------------------



if __name__ == "__main__":
    app.run(debug=True)