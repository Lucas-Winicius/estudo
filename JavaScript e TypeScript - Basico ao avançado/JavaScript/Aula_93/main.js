class Pessoa {
    constructor(nome, sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.idade = 0;
    }

    passarAno() {
        this.idade++
    }

}

const p1 = new Pessoa('Lucas', 'Winicius')
for(let i = 0; i < 10; i++) p1.passarAno()
console.log(p1)