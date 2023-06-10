/**
 * PUBLIC
 * e visivel e pode ser acessado externamente (classe.atributo) (classe.atributo())
 *
 * PRIVATE
 * pode ser acessado apenas internamente (this.atributo)
 */

class Empresa {
  public readonly nome: string;
  private readonly colaboradores: Colaborador[] = [];
  protected readonly cnpj: string;

  constructor(nome: string, cnpj: string) {
    this.nome = nome;
    this.cnpj = cnpj;
  }

  adicionaColaborador(...colaboradores: Colaborador[]): void {
    colaboradores.forEach((colaborador) =>
      this.colaboradores.push(colaborador),
    );
  }

  mostraColaboradores(): void {
    console.log(this.colaboradores);
  }

  public pegarNome() {
    return this.nome;
  }
}

class Colaborador {
  constructor(
    public readonly nome: string,
    public readonly sobrenome: string,
  ) {}
}

const empresa1 = new Empresa("PumpKing", "11.111.111/0001-11");
const colaborador1 = new Colaborador("Lucas", "Winicius");
const colaborador2 = new Colaborador("Leonardo", "Soares");
const colaborador3 = new Colaborador("Maria", "Eduarda");
empresa1.adicionaColaborador(colaborador1, colaborador2, colaborador3);
console.log(empresa1);
console.log(empresa1.pegarNome(), empresa1.nome);
empresa1.mostraColaboradores();

export default "";
