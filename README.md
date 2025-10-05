<h1>🍿 LOCADORA CLI - Sistema de Gestão de Filmes</h1>

<h2>📌 Sobre o Projeto</h2>
<p>
  Este é um sistema completo para gerenciamento de uma locadora de filmes, desenvolvido em <strong>Python</strong> (utilizando <code>datetime</code> e funcionalidades built-in) e operado via Interface de Linha de Comando (CLI).<br>
  O foco principal é a <strong>segurança de dados</strong> e a <strong>validação robusta</strong> em todo o ciclo de locação.
</p>

<h2>🚀 Como Iniciar o Sistema</h2>

<h3>✔️ Pré-requisitos</h3>
<ul>
  <li>Git instalado.</li>
  <li>Python 3 ou superior.</li>
</ul>

<h3>▶️ Execução</h3>
<ol>
  <li>Clone o repositório para sua máquina.</li>
  <li>No terminal, navegue até a pasta do projeto.</li>
  <li>Execute o sistema com o comando:
    <pre><code>python locadora.py</code></pre>
  </li>
</ol>

<h2>✨ Funcionalidades Detalhadas</h2>

<h3>1. 🎬 Catálogo de Filmes</h3>
<table>
  <thead>
    <tr>
      <th>Funcionalidade</th>
      <th>Destaque de Validação</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cadastrar</td>
      <td>Garante que o código é único e que os valores são numéricos (aceita "," ou "." como decimal).</td>
    </tr>
    <tr>
      <td>Atualizar Estoque</td>
      <td>Bloqueia a remoção de unidades que resultem em estoque negativo.</td>
    </tr>
    <tr>
      <td>Exportar para as Planilhas</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

<h3>2. 👤 Clientes</h3>
<table>
  <thead>
    <tr>
      <th>Funcionalidade</th>
      <th>Destaque de Segurança</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cadastrar</td>
      <td>CPF deve ser único e ter exatamente 11 dígitos numéricos.</td>
    </tr>
    <tr>
      <td>Remover Cliente</td>
      <td>⛔ BLOQUEIO: Não permite remoção se o cliente possuir locação com status ATIVA.</td>
    </tr>
    <tr>
      <td>Exportar para as Planilhas</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

<h3>3. 🛒 Locações (Ciclo Completo)</h3>
<p>Este módulo registra o <strong>tempo exato da transação</strong> e gerencia o estoque.</p>
<table>
  <thead>
    <tr>
      <th>Funcionalidade</th>
      <th>Detalhe</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Finalizar Locação</td>
      <td>Usa o módulo <code>datetime</code> para registrar data/hora exata. Status definido como ATIVA.</td>
    </tr>
    <tr>
      <td>Devolver Filmes</td>
      <td>Encontra a locação ativa, aumenta o estoque (<code>qtd_disponivel += 1</code>) e atualiza o status para DEVOLVIDA.</td>
    </tr>
    <tr>
      <td>Exportar para as Planilhas</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

<h3>4. 📊 Relatórios (Análise Gerencial)</h3>
<table>
  <thead>
    <tr>
      <th>Relatório</th>
      <th>Detalhe</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Listar Todo Histórico</td>
      <td>Permite visualizar todas as transações, incluindo datetime e status (ATIVA/DEVOLVIDA).</td>
    </tr>
    <tr>
      <td>Total Faturado & Ticket Médio</td>
      <td>Cálculos financeiros essenciais.</td>
    </tr>
    <tr>
      <td>Filme Mais Alugado</td>
      <td>Contagem total de cada título no histórico.</td>
    </tr>
    <tr>
      <td>Estoque Baixo</td>
      <td>Lista filmes abaixo de um limite definido pelo usuário.</td>
    </tr>
    <tr>
      <td>Exportar para as Planilhas</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

<h2>🛠️ Estrutura de Dados Globais</h2>
<table>
  <thead>
    <tr>
      <th>Variável</th>
      <th>Função de Controle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>historico_locacoes</code></td>
      <td>Armazena transações com o campo status (ATIVA/DEVOLVIDA).</td>
    </tr>
    <tr>
      <td><code>proximo_id_locacao</code></td>
      <td>Gerador sequencial de IDs únicos.</td>
    </tr>
    <tr>
      <td>Exportar para as Planilhas</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

<h2>✒️ Autor</h2>
<p>
  <strong>Saimonks</strong><br>
  Projeto de desenvolvimento para <em>[Nome da Disciplina/Faculdade]</em>
</p>
