function pessoa(nome) {
    this.nome = nome

    this.falar = function() {
        console.log(`Meu Nome É ${this.nome}`)
    }
}

const p1 = new pessoa('Lucas')
p1.falar()