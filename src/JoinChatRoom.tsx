import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useState, ChangeEvent } from "react";

export function JoingRoom() {
  const [RoomName, SetRoomName] = useState<String>("");
  const GetRoomName = (event: ChangeEvent<HTMLInputElement>) => {
    const Value = event.target.value;
    SetRoomName(String(Value));
  };

  const GetRoomData = async () => {
    try {
      await axios
        .get(`http://localhost:5000/GetRoomData/${RoomName}`)
        .then((response) => {
          console.log(response);
        });
    } catch (err) {}
  };
  return (
    <div>
      <label>
        <input
          onChange={GetRoomName}
          type="text"
          placeholder="RoomName"
        ></input>
      </label>
      <button onClick={GetRoomData}>Join Room!</button>
    </div>
  );
}
