import logging
from datetime import datetime
from pathlib import Path


class Log:

    def carregar(self):
        agora = datetime.now()

        log_diretorio = f'{self.dicionario["json_config"]["diretorio"]["log"]}/{agora.year:04d}{agora.month:02d}{agora.day:02d}/'

        log_nome = f'{self.dicionario["programa_nome"]}_{agora.hour:02d}{agora.minute:02d}.LOG'

        Path(log_diretorio).mkdir(parents=True, exist_ok=True)

        logging.basicConfig(filename=f'{log_diretorio}{log_nome}',
                            format='%(asctime)s -- %(message)s', datefmt='%d/%m/%Y %H:%M:%S', level=logging.DEBUG)

    def info(self, mensagem):
        # Mosta na tela as informações informadas pelo sistema
        print(mensagem)
        logging.info(mensagem)

    def error(self, mensagem):
        print(mensagem)
        logging.error(mensagem)
        erro = "X"+' PROGRAMA FINALIZADO COM ERRO '.center(120, "-")+"X"
        logging.error(erro)
        print(erro)
