import axios from "axios";
import { useState, ChangeEvent } from "react";
import { v4 as uuidv4 } from "uuid";
import { useParams } from "react-router-dom";

export function Room() {
  let [UserName, SetUserName] = useState<string>("");
  let [Value, Setvalue] = useState<string>("");

  let { Room_ID } = useParams<{ Room_ID: string }>();
  const Values = (event: ChangeEvent<HTMLInputElement>) => {
    let value = event.target.value;
    Setvalue(value);
    console.log(Value);
  };

  const postMessage = async () => {
    console.log(Room_ID);

    try {
      const response = await axios.get(
        "http://localhost:5000/GetLoginSession",
        { withCredentials: true }
      );
      const userName = response.data.Username;

      // Generate a unique message ID
      const messageId = uuidv4();
      SetUserName(userName);

      console.log(UserName);
      // Create a new message object
      const newMessage = {
        id: messageId,
        content: Value,
        author: userName, // Use the fetched user name
      };

      // Update state with user name
      // Post the new message
      await axios.post("http://localhost:5000/AddMessage", newMessage);
    } catch (error) {
      console.error("Error posting message:", error);
    }
  };

  const UserList = () => {};

  interface buttonsProps {
    IMGSCR: string;
    ALT: string;
    Funconality?: () => void;
  }

  const Buttons = (props: buttonsProps) => {
    const { IMGSCR, ALT, Funconality } = props;
    return (
      <div>
        <img src={IMGSCR} alt={ALT} onClick={() => Funconality}></img>
      </div>
    );
  };

  interface MessagesProps {
    content: string;
    editButton: React.ReactElement;
    deleteButton: React.ReactElement;
    author: string;
  }

  const Messages = (props: MessagesProps) => {
    const { content, editButton, deleteButton, author } = props;
    return (
      <div style={{ border: "1px solid black" }}>
        <div>
          <p>{author}</p>
        </div>
        <div className="Content">
          <p>{content}</p>
        </div>
        <div className="Buttons">
          {editButton}
          {deleteButton}
        </div>
      </div>
    );
  };

  return (
    <div>
      <p>Welcome to the chat</p>
      <button>Search for a user</button>
      <label>
        <input></input>
      </label>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <div>
          <label>
            <input onChange={Values} placeholder="Whats on your heart?"></input>
          </label>
          <button onClick={postMessage}>Send Message</button>
          <Messages
            author={UserName}
            content="Test"
            editButton={<button>Edit</button>}
            deleteButton={<button>Delete</button>}
          ></Messages>
        </div>
      </div>
    </div>
  );
}
