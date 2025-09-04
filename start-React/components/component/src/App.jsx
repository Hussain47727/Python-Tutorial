import { useState } from 'react'
import './App.css'
import Profile from './Profile'



function App() {

  return (
  <div className="main">
    <Profile name = 'jhon' age = '19' Bios = 'hello iam israr hussain'/>
    <Profile name = 'ibrahim' age = '18' Bios = 'what a shit'/>
    <Profile name = 'yawer' age = '21' Bios = 'are you listning me'/>

    
  </div>    
  )
}

export default App
