const simboloMais = n => {
    let retorno = ''
    for(n; n > 0; n--) {
        retorno += '+'
    }
    console.log(retorno)
}

simboloMais(9)
simboloMais(1)
simboloMais(0)