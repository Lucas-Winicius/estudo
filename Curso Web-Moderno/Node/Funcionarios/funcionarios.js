const url = 'http://files.cod3r.com.br/curso-js/funcionarios.json'
const axios = require('axios')

axios.get(url).then(response => {
    const funcionarios = response.data
    console.log(funcionarios.filter((valor) => {
        if(valor.pais == 'China' && valor.genero == 'F') return true
    }).reduce((menorSalario, funcionarioAtual, indice) => {
        if(indice == 1) return funcionarioAtual
        if(funcionarioAtual.salario < menorSalario.salario) return funcionarioAtual
        else return menorSalario
    }))
})