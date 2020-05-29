import React, { Component } from 'react';
import logo from '../images/airplane.png';
import '../css/paginaInicial.css';
import { Link } from 'react-router-dom';
import Naveg from '../components/Naveg';

class paginaInicial extends Component {
  
  render() {
    return (
      <div>
        <Naveg/>
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Bem-vindo ao Bandeco's Aeroclube!</h1>
        </header>
      </div>
    );
  }
}

export default paginaInicial;
