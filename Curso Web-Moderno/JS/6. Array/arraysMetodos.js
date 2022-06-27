const pilotos = ['Vettel', 'Alonso', 'Raikkoen', 'Massa']

pilotos.pop() // Revoem o ultimo elemento
console.log(pilotos)

pilotos.push('Verstappen') // Adicione um elemeno na ultima posiçao
console.log(pilotos)

pilotos.shift() // Remove o primeiro elemento
console.log(pilotos)

pilotos.unshift('Hamilton') // Adiciona na primeira posiçao
console.log(pilotos)

// SPLICE
// Adicionar
pilotos.splice(2, 0, 'Bottas', 'Massa')
console.log(pilotos)

// Remover
pilotos.splice(3, 1)

const algunsPilotos = pilotos.slice(2) // Retorna um novo array
console.log(algunsPilotos)

const algunsPilotos2 = pilotos.slice(1, 4)
console.log(algunsPilotos2)