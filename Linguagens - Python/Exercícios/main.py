# Importa as bibliotecas

import json
import csv
import time
import copy
from statistics import mean

# Função menu de opções, usuario escolhe as opções de 0 a 9, se 0 encerra o programa, se diferente desses, o programa pede para inserir um valor válido.
def Menu_de_opções(dados: list[dict], arquivo_json: str):

    while True:
        # time.sleep tem como finalidade estabelecer um intervalo temporaral de 0,5 segundos na exibição das opções do menu.
        print('1-Criar pessoa')
        time.sleep(0.5)
        print('2-Atualizar pessoa')
        time.sleep(0.5)
        print('3-Deletar pessoa')
        time.sleep(0.5)
        print('4-Exibir pessoa')
        time.sleep(0.5)
        print('5-Gerar estatísticas;')
        time.sleep(0.5)
        print('6-Gerar arquivo CSV;')
        time.sleep(0.5)
        print('7-Gerar classificação;')
        time.sleep(0.5)
        print('0-Encerrar programa.')
        time.sleep(0.5)

        opçao = input('\nO que deseja fazer? ')


        if opçao == '0':
          print('Programa encerrado!')
          break

        elif opçao == '1':
          print(criar_pessoa(dados, './dados_pessoa.json'))

        elif opçao == '2':
          print(atualizar_pessoa2(dados))

        elif opçao == '3':
          print(deletar_pessoa(dados))

        elif opçao == '4':
          print(exibir_pessoa(dados))

        elif opçao == '5':
          print(gerar_estatisticas(dados))

        elif opçao == '6':
          print(gerar_csv(dados))

        elif opçao == '7':
          genero = input('Insira o gênero, M ou F (não obrigatório): ')
          campo = input("Insira o campo ('altura', 'salario' ou 'idade'):")
          medida = input('''
	        Insira a medida (não obrigatório) para:
   		      - altura - 'centimetros' ou 'pes', sendo metro o padrão;
		      e para:
		        - salário - 'anual', sendo mensal o padrão):
		        ''')
          de = input('Insira o valor inicial do intervalo: ')
          ate = input('Insira o valor final do intervalo: ')
          classificar_grupo(arquivo_json, genero, campo, medida, de, ate)


        else:
            print('Opção invalida!')

# Carregar dados do arquivo JSON
def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado. Criando um novo arquivo.")
        return []

# Salvar Dados em um Arquivo JSON
def salvar_arquivo(dados: list[dict], arquivo_json: dict) -> bool:
    try:
        with open(arquivo_json, 'w') as arquivo:
            arquivo.write(json.dumps(dados))
            return True
    except Exception:
        return False

    

# Entradas
def obter_nome() -> str:
    return input('Informe o nome:').title()

def obter_sobrenome() -> str:
    return input('Informe o sobrenome:').title()

def obter_idade() -> int:
    while True:
        try:
            idade = int(input('Informe a idade: '))
            if 18 <= idade <= 120:
                return idade
            else:
                print("A idade deve estar entre 18 e 120 anos.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def obter_sexo() -> str:
    while True:
        sexo = input(('Informe o sexo (F para Feminino, M para Masculino ou O para Outros): ')).capitalize()
        if sexo in ['F', 'M', 'O']:
            return sexo
        else:
            print("Por favor, digite 'Feminino' ou 'Masculino'.")

def obter_altura() -> float:
    while True:
        try:
            altura = float(input('Informe a altura (m): '))
            if altura > 0:
                return altura
            else:
                print("A altura deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico.")

def obter_salario() -> float:
    while True:
        try:
            salario = float(input('Informe o salário: '))
            if salario > 0:
                return salario
            else:
                print("O salário deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico.")



def exibir_dados(pessoas: list[dict]) -> str:
    if not pessoas:
        return "Nenhuma pessoa para exibir."

    resultados = []
    for pessoa in pessoas:
        resultado_pessoa = '\n'.join([f"{chave.capitalize()}: {valor}" for chave, valor in pessoa.items()])
        resultados.append(resultado_pessoa)

    return "\n\n".join(resultados)


def buscar_pessoa(dados: list[dict], nome: str, sobrenome: str) -> list[dict]:
    encontradas = [pessoa for pessoa in dados if pessoa['nome'] == nome and pessoa['sobrenome'] == sobrenome]
    if not encontradas:
        print(f"Pessoa não encontrada: {nome} {sobrenome}")
    return encontradas


def criar_pessoa(dados: list[dict], arquivo_json: str) -> bool:
    try:
        pessoa = {
            'nome': obter_nome(),
            'sobrenome': obter_sobrenome(),
            'idade': obter_idade(),
            'sexo': obter_sexo(),
            'altura': obter_altura(),
            'salario': obter_salario()
        }

        dados.append(pessoa)
        if salvar_arquivo(dados, arquivo_json):
            return True

    except ValueError as e:
        pass

    return False



def deletar_pessoa(dados: list[dict], arquivo_json: str) -> bool:
    nome = obter_nome()
    sobrenome = obter_sobrenome()
    pessoas_encontradas = buscar_pessoa(dados, nome, sobrenome)

    if not pessoas_encontradas:
        return False

    if len(pessoas_encontradas) > 1:
        return False

    pessoa_encontrada = pessoas_encontradas[0]
    dados.remove(pessoa_encontrada)

    if salvar_arquivo(dados, arquivo_json):
        return True
    else:
        return False



def atualizar_pessoa(dados: list[dict], arquivo_json: str) -> bool:
    nome = obter_nome()
    sobrenome = obter_sobrenome()
    pessoas_encontradas = buscar_pessoa(dados, nome, sobrenome)

    if not pessoas_encontradas:
        return False

    if len(pessoas_encontradas) == 1:
        pessoa_encontrada = pessoas_encontradas[0]

        pessoa_encontrada.update({
            'idade': obter_idade(),
            'sexo': obter_sexo(),
            'altura': obter_altura(),
            'salario': obter_salario()
        })

        if salvar_arquivo(dados, arquivo_json):
            return True
        else:
            return False
    else:
        return False

def exibir_pessoa(dados: list[dict], arquivo_json: str) -> bool:
    nome = obter_nome()
    sobrenome = obter_sobrenome()
    pessoas_encontradas = buscar_pessoa(dados, nome, sobrenome)
    print(exibir_dados(pessoas_encontradas))


def obter_campos_para_atualizar() -> list:
    campos_para_atualizar = []
    while True:
        campo = input("Digite o campo que deseja atualizar (ou digite 'fim' para encerrar): ").lower()
        if campo == 'fim':
            break
        campos_para_atualizar.append(campo)
    return campos_para_atualizar


def atualizar_pessoa2(dados: list[dict], arquivo_json: str) -> bool:
    nome = obter_nome()
    sobrenome = obter_sobrenome()
    pessoas_encontradas = buscar_pessoa(dados, nome, sobrenome)

    if not pessoas_encontradas:
        return False

    if len(pessoas_encontradas) == 1:
        pessoa_encontrada = pessoas_encontradas[0]

        campos_para_atualizar = obter_campos_para_atualizar()

        for campo in campos_para_atualizar:
            if campo == 'idade':
                pessoa_encontrada['idade'] = obter_idade()
            elif campo == 'sexo':
                pessoa_encontrada['sexo'] = obter_sexo()
            elif campo == 'altura':
                pessoa_encontrada['altura'] = obter_altura()
            elif campo == 'salario':
                pessoa_encontrada['salario'] = obter_salario()

        if salvar_arquivo(dados, arquivo_json):
            return True
        else:
            return False
    else:
        return False
    

# Função classificadora

def classificar_grupo(arquivo_json, medida=None, genero=None, campo=None, de=None, ate=None):

    lista = arquivo_json

    def mensagem():
        print('''   ****ATENÇÃO****
      Para comparações de intervalos numericos são necessários os seguintes argumentos:
       * 'Lista' (obrigatório): a lista de dados a ser analisada
       * 'campo' (obrigatório): O campo da lista ao qual vai se aplicar o filtro;
      E, ao menos um dos dois abaixo:
       * 'de': valor do qual o intervalo começa;
       * 'ate' : valor do qual o intervalo termina
      Lembarndo que ambos valores acimasão exclusivos, ou seja, não entram no intervalo de comparação.
      ''')

# Função para mostrar conversões de altura em imperial x sistema métrico em alteraer os registros, apenas para fins de classificação
# Essa parada de medidas pode ser importate para alguns nichos, como vesturário, por exemplo

    def conversor_tamanho(medida, lista):
        if medida == 'centimetros':
            mapeados = map(lambda x: x['altura'] * 100, lista)
        elif medida == 'polegadas':
            mapeados = map(lambda x: round(x['altura'] / 0.0254, 2), lista)
        elif medida == 'pes':
            mapeados = map(lambda x: round(x['altura'] / 0.3048, 2), lista)
        else:
            print('Conversão inválida!')
        return (list(mapeados))

    def atualizar_altura(medida, lista):
        dados_copia = copy.deepcopy(lista)
        for dicionario in dados_copia:
            altura_convertida = conversor_tamanho(medida, [dicionario])[0]
            dicionario['altura'] = altura_convertida
        return dados_copia

# funções para mostrar conversão de salário para anual. sem alteraer os registros, apenas para fins de classificação
# Permite que futuramente se aplique uma API, por exemplo, e converta essses cvalores em outras moedas

    def conversor_salario(medida, lista):
        if medida == 'anual':
            mapeados = map(lambda x: x['salario'] * 12, lista)
        else:
            pass
        return (list(mapeados))

    def atualizar_salario(medida, lista):
        dados_copia = copy.deepcopy(lista)
        for dicionario in dados_copia:
            salario_convertido = conversor_salario(medida, [dicionario])[0]
            dicionario['salario'] = salario_convertido
        return dados_copia

# Funções de filtro de intervalo e gênero (pois a que consta no trabalho é para quantificar por gêmnero)
    def filtrar_genero(genero, lista):
        filtrados = filter(lambda x: x['sexo'] == genero, lista)
        return (list(filtrados))

    def filtrar_numericos_faixa(campo, de, ate, lista):
        filtrados = filter(lambda x: de < x[campo] < ate, lista)
        return (list(filtrados))

    def filtrar_numericos_ate(campo, ate, lista):
        filtrados = filter(lambda x: x[campo] < ate, lista)
        return (list(filtrados))

    def filtrar_numericos_partindo(campo, de, lista):
        filtrados = filter(lambda x: de < x[campo], lista)
        return (list(filtrados))

# Aqui entra a classificação em si, tá marretado, mas funciona

    try:

        if (genero != None and campo == 'salario' and medida != None):
            lista_atualizada = filtrar_genero(genero, lista)
            lista_atualizada2 = atualizar_salario(medida, lista_atualizada)
            if de != None and ate != None:
                return filtrar_numericos_faixa('salario', de, ate, lista_atualizada2)
            elif de != None:
                return filtrar_numericos_partindo('salario', de, lista_atualizada2)
            elif ate != None:
                return filtrar_numericos_ate('salario', ate, lista_atualizada2)
            else:
                mensagem()
        elif (genero != None and campo == 'salario' and medida == None):
            lista_atualizada = filtrar_genero(genero, lista)
            if de != None and ate != None:
                return filtrar_numericos_faixa('salario', de, ate, lista_atualizada)
            elif de != None:
                return filtrar_numericos_partindo('salario', de, lista_atualizada)
            elif ate != None:
                return filtrar_numericos_ate('salario', ate, lista_atualizada)
            else:
                mensagem()
        elif (genero != None and campo == 'altura' and medida != None):
            lista_atualizada = filtrar_genero(genero, lista)
            lista_atualizada2 = atualizar_altura(medida, lista_atualizada)
            if de != None and ate != None:
                return filtrar_numericos_faixa('altura', de, ate, lista_atualizada2)
            elif de != None:
                return filtrar_numericos_partindo('altura', de, lista_atualizada2)
            elif ate != None:
                return filtrar_numericos_ate('altura', ate, lista_atualizada2)
            else:
                mensagem()
        elif (genero != None and campo == 'altura' and medida == None):
            lista_atualizada = filtrar_genero(genero, lista)
            if de != None and ate != None:
                return filtrar_numericos_faixa('altura', de, ate, lista_atualizada)
            elif de != None:
                return filtrar_numericos_partindo('altura', de, lista_atualizada)
            elif ate != None:
                return filtrar_numericos_ate('altura', ate, lista_atualizada)
            else:
                mensagem()
        else:
            mensagem()

    except ValueError:
        print('Valores fora de alcance da amostra!')
        mensagem()
    except:
        mensagem()


#classificar_grupo(arquivo_json, medida='pes', genero='F', campo='altura', de=5, ate=6)

# Máximo e mínimo de salário
def salario_max_min(dados, maximo=True):
    if not dados:
        return "Não há dados a serem exibidos"
    lista_pessoas = [(pessoa["nome"], pessoa["salario"]) for pessoa in dados]
    max_salario = max(lista_pessoas, key=lambda x: x[1]) if maximo else min(lista_pessoas, key=lambda x: x[1])
    return max_salario

# Quantidade de pessoas pelo sexo
def pessoas_sexo(dados, sexo):
    lista_sexo = [pessoa for pessoa in dados if pessoa["sexo"] == sexo]
    return len(lista_sexo)


def calcular_media(dados, campo):

    lista_valores = [pessoa[campo] for pessoa in dados]
    media = mean(lista_valores)
    media_arredondada = round(media, 2)
    return media_arredondada

# Média de altura
def calculo_altura (dados, altura):
    lista_altura_media = list(filter(lambda x: x['altura'] == altura_media, dados))

    if not lista_altura_media:
      return None

    else:
      altura_soma == sum(lista_altura)
      media_altura = altura_soma/ len(lista_altura_media)
      return media_altura

# Média de salário
def calculo_salario (dados, salario):
    lista_salario_media = list(filter(lambda x: x['salario'] == salario_media, dados))

    if not lista_salario_media:
        return None
    else:
      salario_soma = sum(lista_salario)
      media_salario = salario_soma/ len(lista_salario_media)
      return media_salario
    
# Função para calcular estatísticas
def gerar_estatisticas(dados):
    pessoas_f = pessoas_sexo(dados,'F')
    pessoas_m = pessoas_sexo(dados,'M')
    max_nome, max_salario = salario_max_min(dados,maximo=True)
    min_nome, min_salario = salario_max_min(dados, maximo=False)
    print("\n\n dados para altura:", dados[:20])
    media_altura =  calcular_media(dados,'altura')
    media_salario = calcular_media(dados,'salario')
    # print("\n\nDADOS EM ESTATIS:\n", dados[:20])

    

    # Verificar se a função já foi chamada antes
    try:
        with open('estatisticas.csv', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Lê os cabeçalhos, se existirem
            arquivo_existente = True
    except FileNotFoundError:
        arquivo_existente = False

    # Adicionar dados ao arquivo CSV
    with open('estatisticas.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            "pessoas_f",
            "pessoas_m",
            "max_salario_nome",
            "max_salario",
            "min_salario_nome",
            "min_salario",
            "media_altura",
            "media_salario"
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Se o arquivo não existir, escreva os cabeçalhos
        if not arquivo_existente:
            writer.writeheader()

        # Escreva os dados
        writer.writerow({
            "pessoas_f": pessoas_f,
            "pessoas_m": pessoas_m,
            "max_salario_nome": max_nome,
            "max_salario": max_salario,
            "min_salario_nome": min_nome,
            "min_salario": min_salario,
            "media_altura": media_altura,
            "media_salario": media_salario
        })
    # codigo excluia dados
    # return {
    #     "pessoas_f": pessoas_f,
    #     "pessoas_m": pessoas_m,
    #     "max_salario_nome": max_nome,
    #     "max_salario": max_salario,
    #     "min_salario_nome": min_nome,
    #     "min_salario": min_salario,
    #     "media_altura": media_altura,
    #     "media_salario": media_salario
    # }


# Função para obter a média total dos salários
def calcular_media_salarios(dados):
    if not dados:
        return None

    salario_soma = sum(pessoa['salario'] for pessoa in dados)
    media_salarios = salario_soma / len(dados)
    return media_salarios

# Exemplo de uso
# dados = [
#     {"nome": "João", "salario": 3000, "altura": 1.65, 'sexo': 'M'},
#     {"nome": "Maria", "salario": 4000, "altura": 1.85, 'sexo': 'F'},
#     {"nome": "Carlos", "salario": 3500, "altura": 1.70, 'sexo': 'M'},
#     {"nome": "Ana", "salario": 3000, "altura": 1.75, 'sexo': 'F'}
# ]

dados = carregar_dados('./dados_pessoa.json')
print("DADOS", dados[:20])

media_salarios = calcular_media_salarios(dados)

if media_salarios is not None:
    print(f"Média salarial total: {media_salarios}")
else:
    print("Nenhum registro encontrado para calcular a média salarial")




def gerar_csv(estatisticas):
    # Verificar se o arquivo CSV já existe
    try:
        with open('estatisticas.csv', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Lê os cabeçalhos, se existirem
            arquivo_existente = True
    except FileNotFoundError:
        arquivo_existente = False

    # Adicionar dados ao arquivo CSV
    with open('estatisticas.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            "pessoas_f",
            "pessoas_m",
            "max_salario_nome",
            "max_salario",
            "min_salario_nome",
            "min_salario",
            "media_altura",
            "media_salario"
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Se o arquivo não existir, escreva os cabeçalhos
        if not arquivo_existente:
            writer.writeheader()

        # Escreva os dados
        writer.writerow(estatisticas)

# definiu duas vezes, desconsiderando essa

# def gerar_estatisticas(dados):
#     pessoas_f = pessoas_sexo(dados, 'F')
#     pessoas_m = pessoas_sexo(dados, 'M')
#     max_nome, max_salario = salario_max_min(dados, maximo=True)
#     min_nome, min_salario = salario_max_min(dados, maximo=False)
#     media_altura = calcular_media(dados, 'altura')
#     media_salario = calcular_media(dados, 'salario')

#     estatisticas = {
#         "pessoas_f": pessoas_f,
#         "pessoas_m": pessoas_m,
#         "max_salario_nome": max_nome,
#         "max_salario": max_salario,
#         "min_salario_nome": min_nome,
#         "min_salario": min_salario,
#         "media_altura": media_altura,
#         "media_salario": media_salario
#     }

#     return estatisticas

# Exemplo de uso no menu
# dados = [...]  # Seus dados aqui

# opcao = input("Digite a opção (1 para gerar estatísticas, 2 para gerar CSV): ")



Menu_de_opções(dados, './dados_pessoa.json')

# if opcao == '1':
#     estatisticas = gerar_estatisticas(dados)
#     print("Estatísticas geradas:", estatisticas)    
# elif opcao == '2':
#     estatisticas = gerar_estatisticas(dados)
#     gerar_csv(estatisticas)
#     print("Arquivo CSV gerado.")
# else:
#     print("Opção inválida.")