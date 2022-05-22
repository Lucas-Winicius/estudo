const prod1 = {}

prod1.nome = 'Lucas'
prod1.apelido = 'Aboboran'
prod1['idade'] = 15


console.log(prod1)

const prod2 = {
    produto: 'Abobora',
    preco: 11.35,
    emEstoque: true,
    descontoMaximo: '2.50 - 5.00',
    code: null,
    estoqueInfo: {
        corredor: 'A02',
        prateleira: {
            inicio: 'C020',
            fim: 'N003'
        }
    }
}