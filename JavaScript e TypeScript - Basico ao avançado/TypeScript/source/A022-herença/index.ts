// + public
// - private
// # protected

export class Pessoa {
  constructor(
    public readonly nome: string,
    public readonly sobrenome: string,
    private readonly idade: number,
    protected readonly cpf: string,
  ) {}

  getIdade(): number {
    return this.idade;
  }

  getCPF(): string {
    return this.cpf;
  }

  getNomeCompleto(): string {
    return `${this.nome} ${this.sobrenome}`;
  }
}

export class Aluno extends Pessoa {
  getNomeCompleto(): string {
    return `Aluno: ${this.nome} ${this.sobrenome}`;
  }
}
export class Cliente extends Pessoa {
  getNomeCompleto(): string {
    return `Cliente: ${this.nome} ${this.sobrenome}`;
  }
}

const pessoa1 = new Pessoa("Lucas", "Winicius", 16, "111.111.111-11");
const aluno1 = new Aluno("Lucas", "Winicius", 16, "111.111.111-11");
const cliente1 = new Cliente("Lucas", "Winicius", 16, "111.111.111-11");
