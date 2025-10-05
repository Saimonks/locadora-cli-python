<h1>🎥 Locadora CLI — Sistema de Locação de Filmes via Linha de Comando</h1>

<h2>📌 Visão Geral</h2>
<p>
  Este projeto é um sistema de gerenciamento de uma locadora de filmes desenvolvido em <strong>Python</strong>, com interface de linha de comando (CLI). Ele permite o <strong>cadastro de filmes e clientes</strong>, o controle completo do ciclo de locação (início, adição ao carrinho, finalização e devolução), além da geração de <strong>relatórios financeiros e de estoque</strong>.
</p>
<p>
  O sistema utiliza <strong>estruturas de dados nativas do Python</strong>, como listas e dicionários, proporcionando uma experiência leve e funcional.
</p>

<h2>🚀 Como Executar</h2>

<h3>✔️ Pré-requisitos</h3>
<ul>
  <li>Python 3.6 ou superior instalado em sua máquina.</li>
</ul>

<h3>▶️ Passos para executar:</h3>
<ol>
  <li>Salve todo o código em um arquivo chamado, por exemplo, <code>locadora.py</code>.</li>
  <li>Abra o terminal (Prompt de Comando, PowerShell ou Terminal do VS Code) no diretório onde o arquivo está salvo.</li>
  <li>Execute o comando abaixo:</li>
</ol>

<pre><code>python locadora.py</code></pre>

<p>O menu principal será exibido, e você poderá interagir com o sistema diretamente pela CLI.</p>

<h2>📋 Funcionalidades</h2>
<p>O sistema é dividido em <strong>quatro módulos principais</strong>, acessados pelo menu principal:</p>

<h3>1. 🎬 Catálogo de Filmes</h3>
<ul>
  <li><strong>Cadastrar Filme:</strong> Adiciona novos filmes com validação de código único.</li>
  <li><strong>Validação Numérica:</strong> Garante valores positivos para preço e estoque (aceita <code>,</code> ou <code>.</code> como separador decimal).</li>
  <li><strong>Listar Filmes:</strong> Exibe todos os títulos em ordem alfabética.</li>
  <li><strong>Atualizar Estoque:</strong> Permite adicionar ou remover unidades, com bloqueio para evitar estoque negativo.</li>
  <li><strong>Remover Filme:</strong> Exclui um filme do catálogo.</li>
</ul>

<h3>2. 👤 Gestão de Clientes</h3>
<ul>
  <li><strong>Cadastrar Cliente:</strong> Registra clientes com CPF, nome e telefone.</li>
  <li><strong>Validação de CPF:</strong> Verifica se o CPF tem exatamente 11 dígitos e é único.</li>
  <li><strong>Listar Clientes:</strong> Mostra todos os clientes em ordem de registro.</li>
  <li><strong>Remover Cliente:</strong> Só é possível se o cliente não possuir locações ativas.</li>
</ul>

<h3>3. 📦 Locações</h3>
<ul>
  <li><strong>Iniciar/Zerar Carrinho:</strong> Cria um novo carrinho para o cliente.</li>
  <li><strong>Adicionar Filme:</strong> Adiciona títulos ao carrinho, verificando o estoque disponível.</li>
  <li><strong>Finalizar Locação:</strong> Aplica descontos, registra a transação e atualiza o estoque.</li>
  <li><strong>Devolver Filme:</strong> Encerra a locação, atualiza o estoque e muda o status para “DEVOLVIDA”.</li>
</ul>

<h3>4. 📊 Relatórios</h3>
<ul>
  <li><strong>Total Faturado:</strong> Soma de todas as locações finalizadas.</li>
  <li><strong>Ticket Médio:</strong> Média de valor por locação.</li>
  <li><strong>Filme Mais Alugado:</strong> Identifica o título com maior número de aluguéis.</li>
  <li><strong>Estoque Baixo:</strong> Lista filmes com estoque inferior ao limite definido pelo usuário.</li>
</ul>

<h2>🛠️ Estrutura de Dados Utilizada</h2>

<table>
  <thead>
    <tr>
      <th>Variável</th>
      <th>Tipo</th>
      <th>Finalidade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>catalogo_filmes</code></td>
      <td><code>list[dict]</code></td>
      <td>Detalhes de cada filme e seu estoque.</td>
    </tr>
    <tr>
      <td><code>clientes</code></td>
      <td><code>list[dict]</code></td>
      <td>Dados de todos os clientes cadastrados.</td>
    </tr>
    <tr>
      <td><code>carrinhos_ativos</code></td>
      <td><code>list[dict]</code></td>
      <td>Carrinhos de locação em andamento.</td>
    </tr>
    <tr>
      <td><code>historico_locacoes</code></td>
      <td><code>list[dict]</code></td>
      <td>Histórico de todas as locações (ATIVA ou DEVOLVIDA).</td>
    </tr>
    <tr>
      <td><code>proximo_id_locacao</code></td>
      <td><code>int</code></td>
      <td>ID incremental para locações.</td>
    </tr>
  </tbody>
</table>

<h2>🤝 Autor</h2>
<p>
  Desenvolvido por <strong>Saimon Ruan Alves Moreira</strong><br>
  Trabalho acadêmico da disciplina <em>Paradigmas de Linguagens de Programação (Python)</em> — Estácio.
</p>
