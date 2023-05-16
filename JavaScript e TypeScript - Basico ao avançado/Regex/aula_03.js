const { texto, arquivos } = require("./base");

/*
  + (opcional) 0 ou n    -> {0,}
  * (obrigatorio) 1 ou n -> {1,}
  ? (opcional) 0 ou 1    -> {0,1}
  {min, max}
    {10,}  - Minimo 10
    {,10}  - de 0 a 10
    {5,10} - de 5 a 10
    {10}   - Exatamente 10
*/

// const regExp = /Jo+ão+/gi
// console.log(texto.match(regExp))

const regExp1 = /\.jpe?g/gi
const _regExp1 = /\.jpe{0,}g/gi
arquivos.forEach(arquivo => {
    const match = arquivo.match(regExp1)
    match && console.log(`${arquivo} -> ${match}`)
})