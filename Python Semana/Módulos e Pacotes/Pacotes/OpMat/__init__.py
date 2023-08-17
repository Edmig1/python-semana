import random
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida."

def potencia(base, expoente):
    return base ** expoente

def raiz_quadrada(numero):
    if numero >= 0:
        return numero ** 0.5
    else:
        return "Número negativo não possui raiz real."

def media(*numeros):
    return sum(numeros) / len(numeros)

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def area_retangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return 0.5 * base * altura

def hipotenusa(cateto_a, cateto_b):
    return (cateto_a ** 2 + cateto_b ** 2) ** 0.5


def area_quadrado(lado):
    print(lado ** 2)
def area_circulo(raio):
    print(3.14*(raio*raio))

def volume_cubo(aresta):
    return aresta ** 3

def juros_simples(capital, taxa, tempo):
    juros = capital * taxa * tempo
    montante = capital + juros
    return juros, montante


def juros_compostos(capital, taxa, tempo):
    montante = capital * (1 + taxa) ** tempo
    juros = montante - capital
    return juros, montante
def celsius_farenheit(c):
    print(f"{c*1.8+32} Graus Farenheit")
def farenheit_celsius(f):
    print(f"{(f-32)/1.8} Graus Farenheit")
def imposto_renda(n1):
    while n1<1903.99:
        print('Salário muito baixo, insira um valor maior que R$ 1903.99')
        n1 = float(input('Diga o salario bruto: '))
    if n1>=1903.99 and n1<=2826.65:
        print(f'O salário Líquido é: {n1*0.925}')
    elif n1>=2826.66 and n1<=3751.05:
        print(f'O salário Líquido é: {n1*0.85}')
    elif n1>=3751.06 and n1<=4664.68:
        print(f'O salário Líquido é: {n1*0.775}')
    elif n1>4664.68:
        print(f'O salário Líquido é: {n1*0.725}')
def ICMS(n1):
    print(f'O valor do produto é: {n1*0.830}')
def dados(a):
    i=0
    if a == 1:
        i = random.randint(1,6)
    if a == 2:
        i = random.randint(1,20)
    if a == 3:
        i = random.randint(1,100)
    print(i)