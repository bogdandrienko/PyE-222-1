import React from "react";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import { store } from "./app/store";
// css
import "./css/bootstrap/bootstrap.css";
import "./css/font_awesome/css/all.min.css";
import "./css/my.css";
// pages
import RegisterPage from "./pages/RegisterPage";
import ResumeListPage from "./pages/ResumeListPage";

const container = document.getElementById("root")!;
const root = createRoot(container);

root.render(
  // <React.StrictMode>
  <Provider store={store}>
    {/*<RegisterPage/>*/}
    <ResumeListPage />
  </Provider>,
  // </React.StrictMode>
);
