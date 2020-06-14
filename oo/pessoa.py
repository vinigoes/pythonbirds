class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)} '



if __name__ == '__main__':
    nicio = Pessoa(nome='Nicio')
    heloise = Pessoa(nicio, nome='Heloise')
    print(Pessoa.cumprimentar(nicio))
    print(id(nicio))
    print(nicio.cumprimentar())
    print(nicio.nome)
    print(nicio.idade)
    for filho in heloise.filhos:
        print(filho.nome)

