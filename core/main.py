  
#GERENCIADOR DO SISTEMA DE TESTES AUTOCHARM ANTES DO GUI
#Este é o arquivo que inicia todo o sistema

import os
import sys

# configurar caminhos de importação
# Adiciona o diretório atual ao path para poder importar nossos módulos
# Path é uma variável do sistema que armazena uma lista de diretórios 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# importar todos os módulos do sistema
from modulo_clientes import MenuClientes
from modulo_veiculos import MenuVeiculos
from modulo_funcionarios import MenuFuncionarios
from modulo_fornecedores import MenuFornecedores
from modulo_estoque import MenuEstoque
from modulo_contas import MenuContas
from modulo_ordens_servico import MenuOrdensServico
from utils.helpers import limpar_tela, aguardar_enter

class MainMenu:
    
    # CLASSE DO MENU PRINCIPAL
    # Controla a navegação entre os diferentes módulos
    
    
    def __init__(self):
        
        # Quando criamos um objeto MainMenu, automaticamente inicia o menu principal
        
        self.menu_principal()
    
    def menu_principal(self):
        
        # Mostra as opções principais do sistema
        # Aguarda a escolha do usuário
        # Direciona para o módulo correspondente
        # Repete até o usuário escolher sair
        
        while True:
            # Limpar tela e mostra cabeçalho para apresentar pro cliente a ideia
            limpar_tela()
            print("=" * 50)
            print("    AUTOCHARM - SISTEMA DE TESTES")
            print("=" * 50)
            
            # opções do menu
            print("1. Clientes")
            print("2. Veículos")
            print("3. Funcionários")
            print("4. Fornecedores")
            print("5. Estoque")
            print("6. Contas (Receitas/Despesas)")
            print("7. Ordens de Serviço")
            print("0. Sair")
            print("=" * 50)
            
            # Solicita opção do usuário
            opcao = input("Escolha uma opção: ").strip()
            
            # Processa a opção escolhida
            if opcao == "1":
                # Executa as opção escolhida
                MenuClientes().executar()
            elif opcao == "2":
                MenuVeiculos().executar()
            elif opcao == "3":
                MenuFuncionarios().executar()
            elif opcao == "4":
                MenuFornecedores().executar()
            elif opcao == "5":
                MenuEstoque().executar()
            elif opcao == "6":
                MenuContas().executar()
            elif opcao == "7":
                MenuOrdensServico().executar()
            elif opcao == "0":
                print("Saindo do sistema...")
                break  # Sai do loop e termina o programa
            else:
                print("Opção inválida!")
                aguardar_enter()
    

# Código que roda quando executamos o arquivo diretamente
if __name__ == "__main__":
    
    # Este código só roda se executarmos este arquivo diretamente
    # Se importarmos este arquivo em outro, este código não roda
    
    try:
        # Cria o menu principal e inicia o sistema
        MainMenu()
    except KeyboardInterrupt:
        # Se o usuário pressionar Ctrl+C, mostra mensagem educada
        print("\n\nPrograma interrompido pelo usuário.")
    except Exception as e:
        # Se ocorrer qualquer erro inesperado, mostra detalhes
        print(f"\nErro inesperado: {e}")