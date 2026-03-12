def estabilidade_deslizamento(tipo_barragem, peso_especifico_barragem, peso_especifico_agua, carga_hidraulica, largura, coeficiente_tracao, base, altura, coeficiente_seguranca):
    
    if tipo_barragem == 'retangular':
        volume = base * altura * largura
        print(f'Volume da barragem: {volume:.2f} m3')
        
        peso = volume * peso_especifico_barragem
        print(f'Peso da barragem: {peso:.2f} tf')
        
        empuxo = (peso_especifico_agua*carga_hidraulica**2)*largura/2
        print(f'Empuxo: {empuxo:.2f} tf')
        
        atrito = coeficiente_tracao*peso
        print(f'Atrito: {atrito:.2f} tf')
        

    if empuxo * coeficiente_seguranca < atrito:
        print(f'Empuxo ({empuxo * coeficiente_seguranca:.2f} tf) < Atrito ({atrito:.2f} tf)')
        print('A barragem esta segura quanto ao deslizamento')
    else:
        print(f'Empuxo ({empuxo * coeficiente_seguranca:.2f} tf) > Atrito ({atrito:.2f} tf)')
        print('A barragem nao e segura quanto ao deslizamento')
    
    return empuxo, peso

def estabilidade_tombamento(empuxo, peso, tipo_barragem, peso_especifico_barragem, peso_especifico_agua, carga_hidraulica, largura, coeficiente_tracao, base, altura, coeficiente_seguranca):
    if tipo_barragem == 'retangular':  
        
        print(f'Peso da barragem: {peso:.2f} tf')  
        print(f'Empuxo: {empuxo:.2f} tf')
        ae = carga_hidraulica / 3
        print(f'Posicao de aplicacao da componente horizontal do empuxo: {ae:.2f} m')
        
        ap = base / 2  
        print(f'Posicao de aplicacao da componente vertical da forca: {ap:.2f} m')

        momento_empuxo = empuxo * ae
        print(f'Momento atuante: {momento_empuxo:.2f} tf.m')

        momento_peso = peso * ap  
        print(f'Momento resistente: {momento_peso} tf.m')


    if momento_empuxo * coeficiente_seguranca < momento_peso:
        print(f'Momento atuante ({momento_empuxo * coeficiente_seguranca:.2f} tf.m) < Momento resistente ({momento_peso:.2f} tf.m)')
        print('A barragem esta segura quanto ao tombamento')
    else:
        print(f'Momento atuante ({momento_empuxo * coeficiente_seguranca:.2f} tf.m) > Momento resistente ({momento_peso:.2f} tf.m)')
        print('A barragem nao esta segura quanto ao tombamento')
        
    
empuxo, peso = estabilidade_deslizamento('retangular', 2.5, 1.0, 3.0, 6.0, 0.7, 2.5, 5.0, 1.2)

estabilidade_tombamento(empuxo, peso, 'retangular', 2.5, 1.0, 3.0, 6.0, 0.7, 2.5, 5.0, 1.2)
