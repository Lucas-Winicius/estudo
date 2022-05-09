# CRIAR UMA CLASSE CARRO MINIMO 3 PROPRIEDADES E 3 METODOS

class carro():
    def __init__(self, marca, ano, capacidade, cor):
        self.marca = marca
        self.ano = int(ano)
        self.capacidade = int(capacidade)
        self.cor = cor
    
    def belo(self):
        if self.cor == 'Preto':
            print('Belo carro')
        else:
            print('Gostei.')
    
    def idade(self):
        if self.ano < 2015:
            print('Carro velho')
        else:
            print('Carro novo')
    
    def tanto(self):
        if self.capacidade < 4:
            print('Carro pequeno')
        else:
            print('Que grande')

carro1 = carro('Ford', '2022', '2', 'Preto')
carro1.belo()
carro1.idade()
carro1.tanto()