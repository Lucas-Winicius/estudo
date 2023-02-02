const inputs = document.querySelectorAll('input')
const setarErro = (inputIndex, texto) => {
    const botao = document.querySelector('button')

    if(inputIndex == 0) {
        const erro = document.querySelector('#erroPeso')
        inputs[0].style.border = '2px solid red'
        document.body.style.backgroundColor = '#cc3300'
        erro.innerHTML = texto
        botao.style.backgroundColor = '#cc3300'
    }
    
    if(inputIndex == 1) {
        const erro = document.querySelector('#erroAltura')
        inputs[1].style.border = '2px solid red'
        document.body.style.backgroundColor = '#cc3300'
        erro.innerHTML = texto
        botao.style.backgroundColor = '#cc3300'
    }
}

const setarIMC = (texto, cor, corTexto = 'black') => {
    const displayIMC = document.querySelector("#exibirIMC")
    const botao = document.querySelector('button')

    document.body.style.backgroundColor = cor
    botao.style.backgroundColor = cor
    botao.style.color = corTexto
    displayIMC.innerHTML = texto
    displayIMC.style.backgroundColor = cor
    displayIMC.style.color = corTexto
    displayIMC.style.display = 'block'

}

const validarPeso = () => {
    const inputPeso = parseFloat(document.querySelector('#peso').value)

    if(!inputPeso) {
        setarErro(0, 'Insira um peso valido.')
        return;
    }
    
    if(inputPeso <= 0 || inputPeso > 600) {
        setarErro(0, 'Insira um numero entre 1 e 600')
        return;
    }

    return inputPeso
}

const validarAltura = () => {
    const inputAltura = parseFloat(document.querySelector('#altura').value)

    if(!inputAltura) {
        setarErro(1, 'Insira uma altura valida.')
        return;
    }
    
    if(inputAltura <= 0 || inputAltura > 3) {
        setarErro(1, 'Insira uma altura entre 0m e 3m')
        return;
    }

    return inputAltura

}

const calcularIMC = e => {
    e.preventDefault();
    const peso = validarPeso()
    const altura = validarAltura()

    if(!peso || !altura) return;

    const imc = peso / (altura * altura)

    console.log(imc)    

    if(imc <= 16.9) { setarIMC('muito abaixo do peso', '#ff3300', 'white') }

    else if (imc >= 17 && imc <=18.4) { setarIMC('Abaixo do peso', '#ffb700') }
    
    else if (imc >= 18.5 && imc <= 24.9) { setarIMC('Peso normal', '#005414', 'white') }
    
    else if (imc >= 25 && imc <= 29.9) { setarIMC('Acima do peso', '#e0fc05') }
    
    else if (imc >= 30 && imc <= 34.9) { setarErro('Obesidade grau 1', '#fc6805') }
    
    else if(imc >= 35 && imc <= 39.9) { setarIMC('Obesidade grau 2', '#fc3205', 'white') }
    
    else if (imc >= 40) { setarIMC('Obesidade grau 3', '#fc1505', 'white') }
    
    else { setarIMC('Erro ao calcular imc', 'red', 'white') }
    
}

addEventListener('submit', e => calcularIMC(e))

onchange = e => {
    document.body.style.backgroundColor = 'rgb(0, 95, 68)'
    document.querySelector('button').style.backgroundColor = 'rgb(0, 95, 68)'
    document.querySelector('button').style.color = 'white'
    document.querySelector('#exibirIMC').style.display = 'none'

    inputs.forEach(element => element.style.border = '2px solid gray');
    document.querySelectorAll('.erro').forEach(element => element.innerHTML = '')
}