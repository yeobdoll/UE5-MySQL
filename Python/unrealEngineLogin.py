import mysql.connector

db = mysql.connector.connect(
    host="rkteam.kr",
    port=3307,
    user="aiquest",
    password="fO4-sv@)Qy",
    database="hzproject"
)

cursor = db.cursor()


def is_duplicate(id, pw, uid):
    query = f"SELECT * FROM users WHERE ID='{id}' OR PASSWORD='{pw}' OR UID='{uid}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result is not None


def login(id, pw):
    query = f"SELECT * FROM users WHERE ID='{id}' AND PASSWORD='{pw}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result is not None:
        return True, result
    else:
        return False, None


def register(id, pw, name, nickname, email, mainpmc, uid):
    if is_duplicate(id, pw, uid):
        return False, None
    else:
        query = f"INSERT INTO users (ID, PASSWORD, NAME, NICKNAME, EMAIL, MAINPMC, UID) VALUES ('{id}', '{pw}', '{name}', '{nickname}', '{email}', '{mainpmc}', '{uid}')"
        cursor.execute(query)
        db.commit()
        return True, (id, pw, name, nickname, email, mainpmc, uid)

cursor.close()
db.close()
