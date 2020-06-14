class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)} '

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    nicio = Mutante(nome='Nicio', idade='35')
    heloise = Pessoa(nicio, nome='Heloise', idade='29')
    print(Pessoa.cumprimentar(nicio))
    print(id(nicio))
    print(nicio.cumprimentar())
    print(nicio.nome)
    print(nicio.idade)
    for filho in heloise.filhos:
        print(filho.nome)
    print(heloise.__dict__)
    print(nicio.__dict__)
    print(nicio.olhos)
    print(heloise.olhos)
    print(Pessoa.metodo_estatico(), nicio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), nicio.nome_e_atributos_de_classe())
    print(nicio.olhos)
