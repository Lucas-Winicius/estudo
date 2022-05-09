function tabuada() {
    let numero = document.getElementById('txtn')
    let res = document.getElementById('resultado')
    let tab = document.getElementById('seltab')
    if (numero.value.length == 0) {
        alert('Por Favor, insira um numero')
    }else {
        let n = Number(numero.value)
        let c = -1
        while(c != 10) {
            let item = document.createElement('option')
            c += 1
            if(c == 0) {
                res.innerHTML = `<p>${n} X ${c} = ${n*c}</p>`
            }else {
                res.innerHTML += `<p>${n} X ${c} = ${n*c}</p>`
            }
            
            
        }
    }
}

//tabuada sem o option