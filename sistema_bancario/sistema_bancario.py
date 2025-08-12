# Implementar 3 operações: Depósito, Saque e Extrato
# Sistema deve permitir 3 saques diários com limite maximo de 500 por saque

"""
- Deposito:
Somente valores positivos
Todos os depositos devem ser armazenados em uma variável  e exibidos na operação extrato
"""

"""
- Saque:
Caso o usuário nao tenha saldo o sistema deve mostra uma mensagem
Todos os saques devem ser armazenados  em uma variavel  e exibidos na operação de extrato
"""


"""
- Extrato:
Essa operação deve listar todos depositos e saques realizados na conta e no fim mostra o saldo atual
Se o extrato estiver em branco , exibir a mensagem de nao foram realizadas movimentações
Os valores devem ser exibidos utilizando o formato R$ xxxx.xx
"""

saldo = 0
numero_de_saques = 0
extrato = ''
VALOR_MAXIMO_SAQUE = 500
SAQUES_DISPONIVEIS = 3

menu = """
    $$ BEM VINDO AO BANCO MONEY $$

Operações disponíveis:
1 - Depósito
2 - Saque
3 - Extrato
4 - Sair

Digite a opção desejada: """
while True:
    try:
        opcao = int(input(menu))

        if opcao == 1:
            valor = float(input('Digite o valor que deseja depositar: '))
            if valor < 0:
                print('\nImpossível depositar valor negativo!\n')
            else:
                saldo += valor
                print(f'\nValor de R${valor:.2f} depositado com sucesso!\nObrigado e volte sempre!\n\n')
                extrato += f'Depósito: R${valor:.2f}\n'
        
        elif opcao == 2:
            valor = float(input('Digite o valor que deseja sacar: '))
            
            excedeu_limite_saque = numero_de_saques >= SAQUES_DISPONIVEIS
            excedeu_saldo = saldo < valor
            excedeu_limite = valor > VALOR_MAXIMO_SAQUE

            if excedeu_limite_saque:
                print('\nErro: Limite de saques diários atingido. Volte amanhã!')
            elif excedeu_saldo:
                print('\nErro: Saldo insuficiente!')
                print(f'Seu saldo atual é de R${saldo:.2f} .')
            elif excedeu_limite:
                print(f'\nErro: Valor solicitado superior a {VALOR_MAXIMO_SAQUE:.2f}!')
            elif valor > 0:
                saldo -= valor
                numero_de_saques += 1
                print(f'\nValor de R${valor:.2f} sacado com sucesso!')
                print(f'Seu saldo atual é de R${saldo:.2f} .')
                extrato += f'Saque: R${valor:.2f}\n'
            else:
                print('\nErro: Valor informado inválido. Tente novamente!')

        elif opcao == 3:
            print('\n\n========= EXTRATO DETALHADO =========')
            print("\nNão foram realizadas movimentações." if not extrato else extrato)
            print(f'\nSaldo disponível: R${saldo:.2f} .\n')
            print('=====================================')
        
        elif opcao == 4:
            break
        
        else:
            print('erro: Opção inválida. Tente novamente!')
    
    except ValueError:
        print('Erro: opção inválida. Tente novamente')


    
