# 4) Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 

# numeros arrendondados para o float funcionar
sp = float('67.836')
rj = float('36.679')
mg = float('29.230')
es = float('27.165')
outros = float('19.850')

# somando todos os floats para ser o total da distribuidora, que equivale a 100% de representacao
distribuidora = sp + rj + mg + es + outros

# calculo do percentual
sp_perc = (sp/distribuidora) * 100
rj_perc = (rj/distribuidora) * 100
mg_perc = (mg/distribuidora) * 100
es_perc = (es/distribuidora) * 100
outros_perc = (outros/distribuidora) * 100

# imprime a mensagem convertendo para % e considerando somente uma casa decimal
print(f'O % de representação dos estados são aproximadamente SP: {sp_perc:.1f}%, RJ: {rj_perc:.1f}%, MG: {mg_perc:.1f}%, ES: {es_perc:.1f}% e Outros: {outros_perc:.1f}%')
