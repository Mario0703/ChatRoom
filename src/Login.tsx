import axios from "axios";
import { useState, ChangeEvent } from "react";
import { Form } from "react-router-dom";

export function Login() {
  const [Submitted_Username, setName] = useState<string>(""); // Use lowercase for variable names
  const [Submitted_password, setPassword] = useState<string>(""); // Use lowercase for variable names

  const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;

    if (name === "username") {
      setName(value);
    } else {
      setPassword(value);
    }
  };

  const handleSubmitForm = async () => {
    const form: FormData = new FormData();

    form.append("Password", Submitted_password);
    form.append("Username", Submitted_Username);

    const formData = {
      Username: Submitted_Username,
      password: Submitted_password,
    };

    await axios
      .post("http://localhost:5000/CheckLogin", formData, {
        withCredentials: true,
      })
      .then((response) => console.log(response));
  };

  return (
    <div>
      <form>
        <label>
          UserName:
          <input
            onChange={handleInputChange}
            placeholder="UserName"
            name="username"
          />
        </label>
      </form>
      <form>
        <label>
          Password:
          <input
            onChange={handleInputChange}
            placeholder="Password"
            name="password"
          />
        </label>
      </form>
      <button onClick={handleSubmitForm}>Submit</button>{" "}
      {/* Add a submit button */}
    </div>
  );
}
