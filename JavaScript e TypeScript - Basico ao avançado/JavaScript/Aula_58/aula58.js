function Pessoa(nome, sobrenome) {
    // const/let cria uma variavel privada
    const id = 'kaj62sh7q8wgdyoqbwdqxxxdgjah'

    this.nome = nome;
    this.sobrenome = sobrenome;

    this.dizerNome = () => `Meu nome é: ${this.nome}`
}

const p1 = new Pessoa('Lucas', 'Winicius');
const p2 = new Pessoa('Leonardo', 'Henrique');
console.log(p2.dizerNome())