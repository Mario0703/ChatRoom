import { Link } from "react-router-dom";
import axios from "axios";
import { useState, ChangeEvent } from "react";

interface RoomJSON {
  Room_id: string;
  Room_Name: string;
}

export function JoingRoom() {
  const [RoomName, SetRoomName] = useState<string>("");
  const [ShowRooms, SetRooms] = useState<[RoomJSON]>();

  const GetRoomName = (event: ChangeEvent<HTMLInputElement>) => {
    const Value = event.target.value;
    SetRoomName(Value);
  };

  const SendRoomName = async () => {
    try {
      const response = await axios.get(
        `http://localhost:5000/GetRoomData/${RoomName}`
      );
      SetRooms(response.data);
    } catch (err) {
      console.log(err);
    }
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
      <button onClick={SendRoomName}>Search for a room!</button>
      {ShowRooms && ShowRooms.length > 0 ? (
        <div>
          <ul>
            {ShowRooms.map((room, index) => (
              <li onClick={() => console.log(index, room.Room_id)} key={index}>
                <Link to={`/Room/${room.Room_id}`}>{room.Room_Name}</Link>
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <div>No rooms</div>
      )}
    </div>
  );
}
