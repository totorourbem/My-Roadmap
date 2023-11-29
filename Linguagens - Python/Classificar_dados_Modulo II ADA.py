# -*- coding: utf-8 -*-

# Created on Tue Nov 21 15:43:41 2023

# @author: ricardojfrancisco

# menu classificar

# elif opçao == '7':

#      genero = input('Insira o gênero, M ou F (não obrigatório): ')
#      campo = input("Insira o campo ('altura', 'salario' ou 'idade'):")
#      medida = input('''
#      Insira a medida para:
#         - altura - 'centimetros' ou 'pes', sendo metro o padrão;
#      e para:
#       - salário - 'anual', sendo mensal o padrão):
#      ''')
#      de = input('Insira o valor inicial do intervalo: ')
#      ate = input('Insira o valor final do intervalo: ')
#      print(classificar_grupo(arquivo_json, medida, genero, campo, de, ate))


# Função classificadora

def classificar_grupo(arquivo_json, medida=None, genero=None, campo=None, de=None, ate=None):

    lista = carregar_dados(arquivo_json)

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


classificar_grupo(arquivo_json, medida='pes', genero='F',
                  campo='altura', de=5, ate=6)
