print('Bem vindo ao hotel!')

#solicitacao de dados check-in

#timer bom dia boa noite pc hour
novaPessoa = True
listaClientes = []


print('Bom dia, vamos começar seu cadastro')

while novaPessoa == True:
    pessoas = []
    nomePessoa = str(input('Qual seu nome completo? '))
    cpfPessoa = int(input('Qual seu cpf? '))
    numeroPessoal = int(input('Qual seu telefone? '))

    pessoas.append(nomePessoa)
    pessoas.append(cpfPessoa)
    pessoas.append(numeroPessoal)

    listaClientes.append(pessoas)
    
    novaPessoa = str(input('Deseja cadastrar outra pessoa? (S)/(N) '))
    if novaPessoa == 's':
        novaPessoa = True
    else:
        novaPessoa = False
        
#mascara numero de telefon/ cpf


print(listaClientes)

print("Consultando Cliente....")

# Tamanho da Lista Cliente
# print (len(listaClientes))

# Criando uma tabela com os dados cadastrado

# Imprime o cabeçalho da tabela
print("-" * 67)
# Imprime as Labels
print("|{:21}|{:21}|{:21}|".format(" Nome", " C.F.P.", " Telefone"))
print("-" * 67)

# Laço de repetição para percorrer a lista [listaClientes]
for i in range(0, len(listaClientes)):
    # Laço de repetição para percorrer a lista [pessoas]  
    for j in range(0, len(pessoas)):
        # Imprime a tabela com os dados dos hospedes
        print("|{:^20}".format(listaClientes[i][j]), end=' ')
        # Imprime um "|" no final da linha e cria a próxima linha
    print("|")
# Imprime a linha final da tabela
print("-" * 67)

# Variável que recebe o nome para consulta
consulta = str(input("Digite o nome do hospede para consulta: ")).strip()
# Variável para retorna da pesquiza
achou = 0
# Laço de repetição para percorrer a lista [listaClientes], na lista [pessoas] o nome
# sempre estara no indice 0
for c in range(0, len(listaClientes)):
    # Compara o nome da variável consulta com os dados da lista [pessoa]
    if consulta == listaClientes[c][0]:
        # Se encontrar o hospede a variável de retorno passa a valer maior que 0
        achou += 1

# Estrutura de desisão para hospede cadastrado ou não
if achou > 0:
    print("Hospede já cadastrado.")
else:
    print("Hospede não cadastrado.")
