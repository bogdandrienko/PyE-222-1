import React from "react";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import { store } from "./app/store";
import HomePage from "./pages/HomePage";
import BlankPage from "./pages/BlankPage";
// css
import "./css/bootstrap/bootstrap.css";
import "./css/font_awesome/css/all.min.css";
import "./css/my.css";

const container = document.getElementById("root")!;
const root = createRoot(container);

root.render(
  // <React.StrictMode>
  //   <Provider store={store}>
  //<div>Hello world!</div>
  //<HomePage/>
  <BlankPage />,
  // </Provider>
  // </React.StrictMode>
);
