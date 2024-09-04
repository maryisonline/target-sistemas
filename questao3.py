# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    # definindo uma variavel que le os dados do json em uma string
    dados_str = arquivo.read()
    # carrega a "leitura de string" do json
    dados = json.loads(dados_str)
# print(dados)

# para registrar o menor valor, é necessario ter como base o maior numero existente na base, por isso inf ao inves de -inf e vice-versa
menor = float('inf')
maior = float('-inf')

# acumulo por dia inicialmente sera 0 pois a cada iteração do loop for, ira acumular os valores
acumulo_valor_dia = 0
# dias faturados inicialmente tambem igual a 0
dias_faturados = 0

for dia in dados: # loop que ira percorrer todos os dias do loop
    valor = dia['valor']

    if valor > 0: # o codigo so ira considerar valores maior que zero, assim ignorando os dias zerados
        # atualiza o valor da variavel "menor" caso encontre um menor
        if valor < menor:
            menor = valor
        # atualiza o valor da variavel "maior" caso encontre um maior
        elif valor > maior:
            maior = valor
        acumulo_valor_dia += valor # ira acumular o valor do dia de acordo com as iterações e assim ira somar
        dias_faturados += 1 # como o loop esta ignorando os valores iguais a zero, entao ira somar de 1 em 1 os dias que possuem valores superiores

media_mesal = acumulo_valor_dia / dias_faturados # calculo da media mensal

faturamento_superior = 0 # definindo a qtd de dias acima como 0 para acumular no loop

for dia in dados: # loop para percorrer os dados e somar os dias em que o faturamento foi acima de media
    valor = dia['valor']
    if valor > media_mesal:
        faturamento_superior += 1 # se o valor do dia percorrido for acima da media, ira somar 1 dia no faturamento_superior e assim acumlando para a proxima iteração

print(f'O menor valor do faturamento em um dia do mês foi de R$ {menor:.2f}.\nO maior valor foi de R$ {maior:.2f}.\nQtd de dias que faturaram acima da média é de {faturamento_superior}.')
