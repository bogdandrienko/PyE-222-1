import axios from "axios";
import { useState } from "react";

export default function Page() {
  let search = "";
  const [data, setData] = useState([]);

  async function getData() {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/vacasies/?search=${search}`,
    );
    console.log(response);
    setData(response.data.list);
    console.log("data: ", data);
  }

  return (
    <div className={"container"}>
      <div className="px-4 py-5 my-5 text-center">
        <img
          className="d-block mx-auto mb-4"
          src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo.svg"
          alt=""
          width="72"
          height="57"
        />
        <h1 className="display-5 fw-bold text-body-emphasis">Centered hero</h1>
        <div className="col-lg-6 mx-auto">
          <p className="lead mb-4">
            Quickly design and customize responsive mobile-first sites with
            Bootstrap, the world’s most popular front-end open source toolkit,
            featuring Sass variables and mixins, responsive grid system,
            extensive prebuilt components, and powerful JavaScript plugins.
          </p>
          <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
            <input
              type={"text"}
              className={"form-control"}
              onChange={(event) => {
                search = event.target.value;
              }}
            />
            <button
              onClick={getData}
              type="button"
              className="btn btn-primary btn-lg px-4 gap-3"
            >
              ИСКАТЬ
            </button>
          </div>
        </div>
      </div>
      <hr />
      <div className="d-flex flex-column align-items-stretch flex-shrink-0 bg-body-tertiary w-75">
        <a
          href="/"
          className="d-flex align-items-center flex-shrink-0 p-3 link-body-emphasis text-decoration-none border-bottom"
        >
          <svg className="bi pe-none me-2" width="30" height="24"></svg>
          <span className="fs-5 fw-semibold">List group</span>
        </a>
        <div className="list-group list-group-flush border-bottom scrollarea">
          {data &&
            data.map((item: any, index: number) => (
              <a
                href="#"
                className="list-group-item list-group-item-action py-3 lh-sm"
                aria-current="true"
              >
                <div className="d-flex w-100 align-items-center justify-content-between">
                  <strong className="mb-1">{item.name}</strong>
                  <small>{item.experience}</small>
                </div>
                <div className="col-10 mb-1 small">{item.id}</div>
              </a>
            ))}
        </div>
      </div>
    </div>
  );
}
