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
      <input onChange={Values} placeholder="Whats on your heart?"></input>
      <button onClick={postMessage}>Send Message</button>
      <MessagesBOX></MessagesBOX>
    </div>
  );
}
