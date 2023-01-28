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

}

const calcularIMC = e => {
    e.preventDefault();
    const peso = validarPeso()
    const altura = validarAltura()
}

addEventListener('submit', e => calcularIMC(e))