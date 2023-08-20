from flask import Flask, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app, supports_credentials=True)

# DB connections
users_db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="UserTest4"
)

rooms_db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="RoomDatabase4"
)

messages_db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="MessagesDatabase4"
)

# Cursours
messages_cursor = messages_db.cursor()
rooms_cursor = rooms_db.cursor()
users_cursor = users_db.cursor()

create_rooms_db = "CREATE DATABASE IF NOT EXISTS RoomDatabase4"
create_messages_db = "CREATE DATABASE IF NOT EXISTS MessagesDatabase4"
users_cursor_db = "CREATE DATABASE IF NOT EXISTS UserTest4"

rooms_cursor.execute(create_rooms_db)
messages_cursor.execute(create_messages_db)
users_cursor.execute(users_cursor_db)

# Here The tables as followsing: RoomTable, Messages Tabled and UsersTable.
# UserRoomTables is defines as a junctions table.
# links the room DB with the Users DB

RoomTable = """
    CREATE TABLE IF NOT EXISTS Room (
        Room_ID VARCHAR(40) PRIMARY KEY,
        Room_Name VARCHAR(50)
    )
"""

UsersTable = """
    CREATE TABLE IF NOT EXISTS User (
        user_id VARCHAR(40) PRIMARY KEY,
        Name VARCHAR(50),
        Password VARCHAR(50)
    )
"""

MessagesTable = """
    CREATE TABLE IF NOT EXISTS Messages (
        Messages_id VARCHAR(40) PRIMARY KEY,
        Messages_string VARCHAR(50),
        Room_ID VARCHAR(50),
        user_id VARCHAR(50),
        Author VARCHAR(50),
        FOREIGN KEY (user_id) REFERENCES User(user_id)
    )
"""

UserRoomTable = """
    CREATE TABLE IF NOT EXISTS UserRoom (
        UserRoom_ID INT AUTO_INCREMENT PRIMARY KEY,
        user_id VARCHAR (50),
        Room_ID VARCHAR (50),
        FOREIGN KEY (user_id) REFERENCES User(user_id),
        FOREIGN KEY (Room_ID) REFERENCES Room(Room_ID)

    )
"""


rooms_cursor.execute(RoomTable)
users_cursor.execute(UsersTable)
messages_cursor.execute(RoomTable)
users_cursor.execute(UserRoomTable)


@app.route("/GetRoomData/<Name>", methods=["POST", "GET"])
def GetRoom(Name):
    select_query = f"SELECT Room_Name FROM Room WHERE Room_Name = {Name}"
    rooms_cursor.execute(select_query)

    results = rooms_cursor.fetchall()

    if len(results) > 1:
        return "Multiple rooms found"
    elif len(results) == 1:
        return "Only one room found"
    else:
        return "No rooms found"


@app.route("/CreateRoom", methods=["POST"])
def CreateRoom():
    data = request.get_json()
    RoomName = data.get("Room")
    RoomID = data.get("Room_ID")

    query = f"INSERT INTO Room(Room_ID, Room_Name) VALUES ('{RoomID}', '{RoomName}')"

    rooms_cursor.execute(query)
    rooms_db.commit()

    rooms_cursor.execute("SELECT * FROM Room")

    for column_info in rooms_cursor:
        print(column_info)

    print(RoomName, RoomID)
    return "Room created!"


@app.route("/AddUser", methods=["POST"])
def AddUserTo_USER_DB():
    data = request.get_json()
    SendUserName = data.get("Name")
    SendUserPassword = data.get("password")
    Generated_User_id = data.get("ID")

    query = f"INSERT INTO User(user_id, Name, Password) VALUES ('{Generated_User_id}', '{SendUserName}', '{SendUserPassword}')"

    users_cursor.execute(query)
    users_db.commit()

    users_cursor.execute("SELECT * FROM User")

    for column_info in users_cursor:
        print(column_info)

    return "Data has been added"


if __name__ == "__main__":
    app.run(debug=True)
