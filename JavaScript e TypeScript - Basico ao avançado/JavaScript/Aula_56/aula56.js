// Funções contrutoras
const criaPessoa = (nome, sobrenome, altura, peso) => {
    return {
        nome,
        sobrenome,
        altura,
        peso,
        fala(assunto) {
            return `${this.nome} esta falando sobre ${assunto}...`
        },
        imc() {
            return this.peso / (this.altura ** 2)
        },
        get imc2() {
            return this.peso / (this.altura ** 2)
        },
        get nomeCompleto() {
            return `${this.nome} ${this.sobrenome}`
        },
        set nomeCompleto(vetor) {
            vetor = vetor.split(' ')
            this.nome = vetor.shift()
            this.sobrenome = vetor.join(' ')
        }
    }
}

const p1 = criaPessoa('Lucas', 'Winicius', 1.69, 70)
console.log(p1.fala('Desenvolvimento'))
console.log(p1.imc())
console.log(p1.imc2)
p1.nomeCompleto = 'Alberto souza silva'
console.log(p1.nomeCompleto)