# MÓDULO DE GERENCIAMENTO DE CONTAS
import sys
import os

# Configurar caminho para importar
caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(caminho_base)

caminho_database = os.path.join(caminho_base, 'database')
sys.path.append(caminho_database)

from database.contas_db import ContasDB
from utils.helpers import limpar_tela, aguardar_enter, input_int, input_float

class MenuContas:
    
    def executar(self):
        # Menu principal de contas
        while True:
            limpar_tela()
            print("=" * 40)
            print("    GERENCIAR CONTAS")
            print("=" * 40)
            print("1. Adicionar Conta a Receber")
            print("2. Adicionar Conta a Pagar")
            print("3. Listar Todas as Contas")
            print("4. Voltar ao Menu Principal")
            print("=" * 40)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.adicionar_conta_receber()
            elif opcao == "2":
                self.adicionar_conta_pagar()
            elif opcao == "3":
                self.listar_contas()
            elif opcao == "4":
                break
            else:
                print("Opção inválida!")
                aguardar_enter()
    
    def adicionar_conta_receber(self):
        # Adiciona conta a receber
        limpar_tela()
        print("ADICIONAR CONTA A RECEBER")
        print("-" * 30)
        
        descricao = input("Descrição: ").strip()
        valor = input_float("Valor: R$ ")
        vencimento = input("Data de vencimento (YYYY-MM-DD): ").strip()
        cliente_id = input("ID do Cliente (opcional): ").strip()
        
        # Valida dados obrigatórios
        if not descricao or not valor or not vencimento:
            print("Descrição, valor e vencimento são obrigatórios!")
            aguardar_enter()
            return
        
        try:
            cliente_id = int(cliente_id) if cliente_id else None
            
            # Insere conta a receber
            sucesso, mensagem = ContasDB.inserir_conta(
                'Receita - Conta a Receber', 
                descricao, 
                valor, 
                vencimento, 
                'A pagar', 
                cliente_id,
                'aberta'  # Status inicial
            )
            print(mensagem)
        except Exception as e:
            print(f"Erro ao adicionar conta: {e}")
        
        aguardar_enter()
    
    def adicionar_conta_pagar(self):
        # Adiciona conta a pagar
        limpar_tela()
        print("ADICIONAR CONTA A PAGAR")
        print("-" * 30)
        
        descricao = input("Descrição: ").strip()
        valor = input_float("Valor: R$ ")
        vencimento = input("Data de vencimento (YYYY-MM-DD): ").strip()
        
        # Menu de formas de pagamento
        print("\nFormas de pagamento:")
        print("1 - A pagar")
        print("2 - Dinheiro")
        print("3 - Cartão Débito") 
        print("4 - Cartão Crédito")
        print("5 - PIX")
        print("6 - Transferência")
        
        opcao_pagamento = input("Escolha a forma de pagamento (1-6): ").strip()
        
        # Mapeia opções para textos
        formas = {
            '1': 'A pagar',
            '2': 'Dinheiro',
            '3': 'Cartão Débito', 
            '4': 'Cartão Crédito',
            '5': 'PIX',
            '6': 'Transferência'
        }
        
        forma_pagamento = formas.get(opcao_pagamento, 'A pagar')
        
        # Valida dados obrigatórios
        if not descricao or not valor or not vencimento:
            print("Descrição, valor e vencimento são obrigatórios!")
            aguardar_enter()
            return
        
        try:
            # Insere conta a pagar
            sucesso, mensagem = ContasDB.inserir_conta(
                'Despesa - Conta a Pagar', 
                descricao, 
                valor, 
                vencimento, 
                forma_pagamento,
                None,  # Conta a pagar não tem cliente
                'aberta'  # Status inicial
            )
            print(mensagem)
        except Exception as e:
            print(f"Erro ao adicionar conta: {e}")
        
        aguardar_enter()
    
    def listar_contas(self):
        # Lista todas as contas
        limpar_tela()
        print("LISTA DE CONTAS")
        print("-" * 30)
        
        sucesso, resultado = ContasDB.buscar_contas()
        
        if sucesso:
            if resultado:
                total_receber = 0
                total_pagar = 0
                
                # Mostra cada conta
                for conta in resultado:
                    tipo = "RECEBER" if "Receita" in conta[1] else "PAGAR"
                    status = "PAGA" if conta[5] == 'paga' else "ABERTA"
                    
                    print(f"ID: {conta[0]}")
                    print(f"Tipo: {tipo}")
                    print(f"Descrição: {conta[2]}")
                    print(f"Valor: R$ {conta[3]:.2f}")
                    print(f"Vencimento: {conta[4]}")
                    print(f"Status: {status}")
                    print(f"Forma Pagamento: {conta[6]}")
                    if conta[7]:
                        print(f"Cliente ID: {conta[7]}")
                    print("-" * 20)
                    
                    # Soma totais das contas abertas
                    if "Receita" in conta[1] and conta[5] == 'aberta':
                        total_receber += conta[3]
                    elif "Despesa" in conta[1] and conta[5] == 'aberta':
                        total_pagar += conta[3]
                
                # Mostra resumo
                print(f"Total a Receber: R$ {total_receber:.2f}")
                print(f"Total a Pagar: R$ {total_pagar:.2f}")
                print(f"Saldo: R$ {(total_receber - total_pagar):.2f}")
                print(f"Total de contas: {len(resultado)}")
            else:
                print("Nenhuma conta cadastrada.")
        else:
            print(f"Erro: {resultado}")
        
        aguardar_enter()
    
    def listar_todos(self):
        # Retorna todas as contas para relatório
        sucesso, resultado = ContasDB.buscar_contas()
        return resultado if sucesso else []