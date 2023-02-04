function criarCalculadora() {
    return {
        display: document.querySelector('.display'),
        btnClear: document.querySelector('.btn-clear'),

        inicia() {
            this.cliqueBotoes()
            this.pressionaEnter()
        },
        cliqueBotoes() {
            document.addEventListener('click', (e) => {
                const el = e.target
                
                if(el.classList.contains('btn-num')) {
                    this.btnParaDisplay(el.innerText)
                }

                if(el.classList.contains('btn-clear')) {
                    this.clearDisplay()
                }

                if(el.classList.contains('btn-del')) {
                    this.apagaUm()
                }

                if(el.classList.contains('btn-eq')) {
                    this.realizaConta()
                }

            })
        },
        pressionaEnter() {
            document.addEventListener('keyup', e => {
                if(e.key === 'enter') {
                    this.realizaConta()
                }
            })
        },
        btnParaDisplay(valor) {
            this.display.value += valor
        },
        clearDisplay() {
            this.display.value = ''
        },
        apagaUm() {
            this.display.value = this.display.value.slice(0, -1)
        },
        realizaConta() {
            let total = this.display.value
            
            try {
                total = eval(total)

                if(!total || typeof total !== 'number') {
                    throw 'Erro'
                }
                this.display.value = total
            } catch(err) {
                alert('Hove um erro!')
            }
            
        }
    }
}

const calculadora = criarCalculadora()
calculadora.inicia()