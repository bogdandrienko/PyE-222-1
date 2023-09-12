import React, { useState } from "react";
import * as bases from "../components/ui/bases";
import axios from "axios";

export default function Page() {
  let firstName = "";
  let lastName = "";

  async function sendData() {
    try {
      console.log("firstName: ", firstName);
      console.log("lastName: ", lastName);
      const data = {
        firstName: firstName,
        lastName: lastName,
      };
      const response = await axios.post("http://127.0.0.1:8000/api/", data);
      console.log(response.status);
    } catch (error) {
      console.log(error);
    }
  }

  // const [form, setForm] = useState({
  //   firstName: "",
  //   lastName: "",
  //   iin: "",
  //   dataBirth: "",
  //   position: "",
  // });
  //
  // async function sendForm() {
  //   try {
  //     console.log(form);
  //     const response = await axios.post("http://127.0.0.1:8000/api/", form);
  //     console.log(response.status);
  //   } catch (error) {
  //     console.log(error);
  //   }
  // }

  return (
    <bases.Base1>
      <div className={"container p-3"}>
        <div className="col-md-7 col-lg-8">
          <h4 className="mb-3">Заполните карточку работника:</h4>
          <form
            className="needs-validation"
            onSubmit={(event) => {
              event.preventDefault(); // останавливает стандартное поведение формы(перезагрузка)
              sendData();
            }}
          >
            <div className="row g-3">
              <div className="col-sm-4">
                <label className="form-label">Имя</label>
                <input
                  type="text"
                  className="form-control"
                  id="firstName"
                  placeholder=""
                  required
                  minLength={10}
                  onChange={(event) => {
                    firstName = event.target.value;
                  }}
                />
                <div className="invalid-feedback">обязательно</div>
              </div>

              <div className="col-sm-8">
                <label className="form-label">Фамилия</label>
                <input
                  type="text"
                  className="form-control"
                  id="lastName"
                  placeholder=""
                  required
                  onChange={(event) => {
                    lastName = event.target.value;
                  }}
                />
                <div className="invalid-feedback">обязательно</div>
              </div>

              <div className="col-12">
                <label className="form-label">ИИН</label>
                <div className="input-group has-validation">
                  <span className="input-group-text">#</span>
                  <input
                    type="text"
                    className="form-control"
                    id="username"
                    placeholder="введите сюда ИИН"
                    required
                  />
                  <div className="invalid-feedback">обязательно</div>
                </div>
              </div>

              <div className="col-12">
                <label className="form-label">Дата рождения:</label>
                <div className="input-group has-validation">
                  <span className="input-group-text">#</span>
                  <input
                    type="date"
                    className="form-control"
                    id="username"
                    placeholder="введите сюда ИИН"
                    required
                  />
                  <div className="invalid-feedback">обязательно</div>
                </div>
              </div>

              <div className="col-12">
                <label className="form-label">
                  Должность
                  <span className="text-body-secondary">(необязательно)</span>
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="email"
                  placeholder="менеджер по продажам"
                />
              </div>
            </div>

            <hr className="my-4" />

            <button
              className="w-100 btn btn-primary btn-lg"
              //onClick={() => sendData()} // НЕЛЬЗЯ, иначе форма не валидируется
              type="submit"
            >
              Сохранить карточку
            </button>
          </form>
        </div>
      </div>
    </bases.Base1>
  );
}
