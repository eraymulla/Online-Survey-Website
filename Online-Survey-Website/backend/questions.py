from requests import request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, request
from main import db,AdminUserModel,ParticipantUserModel,UsersModel,PermissionModel,app

#region database modelleri
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
    answerId         =  db.Column(db.Integer, primary_key = True)
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

#region metodlar
@app.route('/test',methods=['GET'])
def test():
    print('test metoduna girdi')
    return {
        "message" : "questions.py'da ki test metodu"
    }

@app.route('/questions/addQuestion',methods=['POST'])
def addQuestionAndAnswer():
    questionAndAnswerData = request.get_json()
    print("------------",questionAndAnswerData,"---------------")
    # alınacak datada bulunacak değişkenler :  
    #questionId (AutoIncrement)
    # # 
    # question(String), 
    # answerType(answerType tablosuna da yazılacak)
    # categoryId (category tablosundan matchlemek için)
    # adminId (hangi adminin yazdığını bilebilmek için)
    # answer + adminId + answerType + questionId + categoryId(categoryId yazılmayadabilir) Answer tablosuna yazılacak
    questionData = QuestionModel(questionId=questionAndAnswerData['questionId'],question=questionAndAnswerData['question'],answerType=questionAndAnswerData['answerType'],categoryId=questionAndAnswerData['categoryId'],adminId=questionAndAnswerData['adminId'])
    answerData = AnswerModel(answerId=questionAndAnswerData['answerId'],questionId=questionAndAnswerData['questionId'],answer=questionAndAnswerData['answer'], answerType=questionAndAnswerData['answerType'],categoryId=questionAndAnswerData['categoryId'], adminId=questionAndAnswerData['adminId'])
    print(questionData,"\n",answerData)
    return "Soru eklendi",201

#endregion