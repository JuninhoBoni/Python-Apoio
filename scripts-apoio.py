"""
    O script-apoio.py tem o objetivo basico de inserir itens de uso basico e frequentes no ambiente de trabalho atual
"""
__version__ = '0.1'
__author__ = 'Daniel Alves Dias Junior'

import json
import os
import sys
from datetime import *
from modulos.log import Log


def main():
    log.info(f"INICIOU MAIN")
    print(dicionario['json_config']["data_execucao_manual"])
    log.info(f"FINALIZOU MAIN")


if __name__ == "__main__":
    # Declara dicionário que armazenará dados comuns em outras classes
    dicionario = {}
    dicionario["inicio"] = datetime.now()
    dicionario["programa_nome"] = os.path.basename(__file__)
    dicionario["programa_diretorio"] = os.path.abspath(__file__)

    # Caso não exista, o .py, define que o arquivo foi compilado para .exe
    if not os.path.isfile(os.path.abspath(__file__)):
        dicionario["programa_diretorio"] = f'{dicionario["programa_diretorio"][:-3]}.exe'

    # Seta o diretório e nome do arquivo de configuração externa
    json_config = f'{dicionario["programa_diretorio"][:-3]}.json'
    with open(json_config, 'r') as json_arquivo:
        dicionario['json_config'] = json.load(json_arquivo)

    # Prepara a classe log e insere-a no dicionário
    log = Log()
    log.dicionario = dicionario
    dicionario['log'] = log
    log.carregar()

    # Insere no log o inicio do programa
    log.info("X" + f' PROGRAMA {dicionario["programa_nome"][:-3]} - v.{__version__} - INICIADO '.center(120, "-") + "X")
    log.info("X" + f' DATA DE COMPILAÇÃO - {datetime.fromtimestamp(os.path.getctime(dicionario["programa_diretorio"]))} '.center(120,"-") + "X")

    main()
 
    execucao_total = datetime.now() - dicionario["inicio"]
    log.info("X"+f' TEMPO DE EXECUÇÃO: {execucao_total} '.center(120, "-")+"X")
    log.info("X"+' PROGRAMA FINALIZADO COM SUCESSO '.center(120, "-")+"X")
    sys.exit(0)