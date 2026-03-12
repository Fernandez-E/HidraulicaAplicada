from barragens import estabilidade_deslizamento, estabilidade_tombamento

tipo = 'retangular'
p_e_barragem = 2.5
p_e_agua = 1.0
h = 3
l = 6
coef_tracao = 0.7 
base = 2.5
altura = 5.0
coef_seguranca = 1.2

empuxo, peso = estabilidade_deslizamento(tipo, p_e_barragem, p_e_agua, h, l, coef_tracao, base, altura, coef_seguranca)
estabilidade_tombamento(empuxo, peso, tipo, p_e_barragem, p_e_agua, h, l, coef_tracao, base, altura, coef_seguranca)