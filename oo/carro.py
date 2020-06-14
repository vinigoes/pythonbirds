"""
Exemplo:

>>> #Testando motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0

"""

class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    @classmethod
    def acelerar(cls):
        motor.velocidade += 1
    @classmethod
    def frear(cls):
        motor.velocidade -= 2
        if motor.velocidade < 0:
            motor.velocidade = 0


class Direcao:
    def __init__(self, valor='Norte'):
        self.valor = valor


if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    direcao = Direcao()
    print(direcao.valor)

