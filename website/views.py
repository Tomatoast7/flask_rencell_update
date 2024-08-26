from flask import Blueprint, render_template, request, flash, redirect, url_for,jsonify
from flask_login import login_required, logout_user, current_user
from .models import student
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("index.html", user=current_user)

@views.route('/home')
def home():
    return render_template("home.html")

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
