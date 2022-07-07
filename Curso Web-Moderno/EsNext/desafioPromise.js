let fs = require('fs')

const lerArquivo = (caminho, codificacao='utf-8') => {
    
    return new Promise((resolve, reject) => {
        try {
            resolve(fs.readFileSync(caminho, codificacao))
        } catch (e) {
            reject({erro: e, mensagem: "Erro! Não foi possivel ler seu arquivo"})
        }
    })
}

lerArquivo('dado.txt').then(conteudo => console.log(conteudo)).catch(erro => console.log(erro.mensagem))
