function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.querySelector('div#res')

    if (fano.value.length == 0 || fano.value > ano) {
        alert('Verifique os dados e tente novamente!')
    }else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        var genero = ''

        if(fsex[0].checked) {
            genero = 'Homem'

            if (idade >= 0 && idade < 10) {
                // CRIANÇA
                img.setAttribute('src', 'Imagens/bebe-h.png')
            }else if (idade < 21) {
                // JOVEM
                img.setAttribute('src', 'Imagens/jovem-h.png')
            }else if (idade < 50) {
                // ADULTO
                img.setAttribute('src', 'Imagens/adulto-h.png')
            }else {
                // IDOSO
                img.setAttribute('src', 'Imagens/idoso-h.png')
            }
        }else if (fsex[1].checked) {
            genero = 'Mulher'

            if (idade >= 0 && idade < 10) {
                // CRIANÇA
                img.setAttribute('src', 'Imagens/bebe-m.png')
            }else if (idade < 21) {
                // JOVEM
                img.setAttribute('src', 'Imagens/jovem-m.png')
            }else if (idade < 50) {
                // ADULTO
                img.setAttribute('src', 'Imagens/adulto-m.png')
            }else {
                // IDOSO
                img.setAttribute('src', 'Imagens/idosa-m.png')
            }
        }

        res.innerHTML = `Detectamos ${genero} com ${idade} anos.`
        res.appendChild(img)
    }
}