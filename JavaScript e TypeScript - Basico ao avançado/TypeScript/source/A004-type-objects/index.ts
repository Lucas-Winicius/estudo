const objetoA: {
  chaveA: string;
  readonly chaveB: string;
  chaveC?: string;
  [key: string]: unknown;
} = {
  chaveA: "Valor A",
  chaveB: "Valor B",
  chaveC: "Valor C",
};

objetoA.chaveA = "Outro A";
objetoA.chaveC = "NOva Chave";
objetoA.chaveD = "NOva Chave";
