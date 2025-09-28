# MÓDULO DE GERENCIAMENTO DE ORDENS DE SERVIÇO
import sys
import os

# Configurar caminho de importação
caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(caminho_base)

# Adiciona explicitamente a pasta database
caminho_database = os.path.join(caminho_base, 'database')
sys.path.append(caminho_database)

from database.ordemservico_db import OrdemServicoDB
from utils.helpers import limpar_tela, aguardar_enter, input_int, input_float

class MenuOrdensServico:
    
    def executar(self):
        while True:
            limpar_tela()
            print("=" * 40)
            print("    ORDENS DE SERVIÇO")
            print("=" * 40)
            print("1. Criar Nova Ordem de Serviço")
            print("2. Listar Ordens de Serviço")
            print("3. Atualizar Status da Ordem")
            print("4. Voltar ao Menu Principal")
            print("=" * 40)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.criar_ordem_servico()
            elif opcao == "2":
                self.listar_ordens_servico()
            elif opcao == "3":
                self.atualizar_status()
            elif opcao == "4":
                break
            else:
                print("Opção inválida!")
                aguardar_enter()
    
    def criar_ordem_servico(self):
        limpar_tela()
        print("CRIAR ORDEM DE SERVIÇO")
        print("-" * 30)
        
        cliente_id = input_int("ID do Cliente: ")
        veiculo_id = input_int("ID do Veículo: ")
        descricao = input("Descrição do serviço: ").strip()
        valor_total = input_float("Valor total: R$ ")
        
        if not descricao or valor_total < 0:
            print("Descrição é obrigatória e valor deve ser positivo!")
            aguardar_enter()
            return
        
        print("\nStatus da ordem:")
        print("1 - A iniciar")
        print("2 - Em andamento") 
        print("3 - Finalizado")
        
        opcao_status = input("Escolha o status (1-3): ").strip()
        
        status_opcoes = {
            '1': 'A iniciar',
            '2': 'Em andamento',
            '3': 'Finalizado'
        }
        
        status = status_opcoes.get(opcao_status, 'A iniciar')
        
        try:
            sucesso, mensagem = OrdemServicoDB.criar_ordem_servico(
                cliente_id, veiculo_id, descricao, valor_total, status
            )
            print(mensagem)
        except Exception as e:
            print(f"Erro ao criar ordem de serviço: {e}")
        
        aguardar_enter()
    
    def listar_ordens_servico(self):
        limpar_tela()
        print("LISTA DE ORDENS DE SERVIÇO")
        print("-" * 30)
        
        sucesso, resultado = OrdemServicoDB.buscar_ordens_servico()
        
        if sucesso:
            if resultado:
                total_valor = 0
                
                for ordem in resultado:
                    total_valor += ordem[4] if ordem[4] else 0
                    
                    print(f"ID: {ordem[0]}")
                    print(f"Cliente ID: {ordem[1]}")
                    print(f"Veículo ID: {ordem[2]}")
                    print(f"Descrição: {ordem[3]}")
                    print(f"Valor Total: R$ {ordem[4]:.2f}")
                    print(f"Status: {ordem[5]}")
                    print("-" * 20)
                
                print(f"Valor total em ordens: R$ {total_valor:.2f}")
                print(f"Total de ordens: {len(resultado)}")
            else:
                print("Nenhuma ordem de serviço cadastrada.")
        else:
            print(f"Erro: {resultado}")
        
        aguardar_enter()
    
    def atualizar_status(self):
        limpar_tela()
        print("ATUALIZAR STATUS DA ORDEM")
        print("-" * 30)
        
        ordem_id = input_int("ID da Ordem de Serviço: ")
        
        print("\nNovo status:")
        print("1 - A iniciar")
        print("2 - Em andamento") 
        print("3 - Finalizado")
        
        opcao_status = input("Escolha o novo status (1-3): ").strip()
        
        status_opcoes = {
            '1': 'A iniciar',
            '2': 'Em andamento',
            '3': 'Finalizado'
        }
        
        novo_status = status_opcoes.get(opcao_status)
        
        if not novo_status:
            print("Status inválido!")
            aguardar_enter()
            return
        
        try:
            sucesso, mensagem = OrdemServicoDB.atualizar_status_ordem(ordem_id, novo_status)
            print(mensagem)
        except Exception as e:
            print(f"Erro ao atualizar status: {e}")
        
        aguardar_enter()
    
    def listar_todos(self):
        sucesso, resultado = OrdemServicoDB.buscar_ordens_servico()
        return resultado if sucesso else []