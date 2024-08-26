from website import create_app, db
from website.models import student

def print_student_data():
    app = create_app()
    
    with app.app_context():
        # Fetch all students
        students = student.query.all()
        if not students:
            print("No students found in the database.")
        for student in students:
            print(f'ID: {student.studentid}, First Name: {student.first_name}, Last Name: {student.last_name}, Section: {student.section}, Attendance: {student.attendance}')

if __name__ == "__main__":
    print_student_data()