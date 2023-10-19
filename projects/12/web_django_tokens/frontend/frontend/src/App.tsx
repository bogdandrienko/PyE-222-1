import React, {useState} from 'react';
import axios from "axios";

export default function App() {
  const [token, setToken] = useState("")

  async function loginUser(){
    const response = await axios.post("http://127.0.0.1:8000/api/token/", {
      username: "admin", password: "admin"
    })
    console.log("response", response)
    setToken(response.data.access)
  }

  async function getData(){
    const response = await axios.get("http://127.0.0.1:8000/api/drf/private/users_list",
        {headers: {Authorization: `Bearer ${token}`}})
    console.log("response", response)
  }

  function clearToken() {
      setToken("")
  }

  return (
    <div>
      <div>token: --{token}--</div>
      <hr/>
      <hr/>
      <button onClick={loginUser}>loginUser</button>
      <button onClick={getData}>getData</button>
      <button onClick={clearToken}>clearToken</button>
    </div>
  );
}
