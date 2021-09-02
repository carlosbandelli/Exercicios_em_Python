# Programação Orientada a Objetos
# AC02 ADS-EaD - Implementação de classes
#
# Email Impacta: carlos.vieira@aluno.faculdadeimpacta.com.br

class Conta:
    def __init__(self, titular, agencia, numero, saldo_inicial):
        self.titular = titular
        self.agencia = agencia
        self.numero = numero
        self.saldo_inicial = 0
        self.operacoes = [('saldo inicial', saldo_inicial)]

    @property
    def titular(self):
        return self.titular

    @property
    def agencia(self):
        return self.agencia

    @property
    def numero(self):
        return self.numero

    @property
    def saldo(self):
        return self.__saldo_inicial

    @property
    def ativa(self):
        return self.ativo

    @ativa.setter
    def ativa(self, situacao):
        """
      Implemente o setter ativa
        """
        pass

    def depositar(self, valor):
        if valor <= 0:
            return 'Deposito acima de R$1.00'
        self.__saldo_inicial += valor
        return 'Deposito feito com sucesso'

    def sacar(self, valor):
        if valor < 0:
            return 'Valor dever ser positivo'
        if valor > self.__saldo_inicial:
            return 'Saldo Insuficiente'
        self.__saldo_inicial -= valor
        return 'Saque realizado com sucesso'

    def transferir(self, conta_destino, valor):
        if conta_destino != self.agencia:
            return 'Conta invalida'
        if valor <= 0:
            return 'Valor acima de R$1.00 por Transferencia'
        self.__saldo_inicial += valor

    def tirar_extrato(self):
        """
        Implemente o método tirar_extrato()
        """
        pass