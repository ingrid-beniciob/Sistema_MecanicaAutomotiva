
# Módulo com funções auxiliares para o sistema
# Funções que serão usadas em vários lugares do código

import os

def limpar_tela():
   
# Esta função limpa a tela do terminal
# Verifica se o sistema é Windows (cls) ou Linux/Mac (clear)
# Executa o comando apropriado
    
    os.system('cls' if os.name == 'nt' else 'clear')

def aguardar_enter():
    
# Pausa a execução do programa
# Aguarda o usuário pressionar Enter
# Útil para dar tempo do usuário ler as mensagens
    
    input("\n↵ Pressione Enter para continuar...")

def input_int(mensagem):

# Solicita um número inteiro do usuário
# Fica em loop até receber um número válido
# Se o usuário digitar texto, mostra erro e pede novamente

    while True:
        try:
            # Tenta converter o input para número inteiro
            return int(input(mensagem).strip())
        except ValueError:
            # Se der erro (usuário digitou texto), mostra mensagem
            print("Por favor, digite um número inteiro válido.")

def input_float(mensagem):
   
# Solicita um número decimal do usuário
# Fica em loop até receber um número válido
# Aceita números com ponto decimal (ex: 10.50)
    
    while True:
        try:
            # Tenta converter o input para número decimal
            return float(input(mensagem).strip())
        except ValueError:
            # Se der erro, mostra mensagem e pede novamente
            print("Por favor, digite um número decimal válido.")

def validar_data(data_str):

# Verifica se uma string está no formato de data correto (YYYY-MM-DD)
#Retorna True se for válida, False se for inválida
    
    try:
        from datetime import datetime
        # Tenta converter a string para data
        datetime.strptime(data_str, '%Y-%m-%d')
        return True
    except ValueError:
        # Se a conversão falhar, a data é inválida
        return False