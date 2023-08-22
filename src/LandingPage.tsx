import "bootstrap/dist/css/bootstrap.css";
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";

function LandingPage() {
  const [Username, setUsername] = useState();

  const Logout = async () => {
    axios.get("http://localhost:5000/logout", { withCredentials: true });
  };

  useEffect(() => {
    axios
      .get("http://localhost:5000/GetLoginSession", { withCredentials: true })
      .then((response) => {
        console.log(response.data);
      });
  }, []);

  return (
    <>
      <link
        href="./src/LandingPageStyle.css"
        rel="stylesheet"
        type="text/css"
      ></link>
      <header>
        <p>Logo goes here!</p>
        <h1>Chat room</h1>
        <span>Welcome user</span>
        <br></br>
        <span>Click me to logut</span>
      </header>
      <section>
        <div>
          <div>
            <p>
              The most populare chatroom of all time is here, log ing or sign up
              to get started!
            </p>
            <p>Check us out on social medier!</p>
          </div>
          <div>
            <p>Facebook Icon</p>
            <p>Instagram Icon</p>
            <p>Twitter Icon</p>
            <p>Youtube Icon</p>
          </div>
        </div>
        <div>
          <p>
            There is reasonx 6 more to pick Chatplatform more then chatplatform
            2 for live chat
          </p>
          <Link to={"/SignUp"}>
            <button className="btn btn-primary">Sign in!</button>
          </Link>
          <Link to={"/Login"}>
            <p>Already have an account? Click here to login</p>
          </Link>
          <Link to={"/JoinRoom"}>
            <p>Click here to join a room</p>
          </Link>
        </div>
      </section>
    </>
  );
}

export default LandingPage;
