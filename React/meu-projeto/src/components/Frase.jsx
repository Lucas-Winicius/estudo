import styles from '../css/Frase.module.css'

const Frase = props => {
    return (
        <div className={ styles['frase-container'] }>
            <p className={ styles.fraseContent }>Este e um componente com uma frase!</p>
        </div>
    )
}

export default Frase