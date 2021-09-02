class Teste:
    def __init__(self):
        self.__nome = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter #sempre tem que vir depois da property, ele tem que ter mais um paramentromalem do self Igal exemplo
    def nome(self, novo_nome):
        self.__nome = novo_nome
