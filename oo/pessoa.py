class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)} '

if __name__ == '__main__':
    nicio = Pessoa(nome='Nicio', idade='35')
    heloise = Pessoa(nicio, nome='Heloise', idade='29')
    print(Pessoa.cumprimentar(nicio))
    print(id(nicio))
    print(nicio.cumprimentar())
    print(nicio.nome)
    print(nicio.idade)
    for filho in heloise.filhos:
        print(filho.nome)
    nicio.olhos = 3
    print(heloise.__dict__)
    print(nicio.__dict__)
    print(nicio.olhos)
    print(heloise.olhos)