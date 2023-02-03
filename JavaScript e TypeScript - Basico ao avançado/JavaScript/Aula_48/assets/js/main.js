const inputTarefa = document.querySelector('.input-tarefa');
const btnTarefa = document.querySelector('.btn-tarefa');
const tarefas = document.querySelector('.tarefas');

const criarLI = () => document.createElement('li')

const reiniciarInput = input => {
    input.value = ''
    input.focus()
}

const criarBotaoApagar = li => {
    const botaoApagar = document.createElement('button')
    botaoApagar.innerText = 'Apagar'
    botaoApagar.setAttribute('class', 'apagar')
    botaoApagar.setAttribute('title', 'Apagar esta tarefa')
    li.innerText += '    '
    li.appendChild(botaoApagar)
}

const salvarTarefas = () => {
    const liTarefas = tarefas.querySelectorAll('li')
    const listaDeTarefas = []

    liTarefas.forEach(tarefa => {
        let tarefaTexto = tarefa.innerText
        tarefaTexto = tarefaTexto.replace('Apagar', '').trim()
        listaDeTarefas.push(tarefaTexto)
    })

    const tarefasJSON = JSON.stringify(listaDeTarefas)
    localStorage.setItem('tarefas', tarefasJSON)

}

const criarTarefa = tarefa => {
    const li = criarLI()
    li.innerText = tarefa
    tarefas.appendChild(li)
    reiniciarInput(inputTarefa)
    criarBotaoApagar(li)
    salvarTarefas()
}

const adicionarTarefasSalvas = () => {
    const tarefas = localStorage.getItem('tarefas')
    const listaDeTarefas = JSON.parse(tarefas)

    listaDeTarefas.forEach(tarefa => criarTarefa(tarefa))

}

btnTarefa.addEventListener('click', e => {
    if(!inputTarefa.value) return;
    criarTarefa(inputTarefa.value)
})

inputTarefa.addEventListener('keypress', e => {
    if(!inputTarefa.value) return;
    if(e.keyCode === 13) criarTarefa(inputTarefa.value)
})

document.addEventListener('click', e => {
    const el = e.target
    if(!el.classList.contains('apagar')) return;
    el.parentElement.remove()
    salvarTarefas()
})

adicionarTarefasSalvas()