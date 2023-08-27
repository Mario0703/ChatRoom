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

# rooms_cursor.execute(RoomTable)
# users_cursor.execute(UsersTable)
# messages_cursor.execute(MessagesTable)
# users_cursor.execute(UserRoomTable)
# rooms_cursor.execute(RoomMessageTable)
