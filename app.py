# Created On: 14-March-2023
# Created By: Roshni Vittanala
# Reference: https://codeberg.org/SnowCode/simple-forum
# This is main Python file which invokes different functions and renders different HTML views
# Operations involved:
# Login/Logout
# Register user
# Create topic
# List topics
# Reply to topic
from flask import Flask, redirect, render_template, request, flash  # import flask
from login import *  # import the login helper file
import helper, json, time  # Import the helper file and other modules

app = Flask(__name__)  # Create the app
db = helper.createDb(app)  # Get the database
Topic, Reply, db = db["Topic"], db["Reply"], db["db"]  # Get the classes
User = initLogin(app, db)  # Create and init the login manager (login helper file)
db.create_all()


def getTime():
    return time.asctime(time.localtime(time.time()))  # Get the current time and date


@app.route("/login")  # Render the login page, nothing more
def renderLogin():
    logout_user()
    return render_template("login.html")


@app.route("/login/post", methods=["POST"])
def login():  # Login backend
    try:
        loginUser(request.form["username"], request.form["password"], User)
        return redirect("/")
    except:
        try:
            createUser(request.form["username"], request.form["password"], db, User)
            return redirect("/")
        except:
            return redirect("/login")


@app.route("/")  # Render the homepage
def renderHome():
    return render_template(
        "index.html", topics=Topic.query.order_by(Topic.lastActivity.desc())
    )  # List all the topics in the reversed order


@app.route("/post")  # Render the 'write new topic' box
@login_required
def renderCreateTopic():
    return render_template("post.html")


@app.route("/post/post", methods=["POST"])  # Backend of the new topic box
def createTopic():
    topic = Topic(
        request.form["title"],
        request.form["content"],
        getTime(),
        getUsername(),
        request.form["category"],
    )
    db.session.add(topic)
    db.session.commit()
    return redirect("/topic/" + str(topic.id))


@app.route("/topic/<id>")  # Render a topic
def renderTopic(id):
    topic = Topic.query.filter_by(id=id).first_or_404()
    topic.views += 1  # Add one view
    db.session.add(topic)
    db.session.commit()  # Change the value of the view in the database
    return render_template(
        "topic.html", topic=topic, replies=Reply.query.filter_by(inReplyTo=id)
    )  # Render the page


@app.route("/reply/<id>", methods=["POST"])  # Reply to a post.
@login_required
def replyTo(id):
    topic = Topic.query.filter_by(id=id).first_or_404()
    topic.reply(getTime())  # Reply to the topic
    reply = Reply(
        request.form["body"], getTime(), current_user.username, id
    )  # Add the reply
    db.session.add(reply)
    db.session.add(topic)
    db.session.commit()  # Add everything in the database
    return redirect("/topic/" + str(id))  # Redirect to the correct page


@app.route("/like/<id>")  # Like a topic
@login_required
def likeTopic(id):
    topic = Topic.query.filter_by(id=id).first_or_404()
    topic.like(current_user.username)  # Call the 'like' function of the class 'Topic'
    db.session.add(topic)
    db.session.commit()
    return redirect("/topic/" + str(id))


@app.route("/like/reply/<id>/<idt>")  # Like a reply
@login_required
def likeReply(id, idt):
    reply = Reply.query.filter_by(id=id).first_or_404()
    reply.like(current_user.username)  # Call the like function of the class Reply
    db.session.add(reply)
    db.session.commit()
    return redirect("/topic/" + str(idt))  # Return to the topic


@app.route(
    "/top"
)  # Order the list of posts by thoses who have the biggest number of replies
def topList():
    topics = Topic.query.order_by(Topic.repliesNum.desc())
    return render_template("index.html", topics=topics)


@app.route("/new")  # Order the list like normal (redirect)
def redirectIndex():
    return redirect("/")


@app.route("/cat/<category>")  # Get the list of posts in a category
def catList(category):
    topics = Topic.query.filter_by(category=category).order_by(Topic.id.desc())
    return render_template("index.html", topics=topics)


app.run(debug=False, port='81', host='0.0.0.0')  # Run the app with no debug mode
