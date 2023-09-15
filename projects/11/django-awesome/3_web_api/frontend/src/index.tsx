import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import { Provider } from "react-redux";
// import { store } from "./app/store";
// css
import "./css/bootstrap/bootstrap.css";
import "./css/font_awesome/css/all.min.css";
import "./css/my.css";

import App, { App2 } from "./App";
import HomePage from "./pages/HomePage";
import CreateWorker from "./pages/CreateWorker";
import ChatPage from "./pages/ChatPage";
import ReportPage from "./pages/ReportPage";
import axios from "axios";

// todo ТОЧКА ВХОДА В ПРИЛОЖЕНИЕ(SPA - single page application)
const container = document.getElementById("root")!;
const root = createRoot(container);

// этот блок "вставляется" в блок id=root
root.render(
  // <React.StrictMode>
  //   <Provider store={store}>
  //   <MyApp/>,
  // virtual-router
  <Router>
    <Routes>
      <Route path="/" element={<HomePage />}></Route>
      <Route path="/home" element={<HomePage />}></Route>
      <Route path="/create" element={<CreateWorker />}></Route>
      <Route path="/list" element={<HomePage />}></Route>
      <Route path="/search" element={<HomePage />}></Route>
      <Route path="/chat" element={<ChatPage />}></Route>
      <Route path="/report" element={<ReportPage />}></Route>
    </Routes>
  </Router>,
  // <Apps />
  // </Provider>
  // </React.StrictMode>
);
