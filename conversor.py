# IMPORTAÇÕES
import requests
import os
from rich import print
from time import sleep

'''
REAL PARA OUTRO

USD-BRL - Dólar Americano/Real Brasileiro
USD-BRLT - Dólar Americano/Real Brasileiro Turismo
CAD-BRL - Dólar Canadense/Real Brasileiro
EUR-BRL - Euro/Real Brasileiro
BTC-BRL - Bitcoin/Real Brasileiro
JPY-BRL - Iene Japonês/Real Brasileiro
BRL-ARS - Real Brasileiro/Peso Argentino

'''

# IDENTIFICAÇÃO DAS MOEDAS
moedas = {'1':'DOLAR', '2':'EURO', '3':'DOLAR CANADENSE', '4':'IENE','5':'PESO ARGENTINO'}

# CONVERSOES REAL TO *
dados = requests.get('http://economia.awesomeapi.Com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,CAD-BRL,JPY-BRL,USD-BRLT,BTC-BRL,ARS-BRL')
dadosjson = dados.json()
dolar = dadosjson['USDBRL']['bid']
euro = dadosjson['EURBRL']['bid']
dolarcanad = dadosjson['CADBRL']['bid']
iene = dadosjson['JPYBRL']['bid']
argent = dadosjson['ARSBRL']['bid']
dolart = dadosjson['USDBRLT']['bid']

# --------------------------------------------------------------------------------------------------------------------------------------------- 

# FUNÇÃO PARA SAIR
def sair():
    print('Saindo...')
    sleep(2)
    exit()


    
# FUNÇÃO PARA CALCULAR O VALOR DO INVESTIMENTO
def val():
    
    if valor == 0:
        print('[bold][red]Sem dinheiro você não pode Comprar qualquer moeda!!')       

    elif opcao == '1':
        print(f'Investindo R${valor} você Compra {valor/float(dolar):,.2f} em {moedas[opcao]}')

    elif opcao == '2':
        print(f'Investindo R${valor} você Compra {valor/float(euro):,.2f} em {moedas[opcao]}')
        

    elif opcao == '3':
        print(f'Investindo R${valor} você Compra {valor/float(dolarcanad):,.2f} em {moedas[opcao]}')
    

    elif opcao == '4':
        print(f'Investindo R${valor} você Compra {valor/float(iene):,.2f} em {moedas[opcao]}')
        

    elif opcao == '5':
        print(f'Investindo R${valor} você Compra {valor/float(argent):,.2f} em {moedas[opcao]}')
 
    


    
# EXPLICAÇÃO DO SISTEMA
os.system('clear')
print('-'*70)
print('/','Olá!'.center(65),'/')
print('/','Bem vindo ao nosso conversor de moeda.'.center(65),'/')
print('/','Nessa nossa versão inicial calculamos apenas usando o Real - R$'.center(65),'/')
print('/','Brasileiro como moeda de compra.'.center(65),'/')
print('/','Mas, futuramente iremos adicionar outras moedas ao conversor.'.center(65),'/')
print('/','Para usar basta apenas escolher a opção de compra'.center(65),'/')
print('/','e digitar o valor do investimento...'.center(65),'/')
print('-'*70)
print('Tecle < [bold][purple]Enter[/][/] > para continuar...\n')
input()
os.system('clear')





while True:
    print('-'*34)
    print('|','DIGITE A OPÇÃO DE CONVERSÃO'.ljust(30),'|')
    print('-'*34)
    print('|','[1]-REAL - DOLAR'.ljust(30),'|')
    print('|','[2]-REAL - EURO'.ljust(30),'|')
    print('|','[3]-REAL - DOLAR CANADENSE'.ljust(30),'|')
    print('|','[4]-REAL - IENE'.ljust(30),'|')
    print('|','[5]-REAL - PESO ARGENTINO'.ljust(30),'|')
    print('|','[0]- SAIR'.ljust(30),'|')
    print('-'*34)
    
    # RECEBENDO A OPÇÃO DE CONVERSÃO
    opcao = input('Digite sua opção aqui: ')
    while opcao =='':
        print('Ops! Parece que você não digitou nada!!')
        opcao = input('Digite sua opção aqui: ')

    while opcao not in ['1','2','3','4','5','0']:
        print('Opção invalida!')    
        opcao = input('Digite sua opção aqui: ')
    # CALCULANDO O INVESTIMENTO SE TUDO CORRETO
    if opcao in moedas.keys():
    
        try:
            valor = int(input(f'Quanto deseja investir em {moedas[opcao]}: '))
        except ValueError:
            print('Desculpe, apenas números são permitidos!!')
            break
            

    elif opcao == '0':
        sair()

    os.system('clear')

    val()
    
