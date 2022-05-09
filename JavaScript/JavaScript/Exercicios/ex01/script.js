function carregar() {
    var msg = document.getElementById("msg")
    var img = document.getElementById("imagem")
    var texto = document.getElementById("texto")
    var data = new Date()
    var hora = data.getHours()

    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora <= 4) {
        //MADRUGADA
        img.src = 'imagens/madrugada.png'
        texto.innerHTML = '<p>Como esta sua <strong>Madrugada</strong>?</p>'
        document.body.style.background = '#0d1a2b'
    }else if (hora >= 0 && hora < 12) {
        // BOMDIA
        img.src = 'imagens/manha.png'
        texto.innerHTML = '<p>Bom Dia!</p>'
        document.body.style.background = '#61a9e1'
    }else if (hora >= 12 && hora < 18) {
        // BOATARDE
        img.src = 'imagens/tarde.png'
        texto.innerHTML = '<p>Boa Tarde!</p>'
        document.body.style.background = '#f27318'
    }else {
        //BOANOITE
        img.src = 'imagens/noite.png'
        texto.innerHTML = '<p>Boa Noite.</p>'
        document.body.style.background = '#20252b'
    }
}