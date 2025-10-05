# ARMAZENAMENTO

proximo_id_locacao = 1

catalogo_filmes = [
    {'codigo': 'PCH001', 'titulo': 'O Poderoso Chefão', 'categoria': 'Drama', 'preco_diaria': 5.00, 'qtd_disponivel': 3},
    {'codigo': 'INT002', 'titulo': 'Interestelar', 'categoria': 'Sci-Fi', 'preco_diaria': 7.50, 'qtd_disponivel': 5}
]

clientes = [
    {'cpf': '00000000000', 'nome': 'Saimon Ruan', 'telefone': '000000000'},
    {'cpf': '11111111111', 'nome': 'Maria Joana', 'telefone': '111111111'}
]

carrinhos_ativos = []

historico_locacoes = []

#############################################

def busca_filme_por_codigo(codigo):
    for filme in catalogo_filmes:
        if filme['codigo'] == codigo:
            return filme
    return None

def busca_cliente_por_cpf(cpf):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return cliente
    return None

def busca_carrinho_por_cpf(cpf):
    for carrinho_ativo in carrinhos_ativos:
        if carrinho_ativo['cpf_cliente'] == cpf:
            return carrinho_ativo
    return None


def exibir_menu():
    print("=== LOCADORACLI ===")
    print("[1] Catálogo")
    print("[2] Clientes")
    print("[3] Locações")
    print("[4] Relatorios")
    print("[0] Sair")

# FUNÇÕES DE CATALOGO (OPÇÃO 1)

def menu_catalogo():
    while True:
        print("=== CATÁLOGO FILMES ===")
        print("[1] Cadastrar Filme")
        print("[2] Lista de Filme")
        print("[3] Atualizar Estoque")
        print("[4] Remover Filme")
        print("[0] Volta")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_filme()
        elif opcao == '2':
            listar_filme()
        elif opcao == '3':
            atualizar_estoque()
        elif opcao == '4':
            remover_filme()   
        elif opcao == '0':
            break
        else:
            print("Opção Invalida")
            

def cadastrar_filme():
    print("=== Cadastro de Filme ===")
    
    while True:
        codigo = input("Código do filme: ").strip().upper()
        if busca_filme_por_codigo(codigo):
            print(f"ERRO: O código '{codigo}' já está em uso. Digite outro.")
        else:
            break

    titulo = input("Digite o nome do filme: ").strip().title()
    categoria = input("Digite a categoria do filme: ").strip().title()

    while True:
        try:
            preco_input = input("Preço da Diária: ").strip().replace(',', '.')
            preco_diaria = float(preco_input)
            if preco_diaria < 0:
                print("O preço da diária nao pode ser negativo. Tente novamente")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número para o preço.")

    while True:
        try:
            qtd_disponivel = int(input("Quantidade inicial de estoque: "))
            if qtd_disponivel < 0:
                print("A quantidade em estoque não pode ser negativo. Tente novamente")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número para o preço.")

    novo_filme = {
        'codigo': codigo,
        'titulo': titulo,
        'categoria': categoria,
        'preco_diaria': preco_diaria,
        'qtd_disponivel': qtd_disponivel
    }

    catalogo_filmes.append(novo_filme)
    print(f"SUCESSO: Filme '{titulo}' (Código: {codigo}) cadastrado.")

def listar_filme():
    if not catalogo_filmes:
        print("O catalogo de filme está vazio.")
        return
    
    print("=== Catalogo de Filmes ===")
    filmes_ordenados = sorted(catalogo_filmes, key=lambda x: x['titulo'])

    for filmes in filmes_ordenados:
        print(
            f"{filmes['codigo']} |"
            f" {filmes['titulo']} |"
            f" {filmes['categoria']} |"
            f" R$ {filmes['preco_diaria']} |"
            f" Quantidade: {filmes['qtd_disponivel']}"

        )

def atualizar_estoque():
    print("=== Atualizar Estoque ===")
    codigo_busca = input("Digite o código do filme:").strip().upper()
    filme_encontrado = busca_filme_por_codigo(codigo_busca)

    if not filme_encontrado:
        print(f"ERRO: Filme com código '{codigo_busca}' não encontrado")
        return

    titulo = filme_encontrado['titulo']

    while True:
        print(f"Filme: {titulo}. Estoque atual: {filme_encontrado['qtd_disponivel']}")
        print("[1] Adicionar unidades ao estoque")
        print("[2] Remover unidades do estoque")
        print("[0] Cancelar e Voltar")

        operacao = input("Escolha a operação: ").strip()

        if operacao == '0':
            print("Operação Cancelada.")
            return
        if operacao not in ('1' , '2'):
            print("Opção Inválida. Tente novamente")

        while True:
            try:
                quantidade = int(input("Digite a quantidade: "))
                if quantidade < 0:
                    print("A quantidade dever um numero positivo")
                    continue
                if operacao == '2':
                    if quantidade > filme_encontrado['qtd_disponivel']:
                        print(f"ERRO: Não é possível remover {quantidade} unidades. Estoque máximo disponível: {filme_encontrado['qtd_disponivel']}")
                        continue

                break

            except ValueError:
                print("Entrada invalida. Digite um numero inteiro")

        if operacao == '1':
            filme_encontrado['qtd_disponivel'] += quantidade
            print(f"SUCESSO: {quantidade} unidades adicionadas. Novo estoque de '{titulo}': {filme_encontrado['qtd_disponivel']} unidades.")
            return
        elif operacao == '2':
            filme_encontrado['qtd_disponivel'] -= quantidade
            print(f"SUCESSO: {quantidade} unidades removidas. Novo estoque de '{titulo}': {filme_encontrado['qtd_disponivel']} unidades.")
            return
def remover_filme():
    print("=== REMOVER FILME ===")
    codigo_busca = input("Digite o Código do filme que desejar remover: ").strip().upper()

    for i, filme in enumerate(catalogo_filmes):
        if filme['codigo'] == codigo_busca:
            del catalogo_filmes[i]
            print(f"SUCESSO: Filme '{filme['titulo']} (CÓDIGO: {codigo_busca}) removido")
            return
    print(f"ERRO: Filme com código '{codigo_busca}' não encontrado")

# FUNÇÕES DE CLIENTES (OPÇÃO 2)

def menu_cliente():
    
    while True:
        print("=== CLIENTES  ===")
        print("[1] Cadastrar Cliente")
        print("[2] Listar Clientes")
        print("[3] Remover Cliente")
        print("[0] Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            remover_clientes()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

def cadastrar_cliente():
    
    print("=== CADASTRAR CLIENTE ===")

    while True:
        cpf = input("CPF (apenas 11 numeros): ").strip()

        if len(cpf) != 11 or not cpf.isdigit():
            print("ERRO: O CPF deve conter exatamente 11 dígitos numéricos.")
        elif busca_cliente_por_cpf(cpf):
            print(f"ERRO: O CPF {cpf} já está cadastrado.")
        else:
            break

    nome = input("Nome do Cliente: ").strip().title()
    telefone = input("Telefone: ").strip()

    novo_cliente = {
        'cpf': cpf,
        'nome': nome,
        'telefone': telefone
    }
    clientes.append(novo_cliente)
    print(f"SUCESSO: Cliente '{nome}' (CPF: {cpf}) cadastrado.")

def listar_clientes():
    if not clientes:
        print ("O cadastro de clientes está vazio.")
        return
    print("=== LISTA DE CLIENTES ===")

    for cliente in clientes:
        print(
            f"{cliente['nome']} | "
            f"{cliente['cpf']} | "
            f"{cliente['telefone']}"
        )

def remover_clientes():
    print("=== REMOVER CLIENTES ===")

    cpf_busca = input("Digite o CPF do cliente que deseja remover: ").strip()

    locacao_ativa_encontrada = False

    for locacao in historico_locacoes:
        if locacao['cpf_cliente'] == cpf_busca and locacao['status'] == 'ATIVA':
            locacao_ativa_encontrada = True
            break
            
    if locacao_ativa_encontrada:
        print(f"ERRO: O cliente com CPF {cpf_busca} possui uma locação ATIVA.")
        print("A remoção está BLOQUEADA. O cliente deve devolver o(s) filme(s) primeiro.")
        return

    for i, cliente in enumerate(clientes):
        if cliente['cpf'] == cpf_busca:
            del clientes[i]
            print(f"SUCESSO: Cliente '{cliente['nome']}' (CPF: {cpf_busca}) removido.")
            return

    print(f"ERRO: Cliente com CPF {cpf_busca} não encontrado.")

# FUNÇÕES DE LOCAÇÕES (OPÇÃO 3)

def menu_locacoes():

    while True:
        print("=== LOCAÇÕES ===")
        print("[1] Iniciar/Zerar Locação")
        print("[2] Adicionar Filme ao Carrinho")
        print("[3] Remover Filme do Carrinho")
        print("[4] Ver Carrinho e Subtotal")
        print("[5] Finalizar Locação")
        print("[0] Voltar ao Menu Principal")

        opcao = input("Escola uma opção:  ")

        if opcao == '1':
            iniciar_locacao()
        elif opcao == '2':
            adicionar_filme_ao_carrinho()
        elif opcao == '3':
            remover_filme_do_carrinho()
        elif opcao == '4':
            ver_carrinho()
        elif opcao == '5':
            finalizar_locacao()
        elif opcao == '6':
            devolver_filmes()
        elif opcao == '0':
            break



def iniciar_locacao():
    print("=== INICIAR NOVA LOCAÇÃO ===")
    
    cpf_busca = input("Digite o CPF do cliente para iniciar a locação: ").strip()
    cliente = busca_cliente_por_cpf(cpf_busca)

    if not cliente:
        print(f"ERRO: Cliente com CPF {cpf_busca} não encontrado. Cadastre-o primeiro.")
        return
    
    carrinho_existente = busca_carrinho_por_cpf(cpf_busca)

    if carrinho_existente:
        print(f"ATENÇÃO: Cliente {cliente['nome']} já possui um carrinho ativo com {len(carrinho_existente['carrinho'])} item(ns).")
        opcao = input("Deseja ZERAR o carrinho atual e começar um novo? (S/N): ").strip().upper()

        if opcao == 'S':
            carrinho_existente['carrinho'] = []
            print("Carrinho zerado. Pronto para adicionar novos filmes")
        else:
            print("Continuando com o carrinho atual")

    else:
        novo_carrinho = {
            'cpf_cliente': cpf_busca,
            'carrinho': []
        }
        carrinhos_ativos.append(novo_carrinho)
        print(f"SUCESSO: Carrinho iniciado para {cliente['nome']}")

def adicionar_filme_ao_carrinho():
    print("=== ADICIONAR FILME ===")

    cpf_busca = input("Digite o CPF do cliente com carrinho ativo: ")
    carrinho_ativo = busca_carrinho_por_cpf(cpf_busca)

    if not carrinho_ativo:
        print(f"ERRO: Não há carrinho ativo para o CPF {cpf_busca}. Use a opção [1] Iniciar Locação.")
        return

    codigo_busca = input("Digite o Código do filme: ").strip().upper()
    filme_encontrado = busca_filme_por_codigo(codigo_busca)

    if not filme_encontrado:
        print(f"ERRO: Filme com código '{codigo_busca}' não encontrado no catálogo.")
        return

    if filme_encontrado['qtd_disponivel'] <= 0:
        print(f"ERRO: O filme '{filme_encontrado['titulo']}' está esgotado.")
        return
    
    while True:
        try:
            dias = int(input(f"Quantos dias de locação para o '{filme_encontrado['titulo']}'? "))
            if dias <= 0:
                print("ERRO: O número de dias deve ser um inteiro positivo.")
                continue
            break
        except ValueError:
            print("ERRO: Entrada inválida. Digite um número inteiro.")

    filme_ja_no_carrinho = None

    for item in carrinho_ativo['carrinho']:
        if item['codigo_filme'] == codigo_busca:
            filme_ja_no_carrinho = item
            break

    preco = filme_encontrado['preco_diaria']
    subtotal = preco * dias

    if filme_ja_no_carrinho:
        filme_ja_no_carrinho['dias'] += dias
        filme_ja_no_carrinho['subtotal'] += subtotal
        print(f"SUCESSO: Dias de locação atualizados. Total de dias para '{filme_encontrado['titulo']}': {filme_ja_no_carrinho['dias']}.")
    
    else:
        novo_item = {
            'codigo_filme': codigo_busca,
            'titulo': filme_encontrado['titulo'],
            'dias': dias,
            'preco_diaria': preco,
            'subtotal': subtotal
        }

        carrinho_ativo['carrinho'].append(novo_item)
        print(f"SUCESSO: '{filme_encontrado['titulo']}' adicionado ao carrinho por {dias} dia(s). Subtotal: R${subtotal:.2f}")

def remover_filme_do_carrinho():
    print("=== REMOVER FILME DO CARRINHO ===")

    cpf_busca = input("Digite o CPF do cliente com o carrinho ativo: ").strip()
    carrinho_ativo = busca_carrinho_por_cpf(cpf_busca)

    if not carrinho_ativo:
         print(f"ERRO: Não há carrinho ativo para o CPF {cpf_busca}.")
         return

    if not carrinho_ativo['carrinho']:
        print("Carrinho vazio! Não há itens para remover.")
        return
        
    print("=== Itens no Carrinho ===")

    for i, item in enumerate(carrinho_ativo['carrinho']):
        print(f"[{i + 1}] Código: {item["codigo_filme"]} | Título: {item['titulo']} | Dias: {item['dias']} | Subtotal: R${item['subtotal']:.2f}")

    codigo_remover = input("Digite o Código do filme que desejar remover: ").strip().upper()

    filme_removido = False

    for i, item in enumerate(carrinho_ativo['carrinho']):
        if item['codigo_filme'] == codigo_remover:
            titulo_removido = item['titulo']

            del carrinho_ativo['carrinho'][i]

            filme_removido = True
            print(f"SUCESSO: Filme '{titulo_removido}' removido do carrinho.")
            break
            
        if not filme_removido:
            print(f"ERRO: Filme com código '{codigo_remover}' não encontrado no carrinho.")

        if not carrinho_ativo['carrinho']:
            print("O carrinho está vazio.")

def ver_carrinho():
    print("=== VER CARRINHO ===")

    cpf_busca = input("Digite o CPF do cliente para ver o carrinho: ").strip()
    carrinho_ativo = busca_carrinho_por_cpf(cpf_busca)

    if not carrinho_ativo:
        print(f"ERRO: Não há carrinho ativo para o CPF {cpf_busca}.")
        return

    carrinho = carrinho_ativo['carrinho']

    if not carrinho:
        print("O carrinho está vazio.")
        return

    subtotal_total = 0.0
    
    print("=== ITENS NO CARRINHO ===")

    for item in carrinho:
        subtotal_total += item['subtotal']

        print(
            f"{item['codigo_filme']} |"
            f"{item['titulo']} |"
            f"R${item['preco_diaria']} |"
            f"Dias: {item['dias']} |"
            f"R${item['subtotal']}"
        )
    print("===================")
    print(f"SUBTOTAL TOTAL ESTIMADO: R${subtotal_total:.2f}")

def finalizar_locacao():
    global proximo_id_locacao
    print("=== FINALIZAR LOCAÇÃO ===")

    cpf_busca = input("Digite o CPF do cliente para finalizar a locação: ").strip().upper()
    carrinho_ativo = busca_carrinho_por_cpf(cpf_busca)

    if not carrinho_ativo:
        print(f"ERRO: Não há carrinho ativo ou o carrinho está vazio para o CPF {cpf_busca}.")
        return
    
    carrinho = carrinho_ativo['carrinho']
    subtotal = sum(item['subtotal'] for item in carrinho)

    print(f"Subtotal da Locação: R${subtotal}")

    desconto_porcentual = 0.0
    
    while True:
        try:
            input_desc = input("Digite o percetual de desconto (0 a 100): ").strip().replace(',', '.')
            
            if not input_desc:
                desconto_porcentual = 0.0
            else:
                desconto_porcentual = float(input_desc)

            if 0 <= desconto_porcentual <= 100:
                break
            else:
                print("ERRO: O desconto deve ser um valor entre 0 e 100.")
        except ValueError:
            print("ERRO: Entrada inválida. Digite um número.")

    desconto_valor = subtotal * (desconto_porcentual / 100)
    total_final = subtotal - desconto_valor

    print(f"Desconto Aplicado ({desconto_porcentual:.1f}%): R${desconto_valor:.2f}")
    print(f"TOTAL A PAGAR: R${total_final:.2f}")

    confirmacao = input("Confirmar finalição da locação? (S/N) ").strip().upper()

    if confirmacao != 'S':
        print("Finalização cancelada.")
        return
    
    estoque_atualizado_com_sucesso = True

    for item in carrinho:
        filme_no_catalogo = busca_filme_por_codigo(item['codigo_filme'])

        if filme_no_catalogo:
            if filme_no_catalogo['qtd_disponivel'] > 0:
                filme_no_catalogo['qtd_disponivel'] -= 1
            else:
               print(f"AVISO: O filme '{item['titulo']}' zerou o estoque antes da finalização. Locação registrada, mas estoque ficou em 0.")
        else:
            print(f"ERRO CRÍTICO: Filme com código {item['codigo_filme']} não encontrado no catálogo durante o débito de estoque.")
            estoque_atualizado_com_sucesso = False

    if estoque_atualizado_com_sucesso:

        nova_locacao_historico = {
            'id_locacao': proximo_id_locacao,
            'cpf_cliente': cpf_busca,
            'nome_cliente': busca_cliente_por_cpf(cpf_busca)['nome'],
            'total_bruto': subtotal,
            'desconto_aplicado': desconto_valor,
            'total_final': total_final,
            'status': 'ATIVA',
            'itens': carrinho
        }

        historico_locacoes.append(nova_locacao_historico)

        for i, cart in enumerate(carrinhos_ativos):
            if cart['cpf_cliente'] == cpf_busca:
                del carrinhos_ativos[i]
                break

        print(f"SUCESSO: Locação ID {proximo_id_locacao} finalizada com sucesso.")
        print(f"Total: R${total_final:.2f}. Estoque atualizado.")

        proximo_id_locacao += 1

    else:
      print("ERRO: A locação não foi registrada devido a um erro no estoque.")

def devolver_filmes():
    print("=== DEVOLUÇÃO DE FILMES ===")

    cpf_busca = input("Digite o CPF do cliente para processar a devolução: ").strip()
    
    locacao_para_devolver = None
    indice_locacao = -1
    
    for i, locacao in enumerate(historico_locacoes):
        if locacao['cpf_cliente'] == cpf_busca and locacao['status'] == 'ATIVA':
            locacao_para_devolver = locacao
            indice_locacao = i
            break
            
    if not locacao_para_devolver:
        print(f"ERRO: Não foi encontrada nenhuma locação ATIVA para o CPF {cpf_busca}.")
        return

    print(f"Locação encontrada (ID: {locacao_para_devolver['id_locacao']}) para o cliente {locacao_para_devolver['nome_cliente']}.")
    print(f"Total de itens a devolver: {len(locacao_para_devolver['itens'])}")
    confirmacao = input("Confirmar devolução desta locação? (S/N): ").strip().upper()
    
    if confirmacao != 'S':
        print("Devolução cancelada.")
        return
    
    itens_devolvidos = 0
    
    for item in locacao_para_devolver['itens']:
        codigo_filme = item['codigo_filme']
        filme_no_catalogo = busca_filme_por_codigo(codigo_filme)
        
        if filme_no_catalogo:
            filme_no_catalogo['qtd_disponivel'] += 1
            itens_devolvidos += 1
        else:
            print(f"AVISO: Filme com código {codigo_filme} não encontrado no catálogo. Estoque não pôde ser aumentado.")

    if itens_devolvidos > 0:
        historico_locacoes[indice_locacao]['status'] = 'DEVOLVIDA'
        print(f"SUCESSO: Devolução processada. {itens_devolvidos} item(s) devolvido(s).")
        print("Status da Locação atualizado para 'DEVOLVIDA'.")
    else:
        print("AVISO: Nenhuma alteração no estoque foi feita, mas o status da locação foi mantido.")


# FUNÇÕES DE RELATORIO (OPÇÃO 4)

def relatorio_total_faturado():
    if not historico_locacoes:
         print("Não há locações registradas para calcular o faturamento.")
         return    

    total_faturado = sum(locacao['total_final'] for locacao in historico_locacoes)

    print("=== RELATORIO: TOTAL FATURADO ===")
    print(f"P faturamento total é: R${total_faturado:.2f}")

def relatorio_ticket_medio():
    if not historico_locacoes:
        print("Não há locações registradas para calcular o faturamento.")
        return

    num_locacoes = len(historico_locacoes)

    total_faturado = sum(locacao['total_final'] for locacao in historico_locacoes)

    ticket_medio = total_faturado / num_locacoes

    print("=== RELATÓRIO: TICKET MÉDIO POR LOCAÇÃO ===")
    print(f"Total de Locações: {num_locacoes}")
    print(f"Ticket Médio: R${ticket_medio:.2f}")

def relatorio_filme_mais_alugados():
    print("=== RELATORIO: FILME MAIS ALUGAGOS ===")

    if not historico_locacoes:
         print("Não há locações registradas para calcular o faturamento.")
         return

    contagem_filme = {}

    for locacao in historico_locacoes:
        for item in locacao['itens']:
            titulo = item['titulo']
            contagem_filme[titulo] = contagem_filme.get(titulo, 0) + 1
    
    if not contagem_filme:
        print("Nenhum filme encontrado no histórico de locações.")
        return

    filme_mais_alugado = max(contagem_filme, key=contagem_filme.get)
    max_contagem = contagem_filme[filme_mais_alugado]

    print(f"O filme mais alugado é: '{filme_mais_alugado}'")
    print(f"Total de vezes alugado: {max_contagem}")

def relatorio_estoque_baixo():

    print("\n=== RELATÓRIO: ESTOQUE BAIXO ===")
    
    limiar = -1
    while limiar < 0:
        try:
            limiar_input = input("Defina o limiar de estoque: ").strip()
            if not limiar_input:
                print("ERRO: O limiar não pode ser vazio.")
                continue
            limiar = int(limiar_input)
            if limiar < 0:
                print("ERRO: O limiar deve ser um número inteiro não negativo.")
        except ValueError:
            print("ERRO: Entrada inválida. Digite um número inteiro.")
            
    filmes_baixo_estoque = []
    
    for filme in catalogo_filmes: 
        if filme['qtd_disponivel'] <= limiar:
            filmes_baixo_estoque.append(filme)

    if not filmes_baixo_estoque:
        print(f"Nenhum filme está com estoque abaixo ou igual a {limiar}.")
        return

    print(f"\n--- FILMES COM ESTOQUE <= {limiar} ---")
    print(f"{'CÓDIGO':<8} | {'TÍTULO':<30} | {'ESTOQUE ATUAL':<15}")
    print("-" * 55)
    
    for filme in filmes_baixo_estoque:
        print(
            f"{filme['codigo']} |"
            f"{filme['titulo']} |"
            f"{filme['qtd_disponivel']}"
        )
def relatorios():

    while True:
        print("=== RELATÓRIOS ===")
        print("[1] Total Faturado")
        print("[2] Ticket Médio por Locação")
        print("[3] Filme Mais Alugado")
        print("[4] Estoque Baixo")
        print("[0] Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            relatorio_total_faturado()
        elif opcao == '2':
            relatorio_ticket_medio()
        elif opcao == '3':
            relatorio_filme_mais_alugados() 
        elif opcao == '4':
            relatorio_estoque_baixo() 
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


def main():
    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_catalogo()
        elif opcao == '2':
            menu_cliente()
        elif opcao == '3':
            menu_locacoes()
        elif opcao == '4':
            relatorios()
        elif opcao == '0':
            break
        else:
            print("Opção Invalida")

if __name__ == "__main__":
    main()