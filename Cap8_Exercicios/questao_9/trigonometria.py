# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: 8.4.9
# Autor...: Givanaldo Rocha de Souza
# Data....: 02/05/2020

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