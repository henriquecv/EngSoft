import React, { Component } from 'react';
import MaskedInput from 'react-text-mask'
import '../css/Ficha_Cadastro.css';


class Busca_Alterar_Instrutor extends Component {
    constructor(props){
        super(props);
        this.handleEmailChange=this.handleEmailChange.bind(this)
        this.handleTelefoneChange=this.handleTelefoneChange.bind(this)
        this.handleEnderecoChange = this.handleEnderecoChange.bind(this)
    }
    
    handleEmailChange(e) {
        this.props.onEmailChange(e.target.value);
    }
    
    handleEnderecoChange(e) {
        this.props.onEnderecoChange(e.target.value);
    }
    
    handleTelefoneChange(e) {
        this.props.onTelefoneChange(e.target.value);
    }

    render() {
        return (
            <div className='Ficha'>
                    <label>Nome</label><br/>
                    <input disabled  type="text" name="nome" value={this.props.nome}></input><br/>
                    <label>Número de Cadastro</label><br/>
                    <input disabled  type="text" name="nome" value={this.props.num_cadastro}></input><br/>
                    <label>E-mail</label><br/>
                    <input type="text" name="email" value={this.props.email} onChange={this.handleEmailChange}></input><br/>
                    <label>CPF (apenas números)</label><br/>
                    <input disabled type="text" name="cpf" value={this.props.cpf}></input><br/>
                    <label>Data de nascimento (dd/mm/yyyy)</label><br/>
                    <input disabled type="text" name="dataNascimento" value={this.props.dataNascimento}></input><br/>
                    <label>Endereço</label><br/>
                    <input type="text" name="endereco" value={this.props.endereco} onChange={this.handleEnderecoChange}></input><br/>
                    <label>Telefone</label><br/>
                    <input type="text" name="telefone" value={this.props.telefone} onChange={this.handleTelefoneChange}></input><br/>
                    <label>Breve</label><br/>
                    <input disabled type="text" name="telefone" value={this.props.breve}></input><br/>
                    <label>Status</label><br/>
                    <input disabled type="text" name="telefone" value={this.props.status}></input><br/>
            </div>
        );
    }
}

export default Busca_Alterar_Instrutor;


/*               
                 <MaskedInput
                    type="text"
                    mask={[ /\d/, /\d/, /\d/, '.',  /\d/, /\d/, /\d/, '.', /\d/, /\d/, /\d/, '-', /\d/, /\d/]}
                    name="cpf"
                    onChange={this.handleCpfChange}
                    /><br/>
                <MaskedInput
                    type="text"
                    mask={[ '(', /\d/ , /\d/,')', ' ', /\d/, /\d/,/\d/, /\d/, /\d/, '-',  /\d/, /\d/, /\d/, /\d/]}
                    name="telefone"
                    onChange={this.handleTelefoneChange}
                    /><br/> */ 