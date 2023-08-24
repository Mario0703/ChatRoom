import axios from "axios";
import { useState, useEffect, ChangeEvent } from "react";
export function Room() {
  let [Value, Setvalue] = useState("");

  const Values = (event: ChangeEvent<HTMLInputElement>) => {
    let value = event.target.value;
    Setvalue(value);
    console.log(Value);
  };

  const postMessage = async () => {
    await axios
      .post("http://localhost:5000/AddMessage", { MessagesString: Value })
      .then((response) => {
        console.log(response.data);
      });
  };

  const UserList = () => {};

  const MessagesBOX = () => {
    return (
      <div>
        <div>
          <p></p>
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
          <MessagesBOX></MessagesBOX>
        </div>
      </div>
    </div>
  );
}
