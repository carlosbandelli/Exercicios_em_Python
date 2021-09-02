class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo


    def depositar(self, valor):
        if valor <0:
            return 'valor deve ser posito'
        self.__saldo += valor
        return 'Deposito realizado com sucesso'

    def sacar(self,valor):
        if valor <0:
            return 'valor deve ser posito'
        if valor > sel.__saldo
            return 'Saldo insuficiente'
        self.__saldo -= valor
        return 'Saque realizado com sucesso'

