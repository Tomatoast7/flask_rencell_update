from website import create_app, db
from website.models import student

app = create_app()

with app.app_context():
    # Fetch all users
    new_student = student.query.all()
    for student in new_student:
        print(f'ID: {student.studentid}, FirstName: {student.first_name}, LastName : {student.last_name} , Section : {student.section}')
      