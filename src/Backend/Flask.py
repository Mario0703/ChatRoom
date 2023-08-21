from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app, supports_credentials=True)

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

RoomTable = """
    CREATE TABLE IF NOT EXISTS Room (
        Room_ID VARCHAR(40),
        Room_Name VARCHAR(50),
        PRIMARY KEY(Room_ID)
    )
"""
UsersTable = """
    CREATE TABLE IF NOT EXISTS User (
        user_id VARCHAR(40), 
        Name VARCHAR(50),
        Password VARCHAR(50),
        PRIMARY KEY(user_id)
    )
"""
MessagesTable = """
    CREATE TABLE IF NOT EXISTS Messages (
        Messages_id VARCHAR(40),
        Messages_string VARCHAR(50),
        Room_ID VARCHAR(50),
        user_id VARCHAR(50),
        Author VARCHAR(50),
        PRIMARY KEY(Messages_id),
        FOREIGN KEY (user_id) REFERENCES User(user_id)

    )
"""
RoomMessageTable = """
    CREATE TABLE IF NOT EXISTS RoomMessagesJunctionTable (
        Room_ID VARCHAR(50),
        Messages_ID VARCHAR(50),
        PRIMARY KEY (Messages_ID, Room_ID),FOREIGN KEY (Room_ID) REFERENCES Room(Room_ID),
        FOREIGN KEY (Messages_ID) REFERENCES Messages(Messages_id)
    )
"""
UserRoomTable = """
    CREATE TABLE IF NOT EXISTS UserRoomJunctionTable (
        user_id VARCHAR(50),
        Room_ID VARCHAR(50),
        PRIMARY KEY (user_id, Room_ID),FOREIGN KEY (user_id) REFERENCES User(user_id),
        FOREIGN KEY (Room_ID) REFERENCES Room(Room_ID)
    )
"""
rooms_cursor.execute(RoomTable)
users_cursor.execute(UsersTable)
messages_cursor.execute(MessagesTable)
users_cursor.execute(UserRoomTable)
rooms_cursor.execute(RoomMessageTable)


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
    String = data.get("MessagesString")
    print(String)
    return "Messeges has been added"


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
