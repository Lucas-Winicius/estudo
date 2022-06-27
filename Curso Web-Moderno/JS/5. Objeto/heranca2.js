const avo = {atr1: 'A'}
const pai = {__proto__: avo, atr2: 'B'}
const filho = {__proto__: pai, atr3: 'C'}

console.log(filho.atr1)