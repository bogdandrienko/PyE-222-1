import React from "react";
import logo from "./logo.svg";
import { Counter } from "./features/counter/Counter";
import "./App.css";
import axios from "axios";

// js - JavaScript (слабая динамическая типизация)
// ts - TypeScript - расширение(+ типизация)
// jsx - React JS - библиотека(+- фреймворк)
// tsx - React JS + TypeScript

function App() {
  async function getData() {
    const response = await axios.get(
      // "https://jsonplaceholder.typicode.com/todos",
      "http://127.0.0.1:8000/api/",
    );
    console.log("response:", response.data);
  }

  return (
    <div className="App">
      <header className="App-header">
        <button className={""} onClick={getData}>
          getData
        </button>
      </header>
    </div>
  );
}

export default App;
