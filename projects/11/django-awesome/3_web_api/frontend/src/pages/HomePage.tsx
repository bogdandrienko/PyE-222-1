import { Link } from "react-router-dom";
import React from "react";
import * as bases from "../components/ui/bases";
import _default from "react-redux/es/components/connect";

export default function Page() {
  return (
    <bases.Base1>
      <div className="px-4 py-5 my-5 text-center">
        <img
          className="d-block mx-auto mb-4"
          src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo.svg"
          alt=""
          width="72"
          height="57"
        />
        <h1 className="display-5 fw-bold text-body-emphasis">Кадровый учёт</h1>
        <div className="col-lg-6 mx-auto">
          <p className="lead mb-4">
            Веб-платформа для ведения учёта персонала для компании.
          </p>
          <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
            <Link
              to={"/create"}
              type="button"
              className="btn btn-primary btn-lg px-4 gap-3"
            >
              Создать карточку работника
            </Link>
            <Link
              to={"/search"}
              type="button"
              className="btn btn-outline-secondary btn-lg px-4"
            >
              Поиск работника
            </Link>
          </div>
        </div>
      </div>
    </bases.Base1>
  );
}
