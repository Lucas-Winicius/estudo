const repetir = (conteudo, NdeRepiticoes) => {
    let retorno = []
    for(NdeRepiticoes; NdeRepiticoes > 0; NdeRepiticoes--) {
        retorno.push(conteudo)
    }
    console.log(retorno)
}

repetir('Abobora', 5)
repetir(6, 6)