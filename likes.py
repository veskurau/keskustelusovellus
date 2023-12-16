from sqlalchemy.sql import text
from db import db
import users
import messages

def like(message_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO likes (message_id, user_id) SELECT :message_id, :user_id WHERE NOT EXISTS (SELECT 1 FROM likes WHERE message_id=:message_id AND user_id=:user_id)")
    db.session.execute(sql, {"message_id":message_id, "user_id":user_id})
    db.session.commit()

    messages.update_like_count(message_id)

    return True