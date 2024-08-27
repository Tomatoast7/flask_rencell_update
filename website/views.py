from flask import Blueprint, render_template, request, flash, redirect, url_for,jsonify
from flask_login import login_required, logout_user, current_user
from .models import student
from . import db

views = Blueprint('views', __name__)

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
        attendances = request.form['attendance']

    
    new_student = student(first_name=fname, last_name=lname, section=email, attendance=attendances, totalPresent=0, totalAbsent=0)
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
            print("present", students.totalPresent)
            print("absent", students.totalAbsent)
       
        
    
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


@views.route('/report')
def report():
    #students = student.query.all()  # Query all student records
    return render_template("report.html")


@views.route('/update-attendance', methods=['POST'])
def update_attendance():
    # Process the form data
    data = request.form
    # Implement logic to update the database or in-memory data
    return jsonify({'status': 'success'})

# @views.route('/submit_attendance', methods=['POST'])
# def submit_attendance():
#     student_ids = request.form.getlist('studentid[]')
#     first_names = request.form.getlist('first_name[]')
#     last_names = request.form.getlist('last_name[]')
#     sections = request.form.getlist('section[]')
#     attendances = request.form.getlist('attendance[]')

#     # Ensure all lists are the same length
#     if len(student_ids) == len(first_names) == len(last_names) == len(sections) == len(attendances):
#         for i in range(len(student_ids)):
#             student_entry = student(
#                 studentid=student_ids[i],
#                 first_name=first_names[i],
#                 last_name=last_names[i],
#                 section=sections[i],
#                 attendance=attendances[i]
#             )
#             db.session.add(student_entry)
        
#         db.session.commit()
#         flash("Attendance data has been saved successfully.", "success")
#     else:
#         flash("There was an error processing the attendance data.", "danger")

#     return redirect(url_for('views.report'))

# @views.route('/view_students')
# def view_students():
#     students = student.query.all()  # Query all records from the student table
#     return render_template('view_students.html', students=students)
