from flask import Flask, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app, supports_credentials=True)

# DB connections
users_db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="UserTest1"
)

rooms_db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="RoomDatabase1"
)

messages_db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="MessagesDatabase1"
)

# Cursours
messages_cursor = messages_db.cursor()
rooms_cursor = rooms_db.cursor()
users_cursor = users_db.cursor()

create_rooms_db = "CREATE DATABASE IF NOT EXISTS RoomDatabase1"
create_messages_db = "CREATE DATABASE IF NOT EXISTS MessagesDatabase1"
users_cursor_db = "CREATE DATABASE IF NOT EXISTS UserTest1"


rooms_cursor.execute(create_rooms_db)
messages_cursor.execute(create_messages_db)
users_cursor.execute(users_cursor_db)

for x in users_cursor:
    print(x)


@app.route("/AddUser", methods=["POST"])
def AddUserToDB():
    data = request.get_json()
    SendUserName = data.get("Name")
    SendUserPassword = data.get("password")

    insert_query = "INSERT INTO User (USER_NAME, user_password) VALUES (%s, %s)"
    values = (SendUserName, SendUserPassword)

    try:
        users_cursor.execute(insert_query, values)
        users_db.commit()
        return "Data has been added"
    except Exception as e:
        print(e)
        users_db.rollback()
        return "Failed to add data"


if __name__ == "__main__":
    app.run(debug=True)
