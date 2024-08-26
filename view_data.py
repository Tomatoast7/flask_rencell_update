from website import create_app, db
from website.models import User, Note

app = create_app()

with app.app_context():
    # Fetch all users
    users = User.query.all()
    for user in users:
        print(f'ID: {user.id}, Email: {user.email}, Password : {user.password}')
        for note in user.notes:
            print(f' - Note ID: {note.id}, Content: {note.data}, Date: {note.date}')