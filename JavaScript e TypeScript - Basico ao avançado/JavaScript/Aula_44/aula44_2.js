function soma(x, y) {
    // if(typeof x !== 'number' || typeof y !== 'number') throw new Error('x e y precisam ser numeros')
    if(typeof x !== 'number' || typeof y !== 'number') throw new TypeError('x e y precisam ser numeros')

    return x + y
}

try {
    console.log(soma(1, 4))
    console.log(soma('1', 4))
} catch(e) {
    // console.log(e)
    console.log('Hove um erro interno tente novamente.')
}