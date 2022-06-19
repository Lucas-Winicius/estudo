const obj1 = {}
const obj2 = new Object

// Funções Construtoras
function produto(nome, preco, desc) {
    this.nome = nome
    this.getPrecoComDesconto = () => {
        return preco * (1 - desc)
    }
}

const p1 = new produto('Abobora', 13.13, 0.15)
console.log(p1)
p1.nome = 'tang'
console.log(p1)

// Função Factory
function criarFuncionario(nome, salarioBase, faltas) {
    return {
        nome,
        salarioBase,
        faltas,
        getSalario() {
            return (salarioBase / 30) * (30 - faltas)
        }
    }
}

const f1 = criarFuncionario('Lucas', 13000, 2)
const f2 = criarFuncionario('João', 5000, 5)
console.log(f1.getSalario())
console.log(f2.getSalario())