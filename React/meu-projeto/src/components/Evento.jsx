export default ({ numero }) => {

    const meuEvento = e => window.alert('Fui ativado!! Numero: ' + numero)

    return (
        <div>
            <p>Clique para disparar um evento:</p>
            <button onClick={meuEvento}>Ativar!</button>
        </div>
    )
    
}