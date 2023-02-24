class Pessoa {
    constructor(nome, sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
    }

    falar() {
        console.log(this.nome + ' Esta falando.')
    }

    comer() {
        console.log(this.nome + ' Esta comendo.')
    }

    beber() {
        console.log(this.nome + ' Esta bebendo.')
    }
}

const p1 = new Pessoa('Lucas', 'Winicius')