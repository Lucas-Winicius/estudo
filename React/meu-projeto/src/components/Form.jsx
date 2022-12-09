import { useState } from "react"

export default () => {

    const cadastrarUsuario = e => {
        e.preventDefault()
        console.log('Usuario cadastrado com sucesso!')
        console.log(`Usuario: ${name}`)
        console.log(`Senha: ${password}`)
    }

    const [ name, setName ] = useState('Guest')
    const [ password, setPassword ] = useState()

    return (
        <div>
            <h1>Meu Cadastro:</h1>
            <form onSubmit={cadastrarUsuario}>
                <div>
                    <label htmlFor="name" />Nome:<label />
                    <input
                        type='text'
                        id="name"
                        name="name"
                        placeholder="Digite seu nome"
                        onChange={e => setName(e.target.value)}
                        value={name} />
                </div>
                <div>
                    <label htmlFor="password">Senha:</label>
                    <input
                        type='password'
                        id="password"
                        name="password"
                        placeholder="Digite sua senha"
                        onChange={e => setPassword(e.target.value)} />
                </div>
                <div>
                    <input type='submit' value="Cadastrar" />
                </div>
            </form>
        </div>
    )

}