//Sign up page
import axios from "axios";
import { ChangeEvent, useState } from "react";
import { v4 as uuidv4 } from "uuid";

export function SignUp() {
  let [pass, SetPass] = useState<string>("");
  let [Name, SetName] = useState<string>("");
  const SendFormData = async () => {
    const Generated_id = uuidv4();
    const form: FormData = new FormData();
    form.append("Name", Name);
    form.append("password", pass);
    form.append("ID", Generated_id); // Use Generated_id directly

    const formData = {
      Name: Name,
      password: pass,
      ID: Generated_id,
    };

    await axios.post("http://localhost:5000/AddUser", formData).then((res) => {
      console.log(res.data);
    });
  };
  // Get Form Values
  const Val = (event: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;

    if (name === "password") {
      SetPass(value);
      console.log(pass);
    } else if (name === "Name") {
      SetName(value);
      console.log(Name);
    }
  };

  return (
    <div>
      <form>
        <label>
          <input
            type="text"
            name="Name"
            placeholder="Your Name"
            onChange={Val}
          ></input>
        </label>

        <label>
          <input
            type="password"
            name="password"
            placeholder="Your password"
            onChange={Val}
          ></input>
        </label>
      </form>
      <button onClick={SendFormData}>Submit </button>
    </div>
  );
}
