const timeBySeconds = seconds => new Date(seconds * 1000).toLocaleTimeString("pt-Br", { hour12: false, timeZone: "UTC" })
const iniciar = document.querySelector('.iniciar')
const pausar = document.querySelector('.pausar')
const zerar = document.querySelector('.zerar')
const tempo = document.querySelector('#tempo')
let timer;
let seconds = 0

const exibirTempo = () => {
    tempo.innerText = timeBySeconds(seconds)
}

const iniciarCronometro = () => {
    tempo.style.color = 'black'
    timer = setInterval(() => {
        seconds++
        exibirTempo()
    }, 1000)
}

const pausarCronometro = () => {
    clearInterval(timer)
    tempo.style.color = 'red'
}

const zerarCronometro = () => {
    clearInterval(timer)
    tempo.style.color = 'black'
    seconds = 0
    exibirTempo()
}

iniciar.addEventListener('click', () => iniciarCronometro())
pausar.addEventListener('click', () => pausarCronometro())
zerar.addEventListener('click', () => zerarCronometro())