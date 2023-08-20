import { Route, Routes } from "react-router-dom";
import LandingPage from "./LandingPage";
import { SignUp } from "./Signup";
import { Login } from "./Login";
import { JoingRoom } from "./JoinChatRoom";
import { Room } from "./Room";
import { CreateRoom } from "./CreateRoom";
export function Pages() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage></LandingPage>}></Route>
      <Route path="/SignUp" element={<SignUp></SignUp>}></Route>
      <Route path="/Login" element={<Login></Login>}></Route>
      <Route path="/JoinRoom" element={<JoingRoom></JoingRoom>}></Route>
      <Route path="/Room/:ChatRoom_id" element={<Room></Room>}></Route>
      <Route path="/CreateRoom" element={<CreateRoom></CreateRoom>}></Route>
    </Routes>
  );
}
