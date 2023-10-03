import React from "react";
import * as bases from "../components/ui/base";
import axios from "axios";

export default function Page() {
  let first_name = "";

  async function sendData() {
    try {
      const response = await axios.post(`http://127.0.0.1:8000/register/`, {
        first_name: first_name,
      });
      if (response.status === 201) {
      }
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  }
  return (
    <bases.Base1>
      <div>
        <div className="px-4 pt-5 my-5 text-center border-bottom">
          <h1 className="display-4 fw-bold text-body-emphasis">
            Centered screenshot
          </h1>
          <div className="col-lg-6 mx-auto">
            <p className="lead mb-4">
              Quickly design and customize responsive mobile-first sites with
              Bootstrap, the world’s most popular front-end open source toolkit,
              featuring Sass variables and mixins, responsive grid system,
              extensive prebuilt components, and powerful JavaScript plugins.
            </p>
            <div className="d-grid gap-2 d-sm-flex justify-content-sm-center mb-5">
              <button
                type="button"
                className="btn btn-primary btn-lg px-4 me-sm-3"
              >
                Primary button
              </button>
              <button
                type="button"
                className="btn btn-outline-secondary btn-lg px-4"
              >
                Secondary
              </button>
            </div>
          </div>
          <div className="overflow-hidden">
            <div className="container px-5">
              <img
                src="bootstrap-docs.png"
                className="img-fluid border rounded-3 shadow-lg mb-4"
                alt="Example image"
                width="700"
                height="500"
                loading="lazy"
              />
            </div>
          </div>

          <hr />
          <div className="fw-bold text-success border border-1 border-success card m-2 p-2 display-6">
            success
          </div>
          <hr />
          <div className="fw-bold text-danger border border-1 border-danger card m-2 p-2 display-6">
            error
          </div>
          <hr />
          <form
            onSubmit={(event) => {
              event.preventDefault();
              sendData();
            }}
          >
            <div className="card">
              <div className="card-header lead">
                Заполните данные и отправьте форму!
              </div>
              <div className="card-body">
                <input
                  name="first_name"
                  type="text"
                  placeholder="введите сюда своё имя"
                  className="form-control form-control-lg"
                  onChange={(event) => {
                    first_name = event.target.value;
                  }}
                />
                <hr />
                <input
                  name="last_name"
                  type="text"
                  placeholder="введите сюда сво фамилию"
                  className="form-control form-control-lg"
                  required
                />
                <hr />
                <input
                  name="datetime"
                  type="date"
                  className="form-control form-control-lg"
                  required
                />
                <hr />
                <select
                  name="education"
                  className="form-control form-control-lg"
                  required
                >
                  <option value="">Выберите образование</option>
                  <option value="Высшее">Высшее</option>
                  <option value="Средне-специальное">Средне-специальное</option>
                  <option value="Школа">Школа</option>
                </select>
              </div>
              <div className="card-footer">
                <button type="submit" className="btn btn-lg btn-warning w-75">
                  Отправить
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </bases.Base1>
  );
}
