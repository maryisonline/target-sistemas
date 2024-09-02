# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0; Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } Imprimir(SOMA); Ao final do processamento, qual será o valor da variável SOMA?
# RESPOSTA: o valor da variável de SOMA é 91.

# funcao para deixar o calculo mais conciso, dentro dos parenteses estão as variaveis que serao utilizadas
def somatoria(indice, soma, k):
  # loop que ira realizar a soma enquanto K for menor que o INDICE
    while k < indice:
        k += 1
        soma += k
    # imprime a soma
    print(soma)
# chamando a funcao com os devidos valores designados no enunciado
somatoria(13, 0, 0)
