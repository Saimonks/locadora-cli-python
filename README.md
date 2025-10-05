🎥 LOCADORA CLI (Interface de Linha de Comando)

📌 Visão Geral do Projeto
Este é um sistema de gerenciamento de locadora de filmes desenvolvido em Python. Ele permite o cadastro de filmes e clientes, o controle completo do ciclo de locação (iniciar, adicionar ao carrinho, finalizar e devolver) e a emissão de relatórios financeiros e de estoque.

O sistema utiliza estruturas de dados nativas do Python (Listas e Dicionários) e opera através de uma interface de linha de comando (CLI).

🚀 Como Executar o Sistema
Pré-requisitos
Você só precisa ter o Python instalado em sua máquina (versão 3.6 ou superior).

Inicialização
Salve todo o código em um único arquivo chamado, por exemplo, locadora.py.

Abra o terminal (Prompt de Comando, PowerShell ou Terminal do VS Code) no diretório onde você salvou o arquivo.

Execute o sistema com o comando:

python locadora.py

O menu principal será exibido, e você poderá começar a interagir com o sistema.

📋 Funcionalidades Principais

O sistema é dividido em 4 módulos principais, acessíveis pelo menu:

1. Catálogo de Filmes (Gestão de Acervo)
Este módulo trata do controle de filmes e inventário:

Cadastrar Filme: Adiciona um novo filme ao acervo.

Validação Crucial: Garante que o código do filme seja único.

Validação Numérica: Garante que o preço da diária e o estoque inicial sejam números positivos (e aceita , ou . como separador decimal).

Listar Filmes: Exibe todo o acervo em ordem alfabética por título.

Atualizar Estoque: Permite ao usuário escolher se deseja adicionar ou remover unidades do estoque de um filme, bloqueando operações que resultariam em estoque negativo.

Remover Filme: Remove um filme do catálogo.

2. Clientes (Gestão de Cadastro)
Este módulo foca no registro e controle dos usuários da locadora:

Cadastrar Cliente: Registra um novo cliente (CPF, Nome, Telefone).

Validação Crucial: Garante que o CPF seja único e tenha exatamente 11 dígitos numéricos.

Listar Clientes: Exibe todos os clientes cadastrados (na ordem de registro).

Remover Cliente: Exclui um cliente do cadastro.

Segurança: Esta operação é bloqueada se o cliente possuir qualquer locação com o status ATIVA (ou seja, se ele ainda não devolveu um filme).

3. Locações (O Ciclo Completo)
Permite realizar o aluguel, debitando o estoque no momento da finalização:

Iniciar/Zerar: Cria o carrinho (carrinhos_ativos) para um cliente.

Adicionar: Adiciona filmes ao carrinho, checando se há estoque suficiente.

Finalizar: Aplica descontos e registra a locação no historico_locacoes, mudando o status para ATIVA e debitando o estoque.

Devolver: Encontra a locação ativa do cliente, aumenta o estoque e muda o status da locação para DEVOLVIDA.

4. Relatórios
Análise de dados do histórico de locações (historico_locacoes):

Total Faturado: Soma de todos os valores finais das locações.

Ticket Médio: Valor médio de cada locação registrada.

Filme Mais Alugado: Identifica o título com maior contagem no histórico.

Estoque Baixo: Lista filmes com estoque abaixo de um limite definido pelo usuário.

🛠️ Estrutura de Dados Globais
O sistema utiliza as seguintes listas e dicionários para armazenar e rastrear as informações:

Variável	                              Tipo	                                       Função
catalogo_filmes	                      list de dict	          Armazena todos os detalhes do acervo e estoque disponível.
clientes	                          list de dict	                    Armazena o cadastro de clientes.
carrinhos_ativos	                  list de dict	             Armazena os pedidos em andamento (carrinhos).
historico_locacoes	                  list de dict	      Armazena todas as transações concluídas, com o status (ATIVA ou DEVOLVIDA).
proximo_id_locacao	                      int	                  Contador para gerar IDs únicos para cada nova locação.



🤝 Autor
Saimon Ruan Alves Moreira

Trabalho de Desenvolvimento em Python para Paradigmas de Linguagens de Programação em Python / ESTACIO