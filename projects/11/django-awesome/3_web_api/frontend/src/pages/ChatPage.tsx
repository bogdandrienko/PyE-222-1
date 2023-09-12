import React from "react";
import * as bases from "../components/ui/bases";
import axios from "axios";

export default function Page() {
  let message = "";

  async function sendData() {
    try {
      const data = {
        message: message,
      };
      const response = await axios.post(
        "http://127.0.0.1:8000/messages/",
        data,
      );
      console.log("response: ", response);
    } catch (error) {
      console.log("error: ", error);
    }
  }

  async function getData() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/messages/");
      console.log("response: ", response);
    } catch (error) {
      console.log("error: ", error);
    }
  }

  return (
    <bases.Base1>
      <div className={"container p-3"}>
        <div className="col-md-7 col-lg-8">
          <form
            className="needs-validation"
            onSubmit={(event) => {
              event.preventDefault();
              sendData();
            }}
          >
            <label className="form-label">Сообщение</label>
            <div className="input-group input-group-lg">
              <input
                type="text"
                className="form-control w-75"
                id="firstName"
                placeholder=""
                required
                minLength={10}
                onChange={(event) => {
                  // event - событие onChange для этого input-а
                  // event.target - сам input
                  // event.target.value - значение input
                  message = event.target.value;
                }}
              />
              <button className="w-25 btn btn-primary btn-lg" type="submit">
                отправить
              </button>
            </div>
          </form>
        </div>
      </div>
    </bases.Base1>
  );
}
