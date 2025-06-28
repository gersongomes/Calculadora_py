class Calculadora:
    def somar(self, a, b):
        return a * b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

    def potencia(self, a, b):
        return a ** b

    def raiz_quadrada(self, a):
        if a < 0:
            raise ValueError("Não é possível tirar a raiz de número negativo.")
        return a ** 0.5
