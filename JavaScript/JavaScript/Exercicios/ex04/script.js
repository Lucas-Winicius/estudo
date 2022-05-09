function tabuada() {
    let numero = document.getElementById('txtn')
    let res = document.getElementById('resultado')
    let tab = document.getElementById('seltab')
    if (numero.value.length == 0) {
        alert('Por Favor, insira um numero')
    }else {
        let n = Number(numero.value)
        let c = 0
        tab.innerHTML = ''
        while(c <= 10) {
            let item = document.createElement('option')
            item.text = `${n} X ${c} = ${c*n}`
            item.value = `tab${c}`
            tab.appendChild(item)
            c++
        }
    }
}