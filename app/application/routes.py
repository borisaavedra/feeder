from flask import Blueprint, render_template, flash, redirect, url_for, request
from . import db
from flask_login import current_user, login_user, logout_user, login_required
from .forms import LoginForm, TagForm
from .models import Users, Tags, Posts


app = Blueprint("main", __name__)


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.load"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("main.login"))
    return render_template("login.html", title="Sign In", form=form)

@login_required
@app.route("/load-article", methods=["POST", "GET"])
def load():
    new_tag = TagForm()
    all_tags = Tags.query.all()
    all_posts = Posts.query.order_by(Posts.publish_date.desc()).all()
    tag_list = []
    if all_tags is None:
        all_tags = []
    if request.method == "POST":
        title = request.form["title"]
        summary = request.form["summary"]
        url = request.form["url"]
        pic_url = request.form["pic_url"]
        tags = request.form.getlist("tags")
        post_db = Posts.query.filter_by(url=url).first()
        for tag in tags:
            temp_tag = Tags.query.filter_by(id=int(tag)).first()
            if temp_tag is not None:
                tag_list.append(temp_tag)
        if post_db is None:
            new_post = Posts(
                title=title,
                summary=summary,
                url=url,
                pic_url=pic_url,
                user_id=current_user.id)
            for tag in tag_list:
                tag.posts.append(new_post)
            try:
                db.session.add(new_post)
                db.session.commit()
                flash("Post added")
            except:
                db.session.rollback()
                flash("Something went wrong")
            return redirect(url_for("main.load"))
    return render_template("load-article.html", all_tags=all_tags, new_tag=new_tag, all_posts=all_posts)

@login_required
@app.route("/delete-post", methods=["POST", "GET"])
def delete():
    new_tag = TagForm()
    all_tags = Tags.query.all()
    all_posts = Posts.query.all()
    if all_tags is None:
        all_tags = []
    if request.method == "POST":
        post_id = request.form["post_id"]
        post_to_delete = [post for post in all_posts if post.id == int(post_id)]
        try:
            db.session.delete(post_to_delete[0])
            db.session.commit()
            flash("Posts deleted")
        except Exception as e:
            db.session.rollback()
            flash(f"Something went wrong, please try again {e} {post_to_delete}")
        return redirect(url_for("main.load"))
    return render_template("load-article.html", all_tags=all_tags, new_tag=new_tag, all_posts=all_posts)


@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.login"))

@login_required
@app.route("/save-tag", methods=["POST", "GET"])
def savetag():
    new_tag = TagForm()
    if request.method == "POST":
        user_tag = str(new_tag.name.data).lower()
        tag_db = Tags.query.filter_by(name=user_tag).first()
        if tag_db is None:
            try:
                tag = Tags(name=user_tag)
                db.session.add(tag)
                db.session.commit()
                flash("Tag added")
            except:
                db.session.rollback()
                flash("Sorry, something went wrong")
        else:
            flash("This tag is already saved")
        return redirect(url_for("main.load"))    
    return redirect(url_for("main.load"))


@app.route("/free-stuff", methods=["GET"])
def feeder():
    user = 1 # This is Boris User ID
    try:
        all_posts = Posts.query.filter_by(user_id=user).order_by(Posts.publish_date.desc()).all()
    except Exception as e:
        flash(e)
    return render_template("free-stuff.html", all_posts=all_posts)
