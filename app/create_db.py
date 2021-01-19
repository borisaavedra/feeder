from application import create_app, db
from application.models import Users, Posts, Tags, posts_tags

def create_db():
    app = create_app()
    app.app_context().push()
    db.create_all()
    print("** DATABASES CREATED **")
    print("** CONTEXT PUSHED **")