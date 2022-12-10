import Button from "./Button"

export default () => {

    const meuEvento = e => window.alert('Fui ativado!!')

    const segundoEvento = e => window.alert('Ativando segundo evento.')

    return (
        <div>
            <p>Clique para disparar um evento:</p>
            <Button event={meuEvento} text="Primeiro evento" />
            <Button event={segundoEvento} text="Segundo evento" />
        </div>
    )
    
}