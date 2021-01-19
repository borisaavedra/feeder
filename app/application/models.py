from application import db
from application import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(100), unique=False, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    myposts = db.relationship("Posts", backref="users", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.name)


posts_tags = db.Table("posts_tags",
            db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True),
            db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
            extend_existing=True
        )


class Posts(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(400), nullable=False)
    pic_url = db.Column(db.String(400), nullable=False)
    publish_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    tags = db.relationship("Tags", secondary=posts_tags, lazy="subquery",
    backref=db.backref("posts", lazy=True))

    def __repr__(self):
        return "<Post {}>".format(self.title)


class Tags(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return "<Tag {}>".format(self.name)


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))