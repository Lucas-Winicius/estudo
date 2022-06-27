let calc = (dividendo, divisor) => {
    return {
        resto: dividendo % divisor,
        resultado: dividendo / divisor
    }
}

function main(v1, v2) {
    const retorno = calc(v1, v2)

    console.log(`Resultado: ${retorno.resultado}`)
    console.log(`Resto: ${retorno.resto}`)
}

main(11, 2)