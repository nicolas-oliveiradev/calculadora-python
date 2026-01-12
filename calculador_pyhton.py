#Biblioteca
import math

#Funções de Validação
def validador_numero(mensagem = 'Digite um valor: '):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Valor inválido. Digite apenas números.')


def validador_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Valor inválido. Digite apenas números inteiros.')
            

def validador_operacao(op, v1):
    while True:
        v2 = validador_numero('Digite o próximo valor: ')
        
        if op == 4 and v2 == 0:
            print('Valor inválido. O divisor não pode ser zero.')
            continue

        elif op == 7 and v1 < 0 and v2 % 2 == 0:
            print('Não existe raiz real para índice par de número negativo. Tente com outros valores!')
            continue
        
        return v2

#Funções das Operações
def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a / b

def exponenciacao(a,b):
    return a ** b

def radiciacao(a,b):
    return math.copysign(abs(a)**(1/b), a)

def raiz_quadrada(a):
    return a ** 0.5

def seno(a):
    return math.sin(a)

def cosseno(a):
    return math.cos(a)

#Operações

operacoes = {
    1: {
        "nome": "Soma",
        "func": soma,
        "args": 2,
        "simbolo": "+"
    },
    2: {
        "nome": "Subtração",
        "func": subtracao,
        "args": 2,
        "simbolo": "-"
    },
    3: {
        "nome": "Multiplicação",
        "func": multiplicacao,
        "args": 2,
        "simbolo": "X"
    },
    4: {
        "nome": "Divisão",
        "func": divisao,
        "args": 2,
        "simbolo": "%"
    },
    5: {
        "nome": "Exponenciação",
        "func": exponenciacao,
        "args": 2,
        "simbolo": "^"
    },
    6: {
        "nome": "Raiz Quadrada",
        "func": raiz_quadrada,
        "args": 1,
        "simbolo": "√"
    },
    7: {
        "nome": "Radiciação",
        "func": radiciacao,
        "args": 2,
        "simbolo": "√"
    },   
    8: {
        "nome": "Seno",
        "func": seno,
        "args": 1,
        "simbolo": "sen"
    },
    9: {
        "nome": "Cosseno",
        "func": cosseno,
        "args": 1,
        "simbolo": "cos"
    }
}


#Valor Inicial
v1 = validador_numero('Digite o primeiro valor: ')

#Laço
while True:

#Menu
    print("\nQual operação você deseja fazer:")
    for codigo, dados in operacoes.items():
        print(f"{codigo}. {dados['nome']}")

    op = validador_inteiro('Digite o número da operação desejada: ')

    if op not in operacoes:
        print("Operação inválida.")
        continue

    dados = operacoes[op]

    if dados["args"] == 2:
        v2 = validador_operacao(op, v1)
        v1 = dados["func"](v1,v2)
           
    else:
        v1 = dados["func"](v1)

    print(f'O resultado da operação é : {v1:.2f}!')

    sair = validador_inteiro(
    "Deseja fazer outra operação?\n"
    "0 - Sim\n"
    "1 - Não\n"
    "Digite: "
)
    if sair == 1:
        break

#Resultado final
print(f'Resultado final foi {v1:.2f}!')
