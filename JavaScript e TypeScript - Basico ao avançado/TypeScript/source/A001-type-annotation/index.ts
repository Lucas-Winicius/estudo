/* eslint-disable */

let nome: string = "Lucas";
let idade: number = 16;
let adulto: boolean = false;

// Array
let arrayDeNumeros1: number[] = [];
let arrayDeNumeros2: Array<number> = [];

let arrayDeStrings1: string[] = [];
let arrayDeStrings2: Array<string> = [];

// Objetos
let pessoa: { nome: string, idade: number, adulto?: boolean} = { nome: "Lucas", idade: 16 }
console.log(pessoa.nome)

// Funções
function soma(x: number, y: number): number {
    return x + y;
}
console.log(soma(2, 3))

const soma2: (x: number, y: number) => number = (x, y) => x + y;
