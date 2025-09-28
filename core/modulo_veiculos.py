# MÓDULO DE GERENCIAMENTO DE VEÍCULOS
import sys
import os

# Configurar caminho de importação
caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(caminho_base)

# Adiciona explicitamente a pasta database
caminho_database = os.path.join(caminho_base, 'database')
sys.path.append(caminho_database)

from database.veiculos_db import VeiculoDB
from utils.helpers import limpar_tela, aguardar_enter, input_int

class MenuVeiculos:
    
    def executar(self):
        while True:
            limpar_tela()
            print("=" * 40)
            print("    GERENCIAR VEÍCULOS")
            print("=" * 40)
            print("1. Cadastrar Veículo")
            print("2. Listar Veículos")
            print("3. Voltar ao Menu Principal")
            print("=" * 40)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_veiculo()
            elif opcao == "2":
                self.listar_veiculos()
            elif opcao == "3":
                break
            else:
                print("Opção inválida!")
                aguardar_enter()
    
    def cadastrar_veiculo(self):
        limpar_tela()
        print("CADASTRAR NOVO VEÍCULO")
        print("-" * 30)
        
        cliente_id = input_int("ID do Cliente: ")
        marca = input("Marca: ").strip()
        modelo = input("Modelo: ").strip()
        ano = input_int("Ano: ")
        placa = input("Placa: ").strip().upper()
        
        if not marca or not modelo or not placa:
            print("Marca, modelo e placa são obrigatórios!")
            aguardar_enter()
            return
        
        try:
            sucesso, mensagem = VeiculoDB.inserir_veiculo(cliente_id, marca, modelo, ano, placa)
            print(mensagem)
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
        
        aguardar_enter()
    
    def listar_veiculos(self):
        limpar_tela()
        print("LISTA DE VEÍCULOS")
        print("-" * 30)
        
        sucesso, resultado = VeiculoDB.buscar_veiculos()
        
        if sucesso:
            if resultado:
                for veiculo in resultado:
                    print(f"ID: {veiculo[0]}")
                    print(f"Cliente ID: {veiculo[1]}")
                    print(f"Marca: {veiculo[2]}")
                    print(f"Modelo: {veiculo[3]}")
                    print(f"Ano: {veiculo[4]}")
                    print(f"Placa: {veiculo[5]}")
                    print("-" * 20)
                print(f"Total: {len(resultado)} veículo(s)")
            else:
                print("Nenhum veículo cadastrado.")
        else:
            print(f"Erro: {resultado}")
        
        aguardar_enter()
    
    def listar_todos(self):
        sucesso, resultado = VeiculoDB.buscar_veiculos()
        return resultado if sucesso else []