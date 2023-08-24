import { ChangeEvent, useState } from "react";
import axios from "axios";
import { v4 as uuidv4 } from "uuid";

export function CreateRoom() {
  const [Roomname, SetRoomName] = useState<String>("");
  const Val = (event: ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value;
    SetRoomName(String(value));
  };

  const SendRoomData = async () => {
    const Generated_id = uuidv4();
    try {
      await axios.post("http://localhost:5000/CreateRoom", {
        Room: Roomname,
        Room_ID: Generated_id,
      });
      console.log("Posted!", Roomname);
    } catch (err) {
      console.log("Error Posting");
    }
  };

  return (
    <div>
      <label>
        <input
          type="text"
          name="roomName"
          onChange={Val}
          placeholder="RoomName"
        ></input>
      </label>
      <button onClick={SendRoomData}>Create Room</button>
    </div>
  );
}
