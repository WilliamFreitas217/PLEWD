import React, {Component} from 'react';
import './LoginScreen.css';
import uea from '../../Assets/plewd.png';

//App Components

//external components
import Global from '../../Components/global'
import { Link } from 'react-router-dom';


class LoginScreen extends Component{
    constructor(){
        super();
        this.state = {
            email: '',
            password : ''
        }
      }
      
      handleChange(evt) {
        if(evt.target.id === 'cpf'){
            this.setState({
                email : evt.target.value
            });
        }else{
            this.setState({
                password : evt.target.value
            });
        }
      }
    
      handleSubmit(evt) {
        if(!this.state.email || !this.state.password){
            alert('Login required!')
        } else {
            console.log()
            fetch(Global.API_URL + '/login', {
                headers : new Headers({
                    'Authorization': 'Basic '+btoa(this.state.email+':'+(this.state.password)),
                })
            })
            .then(function(response){
              return response.json();
            })
            .then(data => {
                console.log((this.state.password));
                console.log(data)
                if(data.canLogin){
                        sessionStorage.setItem('jwtToken', data.token);
                        this.props.history.push('/produtos')
                        console.log("LOGOU")
                    } else{
                        alert('Verifique as informações e tente novamente');
                    }
                })  
            .catch((e) => {
                    console.log(e);
                    alert('Houve um erro ao realizar o login, tente novamente mais tarde');
            });
        }     
        evt.preventDefault();
      }
  render(){
    return(
      <div>
        <header>
         
        </header>
        <div className='loginContainer'>
                    <div className="formLoginContainer">
                        {/* <form onSubmit={this.handleSubmit.bind(this)} className="formLogin"> */}
                        <div className="logoContainer">
                            <img className = "logo" src={uea}/>
                        </div>
                        <form>
                            <div className="cpfContainer inputContainer">
                                {/* <input className="input" id="cpf" placeholder="CPF" onChange={this.handleChange.bind(this)}/> */}
                                <input className="input-login" id="cpf" placeholder="Email" onChange={this.handleChange.bind(this)}/>
                                <span className=""></span>
                            </div>
                        
                            <div className="passwordContainer inputContainer">
                                {/* <input className="input" type="password" id="password" placeholder="Senha" onChange={this.handleChange.bind(this)}/> */}
                                <input className="input-login" type="password" id="password" placeholder="Senha" onChange={this.handleChange.bind(this)}/>
                                <span className=""></span>
                            </div>
                        
                            <div className="btnContainer">
                                <button onClick={this.handleSubmit.bind(this)}  className="btnLogin" type="submit">
                                    Entrar
                                </button>
                                <Link  variant="body2" onClick = {() => { window.open('http://localhost:3000/cadastro', '_self'); }}>
                                    Cadastre-se
                                </Link>
                            </div >
                                
                            <div className="btnContainer">
                                <Link to="/cadastro" >
                                </Link>
                            </div>
                        </form>
                    </div>
                </div>
          </div>    
    );
  }
  
}

export default LoginScreen;