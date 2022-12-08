const Pessoa = ({ url, descricao, nome, idade, profissao}) => {
    return (
        <div>
            <img src={url} alt={descricao || 'Imagem sem identificação'} />
            <h2>Nome: {nome}</h2>
            <p>Idade: {idade}</p>
            <p>Profissão: {profissao}</p>
        </div>
    )
}

export default Pessoa