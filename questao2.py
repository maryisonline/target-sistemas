# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# input que irá armazenar o numero escolhido pelo usuario
indice = int(input('Informe um número: '))

def fibonacci():
    # definicao inicial das variaveis de x e y
    x = 0
    y = 1
  
    # loop que executara enquanto o valor de x (que vira antes de y) for menor ou igual a 100
    while x <= 100:
            # condicional que, caso o numero armazenado seja igual a x ou igual a y, trará uma mensagem de sucesso e ira parar o programa
            if indice == x or indice == y: 
                print(f'O número {indice} pertence à sequência de Fibonacci.')
                break
            # caso nao encontre o numero informado ira prosseguir com o codigo atualizando o valor de x e y para a sequencia
            soma_sequencia = x + y
            x = y
            y = soma_sequencia
    # caso o loop termine sem acontecer um break, ira direto pro else informado
    else:
        print(f'O número {indice} não pertence à sequência.')   

# chama a funcao para ser executada
fibonacci()
