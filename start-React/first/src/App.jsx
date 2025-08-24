import { useState } from "react";

function App(){
  const [count, setCount] = useState(0);

 const Increase = ()=>{
  if(count < 10){
    setCount(count + 1)
  }
 };

 const Decrease = () => {
  if(count > 0){
    setCount(count - 1)
  }
 };

  

  return(
    <div style = {{textAlign : "center", marginTop : "50px"}}>
    <h1>React Counter</h1>
    <p>Count : {count}</p>
    <button onClick={Increase}>Increase</button>
    <button onClick={Decrease}>Decrease</button>
    </div>
  );
};

export default App;