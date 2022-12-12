const criarSaudacao = nome => `Olar, ${nome || 'Vazio'}. Como vai?`

export default ({nome}) => <>{nome && <p>{criarSaudacao(nome)}</p>}</>