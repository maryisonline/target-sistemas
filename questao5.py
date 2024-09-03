# 5) Escreva um programa que inverta os caracteres de um string.

# variavel para armazenar o input
string = input('Digite qualquer coisa: ')

# funcao
def inverte_str():
    # essa variavel esta a principio fora do loop e vazia porque ira armazenar o primeiro valor
    inverter = ''
    # percorre cada caractere do input:
    for caractere in string:
        # ira atualizar o valor de inverter, que passa a ser o caractere percorrido + o valor do inverter mais atual
        inverter = caractere + inverter
    # imprime como a palavra fica invertida
    print(inverter)
# chama a funcao para ser executada
inverte_str()
