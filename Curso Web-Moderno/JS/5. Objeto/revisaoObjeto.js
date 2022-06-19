const produto = new Object

produto.nome = 'Cadeira'
produto['Marca Do Produto'] = 'Generica'
produto.preco = 220

console.log(produto)
delete produto.preco
delete produto['Marca Do Produto']
console.log(produto)

const carro = {
    modelo: 'A4',
    valor: 89000,
    proprietario: {
        nome: 'Raul',
        idade: 56,
        endereco: {
            logadouro: 'rua ABC',
            numero: 123
        }
    },
    condutores: [{
        nome: 'Junior',
        idade: 19
    }, {
        nome: 'ana',
        idade: '19'
    }],
    calcularValorSeguro: function() {
        // ...
    }
}

console.log(carro.proprietario.endereco.numero)
console.log(carro['proprietario']['endereco']['numero'])