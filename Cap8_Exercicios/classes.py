# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Autor...: Givanaldo Rocha de Souza
# Data....: 30/04/2020
# Comentário: Este arquivo contém todas as classes dos exercícios propostos do Capítulo 08 na ordem em que sáo usadas

class Ingresso:
    def __init__(self, evento, valor):
        self.evento = evento
        self.valor = valor

    def exibirValor(self):
        return self.valor

    def __str__(self):
        return (f"{self.evento}: R$ {self.valor:.2f}")


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularPerimetro(self):
        return 2 * self.largura + 2 * self.altura

    def calcularArea(self):
        return self.largura * self.altura


class Ponto():
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y

    def __str__(self):
        return (f"{self.nome}: ({self.x}, {self.x})")


class Lista():

    def __init__(self, itens):
        self.itens = itens

    def exibirListaDistinta(self):
        novaLista = []
        for item in self.itens:
            if item not in novaLista:
                novaLista.append(item)
        return novaLista


class Calculadora():
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def somar(self):
        return self.op1 + self.op2

    def subtrair(self):
        return self.op1 - self.op2

    def multiplicar(self):
        return self.op1 * self.op2

    def dividir(self):
        return self.op1 / self.op2

    def potencia(self):
        return self.op1 ** self.op2


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, porcentagem):
        return self.salario + (self.salario * porcentagem / 100)


class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def abastecer(self,litros):
        self.combustivel += litros

    def exibirCombustivel(self):
        print(f'Combustível: {self.combustivel:.1f} litros')

    def andar(self, distancia):
        print(f"Carro andou {distancia} Km")
        litrosGastos = distancia / self.consumo
        self.combustivel -= litrosGastos


class ContaInvestimento:
    def __init__(self, saldo, taxaJuros):
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def adicionarJuros(self):
        self.saldo += (self.saldo * self.taxaJuros / 100)


from math import radians, sin, cos, tan

class Trigonometria:

    def __init__(self, angulo):
        self.anguloGraus = angulo
        self.anguloRad = radians(angulo)

    def seno(self):
        return sin(self.anguloRad)

    def cosseno(self):
        return cos(self.anguloRad)

    def tangente(self):
        return tan(self.anguloRad)

    def __str__(self):
        return "\n- Ângulo em graus: %d \n" \
               "- Ângulo em radianos: %f \n" \
               "- Seno: %f \n" \
               "- Cosseno: %f \n" \
               "- Tangente: %f " \
               % (self.anguloGraus, self.anguloRad, self.seno(),
                  self.cosseno(), self.tangente())


# Como já existe a classe Ponto (questão 3), foi criada a classe PontoModificado para a questão 10
class PontoModificado():
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y

    def distancia(self, p):
        from math import sqrt
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def __str__(self):
        return ("%s: (%d, %d)" % (self.nome, self.x, self.y))
