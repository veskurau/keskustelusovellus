from sqlalchemy.sql import text
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from secrets import token_hex
from db import db

def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False

    if check_password_hash(user.password, password):
        session["user_id"] = user.id
        session["csrf_token"] = token_hex(16)
        return True
    else:
        return False

def user_id():
    return session.get("user_id", 0)

def logout():
    del session["user_id"]

def register(username, password, admin):
    hash_value = generate_password_hash(password)

    try:
        sql = text("INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)")
        db.session.execute(sql, {"username":username, "password":hash_value, "admin":admin})
        db.session.commit()
    except:
        return False
    return login(username, password)

def get_counter():
    result = db.session.execute(text(("SELECT COUNT(*) FROM users")))
    counter = result.fetchone()[0]
    return counter

def is_admin():
    if user_id():
        sql = text("SELECT admin FROM users WHERE id=:user_id")
        result = db.session.execute(sql, {"user_id":user_id()})
        is_admin = result.fetchone()
        if is_admin:
            return is_admin[0]
    return 0