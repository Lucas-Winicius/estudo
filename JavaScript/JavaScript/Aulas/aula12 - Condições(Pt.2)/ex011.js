var idade = 67

if (idade < 16 ) {
    console.log('Não Vota')
}else {
    if (idade < 18){
        console.log('Voto opcional')
    }else {
        if ( idade >= 67) {
            console.log('Voto opcional')
        }else {
            console.log('Voto obrigatorio')
        }
    }
}