import React, { useEffect, useState } from "react";
import * as bases from "../components/ui/base";
import axios from "axios";

export default function Page() {
  let search = "";
  const [data, setData] = useState([]); // хук для обновления данных на экране

  async function getData() {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/resume/list/?${search}`,
      );
      if (response.status === 200) {
        setData(response.data.resumes);
      }
      console.log(response);
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    // хук для выполнения действия, когда зависимости(deps) изменились (триггер)
    getData();
  }, []);

  return (
    <bases.Base1>
      <div>
        <div className="row mb-2">
          {data &&
            data.map((item: any, index: number) => (
              <div className="col-md-6">
                <div className="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
                  <div className="col p-4 d-flex flex-column position-static">
                    <strong className="d-inline-block mb-2 text-primary-emphasis">
                      имя пользователя
                    </strong>
                    <h3 className="mb-0">first_name</h3>
                  </div>
                  <div className="col-auto d-none d-lg-block">
                    <svg
                      className="bd-placeholder-img"
                      width="200"
                      height="250"
                      xmlns="http://www.w3.org/2000/svg"
                      role="img"
                      aria-label="Placeholder: Thumbnail"
                      preserveAspectRatio="xMidYMid slice"
                      focusable="false"
                    >
                      <title>Placeholder</title>
                      <rect width="100%" height="100%" fill="#55595c"></rect>
                      <text x="50%" y="50%" fill="#eceeef" dy=".3em">
                        Thumbnail
                      </text>
                    </svg>
                  </div>
                </div>
              </div>
            ))}
        </div>
      </div>
    </bases.Base1>
  );
}
