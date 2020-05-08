#coding: utf-8

from os import system
from time import sleep

opcaoMenu = 0
valorTotal = 0

def opcao1(valorTotal):
    opcaoCrepes = 0

    while opcaoCrepes != 5:
        print('''============ CREPES ============\n
        [1] Crepe de Frango - R$10.99
        [2] Crepe de Carne - R$16.90
        [3] Crepe de Chocolate - R$17.99
        [4] Crepe de Nutella - R$20.99
        [5] Voltar\n''')

        opcaoCrepes = int(input('>>>>>>Qual é a sua opção? '))

        if opcaoCrepes == 1:
            valorTotal += 10.99
            print('Crepe de Frango adicionado ao carrinho com sucesso!. . .')
            sleep(2)
            system('cls')
        elif opcaoCrepes == 2:
            valorTotal += 16.90
            print('Crepe de Carne adicionado ao carrinho!. . .')
            sleep(2)
            system('cls')
        elif opcaoCrepes == 3:
            valorTotal += 17.99
            print('Crepe de Chocolate adicionado ao carrinho!. . .')
            sleep(2)
            system('cls')
        elif opcaoCrepes == 4:
            valorTotal += 20.99
            print('Crepe de Nutella adicionado ao carrinho!. . .')
            sleep(2)
            system('cls')    
        elif opcaoCrepes == 5:
            print('Voltando. . .') 
            sleep(2)
            system('cls')
        else:
            print('Opção inválida. Digite novamente.')
            sleep(2)
            system('cls') 
    return valorTotal

def opcao2(valorTotal):
    opcaoBebidas = 0

    while opcaoBebidas != 3:
        print('''============ BEBIDAS ============\n
        [1] Refrigerantes
        [2] Sucos Naturais
        [3] Voltar\n''')

        opcaoBebidas = int(input('>>>>>>Qual é a sua opção? '))

        if opcaoBebidas == 1:
            system('cls')
            valorTotal = opcaoBebidas1(valorTotal)            
        elif opcaoBebidas == 2:
            system('cls') 
            valorTotal = opcaoBebidas2(valorTotal) 
        elif opcaoBebidas == 3:
            print('Voltando. . .') 
            sleep(2)
            system('cls')
        else:
            print('Opção inválida. Digite novamente.')
            sleep(2)
            system('cls') 
    return valorTotal 

def opcaoBebidas1(valorTotal):
    opcaoBebidas1 = 0

    while opcaoBebidas1 != 5:
        print('''============ REFRIGERANTES ============\n
        [1] Fanta - R$3.50
        [2] Coca-Cola - R$4.80
        [3] Dolly - R$4.90
        [4] Guaraná Jesus - R$5.30
        [5] Voltar\n''')

        opcaoBebidas1 = int(input('>>>>>>Qual é a sua opção? '))

        if opcaoBebidas1 == 1:
            valorTotal += 3.50
            print('Fanta adicionado ao carrinho com sucesso!. . .')
            sleep(2)
            system('cls')
            
        elif opcaoBebidas1 == 2:
            valorTotal += 4.80
            print('Coca-Cola adicionado ao carrinho com sucesso!. . .')
            sleep(2)
            system('cls')
        elif opcaoBebidas1 == 3:
            valorTotal += 4.90
            print('Dolly adicionado ao carrinho com sucesso!. . .')
            sleep(2)
            system('cls')
        elif opcaoBebidas1 == 4:
            valorTotal += 5.30
            print('Guaraná Jesus adicionado ao carrinho com sucesso!. . .')
            sleep(2)
            system('cls') 
        elif opcaoBebidas1 == 5:
            print('Voltando. . .') 
            sleep(2)
            system('cls')           
        else:
            print('Opção inválida. Digite novamente.')
            sleep(2)
            system('cls') 
    return valorTotal 

def opcaoBebidas2(valorTotal):
    opcaoBebidas2 = 0

    while opcaoBebidas2 != 5:
        print('''============ SUCOS NATURAIS ============\n
        [1] Suco de Laranja - R$3.40
        [2] Suco de Goiaba - R$3.50
        [3] Suco de Morango - R$3.90
        [4] Suco de Abacaxi - R$3.99
        [5] Voltar\n''')

        opcaoBebidas2 = int(input('>>>>>>Qual é a sua opção? '))

        if opcaoBebidas2 == 1:
            valorTotal += 3.40
            print('Suco de Laranja adicionado ao carrinho com sucesso!. . .')
            sleep(2)
            system('cls')
            
        elif opcaoBebidas2 == 2:
            valorTotal += 3.50
            print('Suco de Goiaba adicionado ao carrinho com sucesso!. . .')
            sleep(2)
            system('cls')
        elif opcaoBebidas2 == 3:
            valorTotal += 3.90
            print('Suco de Morango adicionado ao carrinho com sucesso!. . .')
            sleep(2)
            system('cls')
        elif opcaoBebidas2 == 4:
            valorTotal += 3.99
            print('Suco de Abacaxi adicionado ao carrinho com sucesso!. . .')
            sleep(2)
            system('cls') 
        elif opcaoBebidas2 == 5:
            print('Voltando. . .') 
            sleep(2)
            system('cls')           
        else:
            print('Opção inválida. Digite novamente.')
            sleep(2)
            system('cls') 
    return valorTotal 

while opcaoMenu != 4:
    system('clear') 
    print('''
    SEJA BEM-VINDO AO ORC'CREPES! 
    ============ MENU ============\n
    [1]Crepes
    [2]Bebidas
    [3]Valor da Conta
    [4]Fechar Pedido\n
    ''')
    opcaoMenu = int(input('>>>>>>Qual é a sua opção? '))

    if opcaoMenu == 1:
        system('cls') 
        valorTotal = opcao1(valorTotal)
    elif opcaoMenu == 2:
        system('cls') 
        valorTotal = opcao2(valorTotal)
    elif opcaoMenu == 3:
        print('Sua conta atual está em R$ {}'.format(round(valorTotal, 2)))
        sleep(2)
        system('cls')
    elif opcaoMenu == 4:
        print('Finalizando pedido. . .')
    else:
        print('Opção inválida. Digite novamente.')

print('Obrigado! Volte Sempre! ^-^ ')
 



