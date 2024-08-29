from flask import Blueprint, render_template, request, redirect, session, flash, redirect, url_for, jsonify
from flask_login import login_required, logout_user, current_user
from .models import student
from . import db
import os
import os.path
import base64
import secrets
import signal
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText

secret_key = secrets.token_hex(16)

views = Blueprint('views', __name__)
views.secret_key = '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'

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

@views.route('/')
def index():
    return render_template("index.html", user=current_user)

@views.before_request
def handle_method_override():
    if request.method == 'POST' and '_method' in request.form:
        request.method = request.form['_method'].upper()

@views.route('/home', methods=['GET'])
def home():
    students = student.query.all()
#    for stud in students:
#        stud.totalPresent = 0
#        stud.totalAbsent = 0 

#        db.session.commit() 

    return render_template("home.html", students=students)

@views.route('/home/register', methods=['GET'])
def registerStudent():
    
    return render_template("register.html")



@views.route('/home/create', methods=['POST'])
def saveStudent():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        section = request.form['section']
        

    
    new_student = student(first_name=fname, last_name=lname, email=email, section=section, totalPresent=0, totalAbsent=0, attendance="")
    db.session.add(new_student)
    db.session.commit()
    
    studentFetch  = student.query.all()


    
    return render_template("home.html", students=studentFetch)




@views.route('/home/attendanceCreate', methods=['POST'])
def attendanceCreate():
    if request.method == 'POST':
        form = request.form

        for key, value in form.items():
            students = student.query.filter_by(studentid=int(key)).first()
            if(value == 'present'):
                students.totalPresent += 1
            else:
                students.totalAbsent += 1
            db.session.commit()
        
        return redirect(url_for("views.home"))

@views.route('/home/deleteStudent/<int:id>', methods=['DELETE', 'POST'])
def deleteStudent(id): 
    
    if request.method == 'DELETE':\
        
        deleteStudent = student.query.get(id)

       
        if deleteStudent is None:   
            flash('Student not found', 'danger')
        
        db.session.delete(deleteStudent)
        db.session.commit()

      

        flash('Student deleted successfully', 'success')
        return redirect(url_for('views.home'))
    else:
        return 'Method Not Allowed', 405    

@views.route('/home/student_attendance', methods=['GET'])
def student_attendance():
    students = student.query.all()

    return render_template("attendance.html", students=students)

@views.route('/update-attendance', methods=['POST'])
def update_attendance():
   
    data = request.form
    
    return jsonify({'status': 'success'})

#Middleware
@views.route('/end_session', methods=['POST'])
def end_session():
    # Terminate the process
    os.kill(os.getpid(), signal.SIGINT)  # Simulate Ctrl+C
    return 'Session ending...', 200
