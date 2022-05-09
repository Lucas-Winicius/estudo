import { useState } from 'react'

function Form() {

    function CadastrarUsuario(e) {
        e.preventDefault()
        console.log(`Usuario cadastrado`)
        console.log(`Nome: ${name}`)
        console.log(`Senha: ${passworld}`)
    }

    const [name, setName] = useState()
    const [passworld, setPassworld] = useState()

    return (
        <div>
            <h1>Meu cadastro</h1>
            <form onSubmit={CadastrarUsuario}>
                <div>
                    <label htmlFor="nome">Nome:</label>
                    <input id="nome" type="text" placeholder="Digite o seu nome" onChange={(e) => setName(e.target.value)} />
                </div>

                <div>
                    <label htmlFor="senha">Senha:</label>
                    <input id="senha" type="passworld" placeholder="Digite a sua senha" onChange={(e) => setPassworld(e.target.value)} />
                </div>

                <div>
                    <input type='submit' value='Cadastrar' />
                </div>

            </form>
        </div>
    )   
}

export default Form