from sqlalchemy.sql import text
from db import db
import users
import topics

def get_list():
    sql = text("SELECT M.id, M.content, U.username, M.sent_at, T.name, M.like_count FROM messages M, users U, topics T WHERE M.user_id=U.id AND M.topic_id=T.id ORDER BY M.id")
    result = db.session.execute(sql)
    return result.fetchall()

def send(content, topic_name):
    user_id = users.user_id()
    topic_id = topics.get_id(topic_name)
    if user_id == 0:
        return False
    sql = text("INSERT INTO messages (content, user_id, topic_id, sent_at, like_count) VALUES (:content, :user_id, :topic_id, NOW(), :like_count)")
    db.session.execute(sql, {"content":content, "user_id":user_id, "topic_id":topic_id, "like_count":0})
    db.session.commit()
    return True

def update_like_count(message_id):
    sql = text("UPDATE messages SET like_count = (SELECT COUNT(*) FROM likes WHERE message_id=:message_id) WHERE id=:message_id")
    db.session.execute(sql, {"message_id":message_id})
    db.session.commit()

def search(query):
    sql = text("SELECT id, content, user_id, topic_id, sent_at, like_count FROM messages WHERE content LIKE :query")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    search_result = result.fetchall()
    print(f"search_results: {search_result}")
    return search_result