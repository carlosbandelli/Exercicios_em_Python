class Conta:

    def __init__(self, numero,titular,saldo,limite):
        print(f'Construindo objeto... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print(f'Saldo {self.saldo} do titular {self.titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")

    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)



    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def saldo(self):
        return self.__saldo

    @limite.setter
    def limite(self,limite):
        self.__limite = limite

    @staticmethod
    def codigo_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
