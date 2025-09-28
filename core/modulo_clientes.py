# MÓDULO DE GERENCIAMENTO DE CLIENTES
import sys
import os

# CORREÇÃO: Configurar caminho para encontrar a pasta database
caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(caminho_base)  # Agora aponta para "Sistema AutoCharm"

# CORREÇÃO: Importar corretamente
sys.path.append(os.path.join(caminho_base, 'database'))  # Adiciona pasta database ao path

from database.clientes_db import ClienteDB  # Agora importa diretamente
from utils.helpers import limpar_tela, aguardar_enter, input_int

class MenuClientes:
    
    def executar(self):
        while True:
            limpar_tela()
            print("=" * 40)
            print("    GERENCIAR CLIENTES")
            print("=" * 40)
            print("1. Inserir Cliente")
            print("2. Listar Clientes")
            print("3. Buscar Cliente por ID")
            print("4. Voltar ao Menu Principal")
            print("=" * 40)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.inserir_cliente()
            elif opcao == "2":
                self.listar_clientes()
            elif opcao == "3":
                self.buscar_cliente_id()
            elif opcao == "4":
                break
            else:
                print("Opção inválida!")
                aguardar_enter()
    
    def inserir_cliente(self):
        limpar_tela()
        print("INSERIR NOVO CLIENTE")
        print("-" * 30)
        
        nome = input("Nome: ").strip()
        contato = input("Contato (telefone/email): ").strip()
        endereco = input("Endereço: ").strip()
        cpf = input("CPF (apenas números): ").strip()
        
        if not nome:
            print("Nome é obrigatório!")
            aguardar_enter()
            return
        
        if not cpf.isdigit():
            print("CPF deve conter apenas números!")
            aguardar_enter()
            return
        
        try:
            sucesso, mensagem = ClienteDB.inserir_cliente(nome, contato, endereco, int(cpf))
            print(mensagem)
        except Exception as e:
            print(f"Erro: {e}")
        
        aguardar_enter()
    
    def listar_clientes(self):
        limpar_tela()
        print("LISTA DE CLIENTES")
        print("-" * 30)
        
        sucesso, resultado = ClienteDB.buscar_clientes()
        
        if sucesso:
            if resultado:
                for cliente in resultado:
                    print(f"ID: {cliente[0]}")
                    print(f"Nome: {cliente[1]}")
                    print(f"Contato: {cliente[2]}")
                    print(f"Endereço: {cliente[3]}")
                    print(f"CPF: {cliente[4]}")
                    print("-" * 20)
                print(f"Total: {len(resultado)} cliente(s)")
            else:
                print("Nenhum cliente cadastrado.")
        else:
            print(f"Erro: {resultado}")
        
        aguardar_enter()
    
    def buscar_cliente_id(self):
        limpar_tela()
        print("BUSCAR CLIENTE POR ID")
        print("-" * 30)
        
        cliente_id = input_int("ID do cliente: ")
        
        sucesso, clientes = ClienteDB.buscar_clientes()
        
        if sucesso:
            cliente_encontrado = None
            for cliente in clientes:
                if cliente[0] == cliente_id:
                    cliente_encontrado = cliente
                    break
            
            if cliente_encontrado:
                print(f"Cliente encontrado:")
                print(f"ID: {cliente_encontrado[0]}")
                print(f"Nome: {cliente_encontrado[1]}")
                print(f"Contato: {cliente_encontrado[2]}")
                print(f"Endereço: {cliente_encontrado[3]}")
                print(f"CPF: {cliente_encontrado[4]}")
            else:
                print(f"Cliente com ID {cliente_id} não encontrado.")
        else:
            print(f"Erro na busca: {clientes}")
        
        aguardar_enter()
    
    def listar_todos(self):
        sucesso, resultado = ClienteDB.buscar_clientes()
        return resultado if sucesso else []