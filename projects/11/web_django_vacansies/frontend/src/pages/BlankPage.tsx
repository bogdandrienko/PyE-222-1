import { useState } from "react";
import axios from "axios";

export default function Page() {
  let name = "";

  async function sendData() {
    try {
      const response = await axios.post(`http://127.0.0.1:8080/api/blank/`, {
        name: name,
      });
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <div>
      <div className="container">
        <form
          className="needs-validation"
          onSubmit={(event) => {
            event.preventDefault();
            sendData();
          }}
        >
          <div>Введите Ваше имя:</div>
          <input
            onChange={(event) => {
              name = event.target.value;
            }}
            type={"text"}
            className={"form-control form-control-lg"}
          />
          <button type="submit" className="btn btn-lg btn-warning">
            Создать резюме
          </button>
        </form>
      </div>
    </div>
  );
}
