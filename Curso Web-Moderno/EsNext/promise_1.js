// resolve( Primeiro Parametro ) ->> Promessa cumprida / Aceita
// reject( Segundo Parametro ) --->> Promessa rejeitada / ñ cumprida

let p = new Promise((resolve, reject) => {
    resolve(['Lucas', 'Maria', 'Leo', 'Rafael', 'Ana', 'Daniela'])
})

p.then((valorDaDevolucao) => { 
    console.log(valorDaDevolucao)
    return valorDaDevolucao
}).then(valor => valor.map(nome => console.log(nome)))