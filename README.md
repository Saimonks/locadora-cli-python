<h1>🍿 LOCADORA CLI - Sistema de Gestão de Filmes</h1>

<h2>📌 Sobre o Projeto</h2>
<p>
  Este é um sistema completo para gerenciamento de uma locadora de filmes, desenvolvido em <strong>Python</strong> e operado via Interface de Linha de Comando (CLI). 
  O foco é a <strong>segurança de dados</strong> e <strong>validações robustas</strong> em todo o ciclo de locação.
</p>

<h2>✨ Funcionalidades Detalhadas</h2>
<p>O sistema é modularizado em 4 áreas principais, cada uma com seu próprio submenu de operações:</p>

<h3>1. 🎬 Catálogo de Filmes (Módulo Principal)</h3>
<ul>
  <li><strong>Cadastrar Filme:</strong> Adiciona um novo filme. Garante código único e valores monetários/estoque positivos (aceita "," ou "." como decimal).</li>
  <li><strong>Listar Filmes:</strong> Exibe todo o acervo em ordem alfabética por título.</li>
  <li><strong>Atualizar Estoque:</strong> Permite adicionar ou remover unidades. Bloqueia operações que resultem em estoque negativo.</li>
  <li><strong>Remover Filme:</strong> Exclui um filme do catálogo.</li>
</ul>

<h3>2. 👤 Clientes (Módulo Principal)</h3>
<ul>
  <li><strong>Cadastrar Cliente:</strong> Registra cliente (CPF, Nome, Telefone). CPF deve ser único e conter 11 dígitos numéricos.</li>
  <li><strong>Listar Clientes:</strong> Exibe todos os clientes cadastrados, organizados por ordem alfabética do nome.</li>
  <li><strong>Remover Cliente:</strong> Exclui um cliente do cadastro. ⚠️ Bloqueado se houver locação com status ATIVA.</li>
</ul>

<h3>3. 🛒 Locações (Módulo Principal)</h3>
<p>Controla o ciclo de aluguel, registrando a data e hora exata da transação:</p>
<ul>
  <li><strong>Iniciar/Zerar Locação:</strong> Cria um carrinho de locação associado ao CPF.</li>
  <li><strong>Adicionar Filme ao Carrinho:</strong> Adiciona itens ao carrinho, verifica disponibilidade e consolida itens duplicados.</li>
  <li><strong>Remover Filme do Carrinho:</strong> Permite retirar itens antes da finalização.</li>
  <li><strong>Ver Carrinho e Subtotal:</strong> Mostra todos os itens no carrinho e calcula o subtotal.</li>
  <li><strong>Finalizar Locação:</strong> Processa pagamento, aplica desconto, debita estoque (<code>qtd_disponivel -= 1</code>) e registra a transação com status ATIVA.</li>
  <li><strong>Devolver Filmes:</strong> Reverte a locação, aumenta estoque (<code>qtd_disponivel += 1</code>) e atualiza o status para DEVOLVIDA.</li>
</ul>

<h3>4. 📊 Relatórios (Módulo Principal)</h3>
<ul>
  <li><strong>Total Faturado:</strong> Soma total de todos os valores pagos.</li>
  <li><strong>Ticket Médio por Locação:</strong> Média de valor pago por transação.</li>
  <li><strong>Filme Mais Alugado:</strong> Título com maior contagem no histórico.</li>
  <li><strong>Estoque Baixo:</strong> Filmes com quantidade disponível abaixo ou igual ao limite definido pelo usuário.</li>
  <li><strong>Listar Todo Histórico:</strong> Exibe todas as transações finalizadas, mostrando datetime e status.</li>
</ul>

<h2>✒️ Autor</h2>
<p>
  <strong>Saimon Ruan</strong><br>
  Projeto de desenvolvimento em Python.
</p>
