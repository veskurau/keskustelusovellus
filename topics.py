from sqlalchemy.sql import text
from db import db
import users

# def get_list():
#     sql = text("SELECT M.content, U.username, M.sent_at FROM messages M, users U WHERE M.user_id=U.id ORDER BY M.id")
#     result = db.session.execute(sql)
#     return result.fetchall()

def create_topic(topic):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO topics (name, user_id) VALUES (:name, :user_id)")
    db.session.execute(sql, {"name":topic, "user_id":user_id})
    db.session.commit()
    return True