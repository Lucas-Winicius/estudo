const bissexto = (ano) => {
    ano = Number(ano)
    if(ano % 4 == 0 && ano % 100 != 0 || ano % 400 == 0) {
        console.log(`O ano ${ano} é bissexto!`)
    } else {
        console.log(`O ano de ${ano} não é bissexto!`)
    }
}

bissexto(2020) // retornará true
bissexto(2100) // retornará false, pois é múltiplo de 100 e não é múltiplo de 400
bissexto("2024")
bissexto("2025")