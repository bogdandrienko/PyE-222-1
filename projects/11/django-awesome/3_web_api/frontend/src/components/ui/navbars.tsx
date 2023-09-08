import React from "react";
import { Link } from "react-router-dom";

export function Navbar1() {
  return (
    <header className="p-3 text-bg-dark">
      <div className="container">
        <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <a
            href="/"
            className="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none"
          >
            <svg
              className="bi me-2"
              width="40"
              height="32"
              role="img"
              aria-label="Bootstrap"
            ></svg>
          </a>

          <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
            <li>
              <Link to={"/"} className="nav-link px-2 text-white">
                Домашняя страница
              </Link>
            </li>
            <li>
              <Link to={"/create"} className="nav-link px-2 text-white">
                Создать карточку работника
              </Link>
            </li>
            <li>
              <Link to={"/list"} className="nav-link px-2 text-secondary">
                Список работников
              </Link>
            </li>
            <li>
              <a href="#" className="nav-link px-2 text-white disabled">
                Зарплатный лист
              </a>
            </li>
          </ul>

          <form
            className="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3"
            role="search"
          >
            <input
              type="search"
              className="form-control form-control-dark text-bg-dark"
              placeholder="искать..."
              aria-label="Search"
            />
          </form>

          <div className="text-end">
            <button type="button" className="btn btn-outline-light me-2">
              Войти
            </button>
            <button type="button" className="btn btn-warning">
              Зарегистрироваться
            </button>
          </div>
        </div>
      </div>
    </header>
  );
}
