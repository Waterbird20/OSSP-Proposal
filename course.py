#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Database URL :  https://rpyy83l3r1.execute-api.ap-northeast-2.amazonaws.com/dev
Created on Fri Apr 29 13:33:24 2022
@author: hsherlcok
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from flask import Flask
from flask import request
from flask import jsonify
from werkzeug.serving import WSGIRequestHandler
import json

USER = "postgres"
PW = "a123123!"
URL = "final-db.ckwpjjg8aiyn.ap-northeast-2.rds.amazonaws.com"
PORT = "5432"
DB = "postgres"

# This line is for solving flask's CORS error
# You need 'pip install flask_cors' to use flask_cors
from flask_cors import CORS
from werkzeug.serving import WSGIRequestHandler

WSGIRequestHandler.protocol_version = "HTTP/1.1"

app = Flask(__name__)

# This line is for solving flask's CORS error
CORS(app)

engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(USER, PW, URL, PORT, DB))
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
db_session_User = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
db_session_Lecture = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class course(Base):
    __tablename__ = 'courses'
    course_id = Column(String(20), primary_key=True)
    course_name = Column(String(20), unique=True)
    professor = Column(String(20), unique=False)
    tutor = Column(String(20), unique=False)
    tutee = Column(String(100), unique=False)
    motivation = Column(String(500), unique=False)
    syllabus = Column(String(500), unique=False)
    schedule = Column(String(500), unique=False)

    def __init__(self, course_id=None, course_name=None, professor=None, tutor=None, tutee=None, motivation=None, syllabus=None, schedule=None):
        self.course_id = course_id
        self.course_name = course_name
        self.professor = professor
        self.tutor = tutor
        self.tutee = tutee
        self.motivation = motivation
        self.syllabus = syllabus
        self.schedule = schedule

    def __repr__(self):
        return f'<course {self.course_id!r}>'

UserBase = declarative_base()
UserBase.query = db_session_User.query_property()

class User(UserBase):
    __tablename__ = "Users"
    user_id = Column(String(50), primary_key = True)
    name = Column(String(50), unique = False)

    def __init__(self, user_id=None, name=None):
        self.user_id=user_id
        self.name=name

    def __repr__(self):
        return f'<User {self.user_id!r}'

lectureBase = declarative_base()
lectureBase.query = db_session_Lecture.query_property()

class Lecture(lectureBase):
    __tablename__ = "lectures"
    lecture_id = Column(String(50), primary_key =True)
    college = Column(String(50), unique = False)
    department = Column(String(50), unique = False)
    name = Column(String(50), unique = False)
    professor = Column(String(50), unique = False)

    def __init__(self, lecture_id=None, college=None, department=None, name=None, professor=None):
        self.lecture_id = lecture_id
        self.college = college
        self.department = department
        self.name = name
        self.professor = professor

    def __repr__(self):
        return f'<Lecture {self.lecture_id!r}'

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# UserBase.metadata.drop_all(bind=engine)
UserBase.metadata.create_all(bind=engine)

# lectureBase.metadata.drop_all(bind=engine)
lectureBase.metadata.create_all(bind=engine)

longtxt = "2.수강신청더보기란추가->튜터가 적은 소개글 보여줌(모달창or히든창)[못 할 수도?]\n4.학수번호 검색기능추가\n5.신청버튼 클릭시 내 신청강좌에 담김\n7.신청모달에서 강의추가 누르면 강의맞는지확인후(DB확인후)->추가(요건 새로고침하면 될겁니다)"

@app.route("/addlecture", methods=['POST'])
def add_lecture():
    content = request.get_json(silent=True)
    college = content["college"]
    department = content["dept"]
    lecture_id = content["id"]
    name = content["name"]
    professor = content["prof"]

    if db_session_Lecture.query(Lecture).filter_by(lecture_id=lecture_id).first() is None:
        l = Lecture(lecture_id=lecture_id, college=college, department=department, name=name, professor=professor)
        db_session_Lecture.add(l)
        db_session_Lecture.commit()
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route("/getallLecture", methods=['GET'])
def get_AllLecture():
    output = {}
    result = db_session.query(Lecture).all()
    check = False

    for i in result:
        check = True
        temp = {}
        lecture_id = i.lecture_id

        temp["lecture_id"] = i.lecture_id
        temp["name"] = i.name
        temp["professor"] = i.professor
        temp["department"] = i.department
        temp["college"] = i.college

        if lecture_id in output:
            continue
        else:
            output[lecture_id] = temp

    if(check):
        return jsonify(lectures = output)
    else:
        return jsonify(success=check)

@app.route("/adduser", methods=['POST'])
def add_user():
    content = request.get_json(silent=True)
    user_id = content["id"]
    name = content["name"]

    if db_session_User.query(User).filter_by(user_id=user_id).first() is None:
        u = User(user_id=user_id, name=name)
        db_session_User.add(u)
        db_session_User.commit()
        return jsonify(success = True)
    else:
        return jsonify(success=False)

@app.route("/login", methods=["POST"])
def login():
    content = request.get_json(silent=True)
    user_id = content["id"]
    name = content["name"]
    result = db_session_User.query(User).filter_by(user_id=user_id)

    check = False
    for i in result:
        if user_id == i.user_id:
            if name == i.name:
                check = True
            else:
                check = False
            break
    return jsonify(success = check)

@app.route("/getalluser", methods=["GET"])
def getallusers():
    output = {}
    check = False
    result = db_session_User.query(User).all()

    for i in result:
        check = True
        temp = {}
        user_id = i.user_id
        temp["user_id"] = i.user_id
        temp["name"] = i.name
        if user_id in output:
            continue
        else:
            output[user_id] = temp
    if check:
        return jsonify(output)
    else:
        return jsonify(success = False)


@app.route("/addcourse", methods=['POST'])
def add_Course():
    content = request.get_json(silent=True)
    course_id = content["id"]
    course_name = content["name"]
    professor = content["professor"]
    tutor = content["tutor"]
    tutee = content["tutee"]
    motivation = content["motivation"]
    syllabus = content["syllabus"]
    schedule = content["schedule"]

    temp = tutee.replace(" ", "")
    if(len(temp) != 0):
        tutees = temp.split(",")

        for i in tutees:
            if isInUser(i):
                continue
            else:
                return jsonify(success=False)

    if db_session.query(course).filter_by(course_id=course_id).first() is None:
        c = course(course_id=course_id, course_name=course_name, professor=professor, tutor=tutor, tutee=tutee, motivation=motivation, syllabus=syllabus, schedule=schedule)
        db_session.add(c)
        db_session.commit()
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route("/getcourse", methods=['POST'])
def get_Course():
    content = request.get_json(silent=True)
    course_id = content["id"]
    output = {}
    check = False
    result = db_session.query(course).filter_by(course_id=course_id)

    for i in result:
        if i.course_id == course_id:
            check = True
            output["course_id"] = i.course_id
            output["course_name"] = i.course_name
            output["professor"] = i.professor
            output["tutee"] = i.tutee
            output["tutor"] = i.tutor
            output["motivation"] = i.motivation
            output["syllabus"] = i.syllabus
            output["schedule"] = i.schedule

            if(len(i.tutee) == 0):
                output["tuteeNum"] = 0
            else:   
                output["tuteeNum"] = len(i.tutee.split(','))
            break

    if(check):
        return jsonify(output)
    else:
        return jsonify(success=check)

@app.route("/getallmycourse", methods=['POST'])
def get_Allcourse():
    content = request.get_json(silent=True)
    user_id = content["id"]
    output = {}
    result = db_session.query(course).all()
    users = db_session.query(User).all()

    check = False

    for i in result:
        if user_id in i.tutee:
            check = True
            temp = {}
            course_id = i.course_id
            currentTutee = StrToArray(i.tutee)

            tutor_name = "IDK"

            for j in users:
                if j.user_id == i.tutor:
                    tutor_name = j.name


            temp["id"] = i.course_id
            temp["name"] = i.course_name
            temp["professor"] = i.professor
            temp["tutor"] = tutor_name
            temp["tutee"] = currentTutee

            if course_id in output:
                continue
            else:
                output[course_id] = temp

    if(check):
        return jsonify(courses = output)
    else:
        return jsonify(success=check)

@app.route("/getallcourse", methods=['GET'])
def get_Allmycourse():
    output = {}
    result = db_session.query(course).all()

    check = False

    for i in result:
        check = True
        temp = {}
        course_id = i.course_id
        currentTutee = StrToArray(i.tutee)

        tutor_name = "IDK"
        users = db_session.query(User).filter_by(user_id=i.tutor)

        for j in users:
            if j.user_id == i.tutor:
                tutor_name = j.name


        temp["id"] = i.course_id
        temp["name"] = i.course_name
        temp["professor"] = i.professor
        temp["tutor"] = tutor_name
        temp["tutee"] = currentTutee
        temp["schedule"] = i.schedule

        if(len(i.tutee) == 0):
            temp["tuteeNum"] = 0
        else:   
            temp["tuteeNum"] = len(i.tutee.split(','))

        if course_id in output:
            continue
        else:
            output[course_id] = temp

    if(check):
        return jsonify(courses = output)
    else:
        return jsonify(success=check)

@app.route("/addtutee", methods=['POST'])
def add_tutee():
    content = request.get_json(silent=True)
    course_id = content["id"]
    newtutee = content["tutee"]
    check = False

    result = db_session.query(course).all()

    for i in result:
        if i.course_id == course_id:
            currentTutee = StrToArray(i.tutee)
            if newtutee in currentTutee:
                break
            elif len(currentTutee) > 5:
                break
            else:
                check = True
                currentTutee.append(newtutee)
                temp = str(currentTutee)
                temp = temp.strip("[""]"" "",""'")
                i.tutee = temp
                db_session.commit()
                break
    return jsonify(success = check)

def StrToArray(Str):
    temp = Str.strip("{""}"" ""[""]")
    temp = temp.replace(" ", "")
    Arr = temp.split(",")
    return Arr

@app.route("/test", methods=['GET'])
def test():
    return jsonify(success=True)

@app.route("/longtest", methods=['GET'])
def longtest():
    return jsonify(test = longtxt)

@app.route("/delete", methods=['POST'])
def delete_all():
    result = db_session.query(course).all()

    for i in result:
        db_session.delete(i)
        db_session.commit()

    check= True

    return jsonify(success = check)

def isInLecture(course_id):
    if db_session_Lecture.query(Lecture).filter_by(lecture_id=course_id).first() is None:
        return False
    else:
        return True

def isInUser(id):
    if db_session_User.query(User).filter_by(user_id=id).first() is None:
        return False
    else:
        return True

if __name__ == "__main__":
    app.run(host='localhost', port=8888)