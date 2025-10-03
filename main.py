# # try:
# #     n = int(input('coloque um numero'))
# #     print(n,' é um numero inteiro')
# # except ValueError as error:
# #     print(error,'não e inteiro')

# # a = int(input(''))
# # b = int(input(''))
# # try:
# #     print(a/b)
# # except ZeroDivisionError as error:
# #       print(error)


# # try:
# #     lista =[1,2,3,4,5]
# #     escolha = int(input('escolha uma opção'))
# #     print(lista[escolha])
# # except IndexError:
# #     print('não à opção escolida')

# def soma():
#     n1 = int(input('nº:'))
#     n2 = int(input('nº: '))
#     print(n1+n2)

# def sub():
#     n1 = int(input('nº:'))
#     n2 = int(input('nº: '))
#     print(n1-n2)

# def mult():
#     n1 = int(input('nº:'))
#     n2 = int(input('nº: '))
#     print(n1*n2)

# def div():
#     n1 = int(input('nº:'))
#     n2 = int(input('nº: '))
#     print(n1/n2)

# def calculadora():
#     while True:
#         print('calculadora z')
#         operacao = input('''Escolha uma equação
#                      + | - | * | /''')
#         if operacao == '+':
#             soma
#         elif operacao == '*':
#             mult()
#         elif operacao == '-':
#             sub()
#         elif operacao == '/':
#             div()
#         else:
#             print('digite algo valido')
# calculadora()

# def numeros():
#     n1= int(input(''))
#     if n1 %2:
#         print('impar')
#     else:
#         print('par')
#     n2 = int(input(''))
#     if n2%2:
#         print('impar')
#     else:
#         print('par')
# numeros()

# def mult():
#     n1 = int(input('nº: '))
#     n2 = int(input('nº: '))
#     n3 = int(input('nº: '))
#     print(n1*n2*n3)
# mult()

# def mult():
#     n1=int(input(''))
#     n2=int(input(''))
#     print(n1**n2)
# mult()

# def idade():
#     ano=2025
#     nascimento=int(input('coloque seu ano de nascimeto: '))
#     print(ano-nascimento)
# idade()

def cardapio():
    lista={
'salada':10,
'macarronada':35,
'sanduiche':15,
'sorvete':12
}
    print(lista)
    print('escolha uma opção do cardapio')
    escolha=input('')
    valor=[lista[escolha]]
    print()
    print('você escolheu', escolha)
    print('R$',valor)
cardapio()