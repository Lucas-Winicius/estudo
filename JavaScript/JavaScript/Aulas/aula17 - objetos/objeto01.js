let amigo = {nome:'Lucas', sexo:'M', peso:85.4, engordar(p=0) {
    this.peso += p
}}

amigo.engordar(3)
console.log(`${amigo.nome} pesa ${amigo.peso}Kg`)