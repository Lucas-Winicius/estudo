const { texto } = require("./base");
// g  - Global ( Procure todas as ocorrencias );
// i  - Incensitive ( Ignora se e maiuscula ou minuscula );
// () - Grupos
// |  - OU

// const regExp = /Lucas/g;

// console.log(regExp.test(texto));

const regExp = /(Foi um ano excelente na vida de )(joão|maria|lucas)/g;
console.log(regExp.exec(texto))