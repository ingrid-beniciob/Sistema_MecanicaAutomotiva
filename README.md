# Sistema de Gestão para Mecânica Automotiva (AutoCharm)

Este é um sistema simples de gerenciamento para oficinas de mecânica automotiva, desenvolvido em Python. Ele é operado inteiramente via terminal e serve para demonstrar a estrutura de um aplicativo de console conectado a um banco de dados.

## Funcionalidades Principais

O sistema é um aplicativo de console para gerenciamento de uma oficina mecânica, dividido nos seguintes módulos principais:

### 1. Gerenciamento de Clientes
* Inserir novos clientes no banco de dados.
* Listar todos os clientes cadastrados.
* Buscar um cliente específico pelo seu ID.

### 2. Gerenciamento de Veículos
* Cadastrar novos veículos, associando-os a um ID de cliente.
* Listar todos os veículos cadastrados no sistema.

### 3. Gerenciamento de Funcionários
* Cadastrar novos funcionários (nome, cargo, aniversário, CPF).
* Listar todos os funcionários da oficina.

### 4. Gerenciamento de Fornecedores
* Cadastrar novos fornecedores (nome, CNPJ, telefone).
* Listar todos os fornecedores cadastrados.

### 5. Gerenciamento de Estoque
* Adicionar novos itens ao estoque (peças, produtos).
* Listar todos os itens do estoque, mostrando quantidade e valor total.
* Atualizar a quantidade de um item existente no estoque.

### 6. Gerenciamento de Contas (Financeiro)
* Adicionar contas a receber (receitas).
* Adicionar contas a pagar (despesas).
* Listar todas as contas (a pagar e a receber), exibindo um saldo.

### 7. Gerenciamento de Ordens de Serviço
* Criar novas ordens de serviço, vinculadas a um cliente e veículo.
* Listar todas as ordens de serviço cadastradas.
* Atualizar o status de uma ordem de serviço (ex: "A iniciar", "Em andamento", "Finalizado").

## Como Clonar e Executar

1.  **Clone o repositório:**
    (A URL exata do repositório não foi fornecida, mas o comando seria assim:)
    ```bash
    git clone [https://github.com/ingrid-beniciob/sistema_mecanicaautomotiva.git](https://github.com/ingrid-beniciob/sistema_mecanicaautomotiva.git)
    ```

2.  **Navegue até a pasta do projeto:**
    Entre na pasta que contém os diretórios `core` e `database`. O nome pode variar, mas baseado nos arquivos, seria algo como:
    ```bash
    cd sistema_mecanicaautomotiva/Sistema_MecanicaAutomotiva-2d3b02ad0d14d9d831cd775b995ea31cde1eaf99
    ```

3.  **Instale as dependências:**
    O projeto depende do conector MySQL para Python.
    ```bash
    pip install mysql-connector-python
    ```

4.  **Configure o Banco de Dados:**
    * Inicie seu servidor MySQL.
    * Crie um banco de dados com o nome `autocharm`.
    * **Importante:** Os arquivos `*.sql` para criação das tabelas (cliente, veiculos, estoque, etc.) não foram fornecidos. Você precisará criá-las manualmente no banco `autocharm` para que o sistema funcione.
    * O sistema tentará se conectar ao `localhost` com o usuário `root` e senha vazia, que é o padrão do XAMPP. Se sua configuração for diferente, edite o arquivo `database/conexao_db.py`.

5.  **Execute o sistema:**
    O arquivo principal que inicia o menu é o `main.py` dentro da pasta `core`.
    ```bash
    python core/main.py
    ```
