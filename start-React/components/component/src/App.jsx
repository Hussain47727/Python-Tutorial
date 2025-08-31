import { useState } from 'react'
import './App.css'
import Header from './Header'
import Footer from './Footer'
import Card from './Card'


function App() {

  return (
  <div className="main">
    <Header/>
    <Footer/>
    <Card Name = 'Ali' Age = '22'/>
    <Card Name = 'Sara' Age = '19'/>
    <Card Name = 'Israr' Age = '25'/>
  </div>    
  )
}

export default App
