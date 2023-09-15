import React, { useState } from "react";
import axios from "axios";

function Input1() {
  const [form, setForm] = useState({ username: "умолчание" });
  return (
    <div>
      <div className={"card"}>
        <div className={"card-body"}>{form.username}</div>
        <div className={"card-header"}>
          <input
            type={"text"}
            onChange={(event) => setForm({ username: event.target.value })}
            value={form.username}
            className={"form-control"}
          />
        </div>
        <div className={"card-body"}>{form.username}</div>
      </div>
    </div>
  );
}

function Counter1({ value }: { value: number }) {
  const [getValue, setValue] = useState(value);
  function Increase() {
    setValue(getValue + 1);
  }
  function Decrease() {
    setValue(getValue - 1);
  }
  return (
    <div>
      <div className={"card"}>
        <div className={"card-header"}>
          <button onClick={Increase} className={"btn btn-lg btn-primary"}>
            increase
          </button>
        </div>
        <div className={"card-body"}>{getValue}</div>
        <div className={"card-footer"}>
          <button onClick={Decrease} className={"btn btn-lg btn-danger"}>
            decrease
          </button>
        </div>
      </div>
    </div>
  );
}

function Apps() {
  function old() {
    var val1 = 12; // устарело (она существует ещё до создания)
    let val2 = 333; // изменяемая
    const val3 = 12; // константа - не изменяемая

    function Decrease() {
      val2 = val2 - 1;
    }

    function ShowToConsole() {
      console.log(new Date(), val2);
    }
  }

  //  getter(берёт)   setter(устанавливает) default(стандарт)
  // const [getValue, setValue] = useState(1000); // object
  const [getValue, setValue] = useState(1000); // object
  function Decrease() {
    setValue(getValue - 1);
  }

  // @ts-ignore
  let data = [];
  const [data1, setData] = useState([]);

  async function getData() {
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/todos",
    );
    data = response.data;
    console.log(data);
    setData(response.data);
  }

  return (
    <div>
      <div className={"card"}>
        <div className={"card-header"}>
          <button onClick={Decrease} className={"btn btn-lg btn-primary"}>
            show
          </button>
        </div>
        <div className={"card-body"}>{getValue}</div>
        <div className={"card-footer"}>
          <button onClick={Decrease} className={"btn btn-lg btn-danger"}>
            decrease
          </button>
        </div>
        <button onClick={getData} className={"btn btn-lg btn-success"}>
          getData
        </button>
        <ul>
          {
            // @ts-ignore
            data1.map((item: any, index: number) => (
              <li key={item.id}>{item.title}</li>
            ))
          }
        </ul>
        22222222222
      </div>
      {/*<Counter1 value={777} />*/}
      {/*<Counter1 value={888} />*/}
      <hr />
      <hr />
      <hr />
      <hr />
      <hr />
      <hr />
      <Input1 />
    </div>
  );
}

function MyApp() {
  return <div className={"display-6"}>HELLO</div>;
}
