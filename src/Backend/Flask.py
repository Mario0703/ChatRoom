from flask import Flask, request, jsonify, session
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config["SECRET_KEY"] = "MyKey"
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = True
# DB connections
users_db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="UserTest7"
)

rooms_db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="RoomDatabase7"
)

messages_db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="MessagesDatabase7"
)

# Cursours
messages_cursor = messages_db.cursor()
rooms_cursor = rooms_db.cursor()
users_cursor = users_db.cursor()

create_rooms_db = "CREATE DATABASE IF NOT EXISTS RoomDatabase7"
create_messages_db = "CREATE DATABASE IF NOT EXISTS MessagesDatabase7"
users_cursor_db = "CREATE DATABASE IF NOT EXISTS UserTest7"


rooms_cursor.execute(create_rooms_db)
messages_cursor.execute(create_messages_db)
users_cursor.execute(users_cursor_db)
# Here The tables as followsing: RoomTable, Messages Tabled and UsersTable.
# UserRoomTables is defines as a junctions table.
# links the room DB with the Users DB


users_cursor.execute("SHOW KEYS FROM  UserRoomJunctionTable")

for x in users_cursor:
    print(x)


@app.route("/GetRoomData/<Name>", methods=["POST", "GET"])
def GetRoom(Name):
    select_query = f"SELECT Room_Name, Room_ID FROM Room WHERE Room_Name = '{Name}'"
    rooms_cursor.execute(select_query)

    results = rooms_cursor.fetchall()
    print(results)
    if len(results) > 1 or len(results) == 1:
        room_data = [
            {"Room_Name": result[0], "Room_id": result[1]} for result in results
        ]
        return jsonify(room_data)

    else:
        return "No rooms found"


@app.route("/AddMessage", methods=["POST"])
def AddMessageToDB():
    data = request.get_json()
    String = data.get("id")
    content = data.get("content")
    author = data.get("author")
    RoomID = data.get("Room")
    print(RoomID)
    query = "INSERT INTO Messages (Messages_id,Messages_string,Room_ID,user_id,Author)"
    return "Messeges has been added"


@app.route("/CheckLogin", methods=["POST"])
def CheckLogin():
    data = request.get_json()
    Submitted_Username = data.get("Username")
    Submitted_Password = data.get("password")
    query = "SELECT Name, Password FROM User WHERE Name = %s AND Password = %s"
    params = (Submitted_Username, Submitted_Password)

    users_cursor.execute(query, params)
    row = users_cursor.fetchone()
    print(row)
    if row:
        session["Username"] = row[0]
        print(session["Username"])
        return f'logged in as {session["Username"]}'
    else:
        print("User not found.")
        return "Users seached for"


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return "User logged out"


@app.route("/GetLoginSession", methods=["GET"])
def GetLoginSession():
    Name = session.get("Username")
    print(Name)
    if "Username" in session:
        return {"Username": session["Username"]}
    else:
        return "User not in session!"


@app.route("/CreateRoom", methods=["POST"])
def CreateRoom():
    data = request.get_json()
    Room_Name = data.get("Room")
    Room_ID = data.get("Room_ID")

    query = f"INSERT INTO Room(Room_ID, Room_Name) VALUES ('{Room_ID}', '{Room_Name}')"

    rooms_cursor.execute(query)
    rooms_db.commit()

    rooms_cursor.execute("SELECT * FROM Room")

    for column_info in rooms_cursor:
        print(column_info)

    return "Room created!"


@app.route("/AddUser", methods=["POST"])
def AddUserTo_USER_DB():
    data = request.get_json()
    SendUserName = data.get("Name")
    SendUserPassword = data.get("password")
    Generated_User_id = data.get("ID")

    print(SendUserName)
    query = f"INSERT INTO User(user_id, Name, Password) VALUES ('{Generated_User_id}', '{SendUserName}', '{SendUserPassword}')"

    users_cursor.execute(query)
    users_db.commit()

    users_cursor.execute("SELECT * FROM User")

    for column_info in users_cursor:
        print(column_info)

    return "User has been added to the database"


if __name__ == "__main__":
    app.run(debug=True)
