import { useState } from "react"

export default () => {

    const [ email, setEmail ] = useState()
    const [ userEmail, setUserEmail ] = useState()

    const enviarEmail = e => {
        e.preventDefault()
        setUserEmail(email)
        console.log(userEmail)
    }

    const limparEmail = e => {
        setUserEmail(null)
    }

    return (
        <div>
            <h2>Cadastre o seu e-mail</h2>
            <form>
                <input type="email" name="" id="" placeholder="Digite seu e-mail..." onChange={e => setEmail(e.target.value)} />
                <button type="submit" onClick={enviarEmail}>Enviar</button>
                { userEmail && (
                    <div>
                        <p>O e-mail do usuario é: { userEmail }</p>
                        <button onClick={limparEmail}>Limpar e-mail</button>
                    </div>
                )}
            </form>
        </div>
    )

}