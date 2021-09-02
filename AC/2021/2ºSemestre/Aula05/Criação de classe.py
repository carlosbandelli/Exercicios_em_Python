class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.editora = ''
    def identidade(self):
        return(f'Sou o livro {self.nome}, e estou salvo'
               f'no endero de memoria: {id(self)}')

livro_1 = Livro('O Senhor dos Aneis', 'J.R.R. Tolkien')
livro_2 = Livro('O Processo', 'Franz Kafka')

print('livro 1: ', vars(livro_1)) #vars serve para vizualizar os valores dos atributos
print(livro_1.nome) # Dessa forma voce acesso o conteudo do atributo
print(livro_1.autor)
print('livro 2: ', vars(livro_2))
print(livro_2.nome)
print(livro_2.autor)
livro_2.identidade()