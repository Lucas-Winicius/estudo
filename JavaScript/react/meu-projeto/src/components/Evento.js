function Evento({number}) {

    function meuEvento() {
        console.log(`Numero: ${number}`)
    }

    return (
        <div>
            <p>Clique Para disparar um evento</p>
            <button onClick={meuEvento}>Ativar!</button>
        </div>
    )
}

export default Evento