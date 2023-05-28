const dadosCliente1: [number, string] = [15, "Lucas"];
const dadosCliente2: [number, string, string] = [15, "Lucas", "Winicius"];
const dadosCliente3: [number, string, string?] = [15, "Lucas", "Winicius"];
// const dadosCliente4: [number, string, ...string[]] = [15, "Lucas", "Winicius"];
const dadosCliente4: [number, ...string[]] = [15, "Lucas", "Winicius"];
const dadosCliente5: readonly [number, string] = [15, "Lucas"];

dadosCliente1[0] = 16;
dadosCliente1[1] = "Lucas W.";

console.log(dadosCliente1);
console.log(dadosCliente2);
console.log(dadosCliente3);
console.log(dadosCliente4);
console.log(dadosCliente5);
