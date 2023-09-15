import React, { useState } from "react";
import * as bases from "../components/ui/bases";
import axios from "axios";

const data = [
  { id: 1, name: "Богдан А.", data_time: new Date(), point: 3 },
  { id: 2, name: "Богдан А. 2", data_time: new Date(), point: 2 },
  { id: 3, name: "Богдан А. 3", data_time: new Date(), point: 3 },
  { id: 4, name: "Богдан А. 4", data_time: new Date(), point: 3 },
];

export default function Page() {
  const [newData, setNewData] = useState([]);
  async function getData() {
    const response = await axios.get("http://127.0.0.1:8000/api/report/");
    console.log(response);
    setNewData(response.data);
  }

  return (
    <bases.Base1>
      <div className={"container"}>
        <div className={"input-group input-group-lg"}>
          <button className={"btn btn-lg btn-success"} onClick={getData}>
            getData
          </button>
          <a
            href={"http://127.0.0.1:8000/static/report/excel/15_09_2023.xlsx"}
            className={"btn btn-lg btn-warning"}
            onClick={getData}
          >
            скачать excel
          </a>
        </div>
        <table className="table table-striped table-light">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col" className={"w-50"}>
                Работник
              </th>
              <th scope="col">Время прохода</th>
              <th scope="col">Точка прохода</th>
            </tr>
          </thead>
          <tbody>
            {newData && newData.length > 0 ? (
              newData.map((item: any, index: number) => (
                <tr key={item.id}>
                  <th scope="row">{index + 1}</th>
                  <td>{item.post_id}</td>
                  <td>{item.user_id}</td>
                  <td
                    className={
                      item.value > 5 ? "fw-bold text-success" : "text-danger"
                    }
                  >
                    {item.value}
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={5}>Данных нет!</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </bases.Base1>
  );
}
