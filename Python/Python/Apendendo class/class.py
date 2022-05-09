# Class
# Sintaxe

class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video): # Consutor que permite criar a funcionalidade inicial que a sua classe tera
        self.marca = marca # PROPRIEDADE
        self.memoria_ram = memoria_ram # PROPRIEDADE
        self.placa_de_video = placa_de_video # PROPRIEDADE

    def Ligar(self): # METODO
        print('Estou ligando')

    def Desligar(self): # METODO
        print('Desligando...')

    def Exibir(self): # METODO
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador('Apple', '128gb', 'GeForce')
computador1.Ligar()
computador1.Desligar()
computador1.Exibir()