function carro(velocidadeMaxima = 200, delta = 5) {
    // Atributo privado
    let = velocidadeAtual = 0

    // Metodo Publico
    this.acelerar = function() {
        if (velocidadeAtual + delta <= velocidadeMaxima) velocidadeAtual += delta
        else velocidadeAtual = velocidadeMaxima
    }

    // Metodo Publico
    this.getVelocidadeAtual = function() {
        return velocidadeAtual
    }
}

const uno = new carro
uno.acelerar()
console.log(uno.getVelocidadeAtual())

const ferrari = new carro(500, 25)
ferrari.acelerar()
ferrari.acelerar()
ferrari.acelerar()
ferrari.acelerar()
console.log(ferrari.getVelocidadeAtual())