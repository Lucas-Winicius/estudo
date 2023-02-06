const obj1 = {}
const obj2 = new Object

function Pessoa(nome, sobrenome) {
    this.nome = nome
    this.sobrenome = sobrenome

    Object.freeze(this)
}

const p1 = new Pessoa('Lucas', 'Winicius')
const p2 = new Pessoa('Leonarrdo', 'Henrique')