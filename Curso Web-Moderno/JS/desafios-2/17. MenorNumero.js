const menorNumero = (arrayc) => console.log(arrayc.reduce((acumulador, valorAtual, indice) => {
    if (indice == 0) { return valorAtual }
    else if (valorAtual < acumulador) { return valorAtual }
    else { return acumulador }
}))

menorNumero([10, 5, 35, 65]) // retornarĂ¡ 5
menorNumero([5, -15, 50, 3]) // retornarĂ¡ -15