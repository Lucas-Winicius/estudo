const contarCaractere = (letra, palavra) => {
    let letrasRepitidas = 0

    palavra.split('').forEach((letraAtual) => {
        if(letra === letraAtual) { letrasRepitidas++ }
    })

    console.log(letrasRepitidas)
}

contarCaractere("r", "A sorte favorece os audazes") // retornarĂ¡ 2
contarCaractere("c", "Conhece-te a ti mesmo") // retornarĂ¡ 1