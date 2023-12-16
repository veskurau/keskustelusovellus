from flask import render_template, request, redirect, url_for
from app import app
import messages
import topics
import users
import visits
import likes

@app.route("/")
def index():
    visits.add_visit()
    messages_list = messages.get_list()
    visits_count = visits.get_counter()
    users_count = users.get_counter()
    user_is_admin = users.is_admin()
    return render_template("index.html", message_count=len(messages_list), messages=messages_list, visits_count=visits_count, users_count=users_count, user_is_admin=user_is_admin)


@app.route("/new")
def new():
    if users.user_id():
        topics_list = topics.get_list()
        if not topics_list:
            return render_template("error.html", message="Yhtään aihealuetta ei ole vielä luotu. Ylläpitäjän täytyy luoda ainakin yksi aihealue, jotta viestejä voi lähettää.")
        return render_template("new.html", topics=topics_list)
    else:
        return redirect("/")

@app.route("/topic")
def topic():
    if users.user_id():
        return render_template("topic.html")
    else:
        return redirect("/")

@app.route("/send", methods=["POST"])
def send():
    topic_name = request.form["topic_name"]
    content = request.form["content"]
    # Check that message is in the correct form
    error_message = error_message_for_messagetext(content)
    if error_message:
        return render_template("error.html", message=error_message)
    if messages.send(content, topic_name):
        return redirect("/")
    else:
        return render_template("error.html", message="Virhe viestin lähetyksessä")

@app.route("/create_topic", methods=["POST"])
def create_topic():
    topic = request.form["topic"]
    error_message = error_message_for_topic(topic)
    if error_message:
        return render_template("error.html", message=error_message)
    if topics.create_topic(topic):
        return redirect("/")
    else:
        return render_template("error.html", message="Virhe aihealueen luonnissa")

@app.route("/like/<int:message_id>", methods=["POST"])
def like(message_id):
    likes.like(message_id)
    return redirect(url_for("index"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        admin = int(request.form["admin"])

        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")

        # Check that username and password are in correct form
        error_message = error_message_for_username_password(username, password1)
        if error_message:
            return render_template("error.html", message=error_message)

        if users.register(username, password1, admin):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")


def error_message_for_username_password(username, password):
    if len(username) > 20 or len(password) > 20:
        return "Käyttäjätunnus ja salasana voivat olla maksimissaan 20 merkkiä pitkä"
    elif len(password) < 8:
        return "Salasanan täytyy olla vähintään 8 merkkiä pitkä"
    elif len(username) < 1:
        return "Käyttäjätunnuksen täytyy olla vähintään 1 merkin pituinen"
    else:
        return None

def error_message_for_messagetext(message):
    if len(message) > 1000:
        return "Viesti saa olla maksimissaan 1000 merkkiä pitkä"
    elif len(message) == 0:
        return "Tyhjää viestiä ei voi lähettää"
    else:
        return None

def error_message_for_topic(topic):
    if len(topic) > 30:
        return "Aihealue saa olla maksimissaan 30 merkkiä pitkä"
    elif len(topic) == 0:
        return "Tyhjää viestiä ei voi lähettää"
    else:
        return None