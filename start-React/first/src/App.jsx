// import { useState } from "react";

// function App(){
//   const [count, setCount] = useState(0);

//  const Increase = ()=>{
//   if(count < 10){
//     setCount(count + 1)
//   }
//  };

//  const Decrease = () => {
//   if(count > 0){
//     setCount(count - 1)
//   }
//  };

  

//   return(
//     <div style = {{textAlign : "center", marginTop : "50px"}}>
//     <h1>React Counter</h1>
//     <p>Count : {count}</p>
//     <button onClick={Increase}>Increase</button>
//     <button onClick={Decrease}>Decrease</button>
//     </div>
//   );
// };

import { useState } from "react";

function Welcome(){
  return(
    <h1>This is my first component !</h1>
  )
}

function React(){
  return(
    <h1>Welcome back boss</h1>
  )
}

function Man(props){
  return(
    <div>
      <p>hello iam {props.name}</p>
      <p>iam {props.age} years old</p>
      <p>i study in class {props.class}</p>
      <p>now i start learning {props.course}</p>
    </div>
    
  )
}


function App(){
  return(
    <>
    <Welcome/>
    <React/>
    <Man name='israr' age='20' class='thirdyear' course='React '/>
    </>
  )
}




export default App;