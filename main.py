# from mostrar_valor import mostrar_valor
# from fazer_pagamento import pagamento

# def mercado():
#     lista_produtos = ['a','b','c']
#     print('Produtos', lista_produtos)
#     lista_valores  = [10,20,30]
#     print('R$', lista_valores)
#     carrinho = []
#     valor_pagar = [] 

#     pedido = input('Deseja efetuar o pedido s/n')
#     while pedido == 's':
#           escolha =  int(input('Escolha o produto através do ID'))
#           carrinho.append(lista_produtos[escolha])
#           valor_pagar.append(lista_valores[escolha])
#           print(carrinho)
#           print(valor_pagar)
#           pedido = input('Deseja efetuar o pedido s/n')
#     else: 
#          mostrar = mostrar_valor(valor_pagar)
#          print('R$',mostrar )  
#     print('valor a pagar: R$',mostrar )   
#     pagamento()     
         
          

# mercado()

import meu_modulo



# def sistema_notas():
#     print('SISTEMA DE NOTAS DOS ALUNOS')    
#     dados =  {}    


#     quantidade = int(input('Quantidade de alunos: '))
#     for n in range(quantidade):
#         nome  = input('Aluno')
#         dados[nome] = []
#         n1  =  float(input('Nota 1'))
#         n2  =  float(input('Nota 2'))
#         n3  =  float(input('Nota 3'))
#         dados[nome].extend([n1,n2,n3])
#         # print(dados)
#         print('***'*10)
#     print(dados)
#     print('Veja a estatística: ')
#     verificar_aluno = input('Digite o nome do aluno : ')


#     media = meu_modulo.media_notas(dados[verificar_aluno])
#     # print(media)
#     print('Media aluno(a)', verificar_aluno,'-', media)
#     moda = meu_modulo.moda_notas(dados[verificar_aluno])
#     print('Moda aluno(a)', verificar_aluno,'-', moda)
#     desvio = meu_modulo.desvio_notas(dados[verificar_aluno])
#     print('Desvio padrão aluno(a)', verificar_aluno,'-', desvio)
#     meu_modulo.menor_maior(dados[verificar_aluno])
#     meu_modulo.mediana_nota(dados[verificar_aluno])




   


#sistema_notas()


def sistema_empresas():   
    dados =  {}    


    quantidade = int(input('Quantidade de empresas: '))
    for n in range(quantidade):
        nome  = input('empresa')
        dados[nome] = []
        n1  =  float(input('salario 1: '))
        n2  =  float(input('salario 2: '))
        n3  =  float(input('salario 3: '))
        n4  =  float(input('salario 4: '))
        n5  =  float(input('salario 5: '))
        dados[nome].extend([n1,n2,n3,n4,n5])
        # print(dados)
        print('***'*10)
    print(dados)
    print('Veja a estatística: ')
    verificar_aluno = input('Digite o nome da empresa : ')


    media = meu_modulo.media_notas(dados[verificar_aluno])
    # print(media)
    print('Media da emprsa', verificar_aluno,'-', media)
    moda = meu_modulo.moda_notas(dados[verificar_aluno])
    print('Moda da empresa', verificar_aluno,'-', moda)
    desvio = meu_modulo.mediana_nota(dados[verificar_aluno])
    print('Mediana da empresa', verificar_aluno,'-', desvio)
    meu_modulo.menor_maior(dados[verificar_aluno])
    meu_modulo.mediana_nota(dados[verificar_aluno])




   


sistema_empresas()