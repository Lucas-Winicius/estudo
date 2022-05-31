// Estrategia 1 para gerar valores padrão

function soma1(a, b, c) {
    a = a || 1
    b = b || 1
    c = c || 1
    
    return a + b + c
}

console.log(`1: ${soma1()} 2: ${soma1(3)} 3: ${soma1(1, 2, 3)}`)

// Estrategia 2, 3 e 4 para gerar valor padrão
function soma2(a, b, c) {
    a = a !== undefined ? a : 1
    b = 1 in arguments ? b : 1
    c = isNaN(c) ? 1 : c
}

console.log(`1: ${soma2()} 2: ${soma2(3)} 3: ${soma2(1, 2, 3)}`)

function soma3 (a=1, b=1, c=1) {
    return a + b + c
}

console.log(`1: ${soma3()} 2: ${soma3(3)} 3: ${soma3(1, 2, 3)}`)