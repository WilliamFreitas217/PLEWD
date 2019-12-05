import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

import {BrowserRouter, Switch, Route } from 'react-router-dom';
import Lista from './Screens/Lista/Lista';
import Footer from './Components/Footer/Footer';
import Product from './Screens/Produtos/Produtos';
import Menu from './Components/Menu/Menu';
import SignUp from './Screens/RegisterScreen/RegisterScreen';
import LoginScreen from './Screens/Login/LoginScreen';
import NewProduct from './Screens/RegisterProduct/newProduct';
import Perfil from './Screens/Perfil/Perfil';
import Edit from './Screens/EditRegister/Edit';
import EditProduct from './Screens/EditProduct/EditProduct';
import ProdutoPerfil from './Screens/ProdutoPerfil/ProdutoPerfil';

import UploadButtons from './Components/UploadButton/Upload';

ReactDOM.render(
    <BrowserRouter>
      <Switch>
      <Route path='/footer' exact={true} component={Footer}/>
      <Route path='/produtos' exact={true} component={Product}/>
      <Route path='/inventario' exact={true} component={Lista}/>
      <Route path='/cadastro' exact={true} component={SignUp}/>
      <Route path='/menu' exact={true} component={Menu}/>
      <Route path='/upload' exact={true} component={UploadButtons}/>
      <Route path='/novo' exact={true} component={NewProduct}/>
      <Route path='/perfil' exact={true} component={Perfil}/>
      <Route path='/editarc' exact={true} component={Edit}/>
      <Route path='/editarp' exact={true} component={EditProduct}/>
      <Route path='/produtoperfil' exact={true} component={ProdutoPerfil}/>
      <Route path='/' exact={true} component={LoginScreen}/>
      </Switch>
    </BrowserRouter>,
  document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
