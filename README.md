# SCRIPTS-APOP

  Projeto desenvolvido em Python3.9 compilado pelo cx-Freeze==6.5.3 para Windows.

## Objetivo  
  
  Criar diversos scripts de apoio para as execuções no dia-a-dia

## Instalação do ambiente de desenvolvimento:
  
  Instalar python3.9
    Observar nas opções de instalação, a inserção do python nas variáveis de sistema.
    É recomendado instalar o python com a opção que disponibiliza-o à todos os usuários do Windows, pois desta forma a instalação é realizada no diretório padrão dos programas do Windows.
  O ambiente abaixo foi criado a partir do powershell dentro do Visual Studio com as extenções abaixo:
    Magic Python
    Notepad++ keymap
    PowerShell
    Pylance
    Python
    Python Extension Pack
    Visual Studio IntelliCode

  Executar o comando abaixo. Este comando cria o ambiente de desenvolvimento, com isso possibilita instalar somente as bibliotecas necessárias para o projeto, facilitando na compilação.
    python -m venv scripts
  Executar o comando abaixo para activar o ambiente virtual.
    scripts\Scripts\activate
  Executar o comando abaixo para instalar as bibliotecas que serão utilizadas no projeto.
    pip install -r requirements.txt
  Ambiente de desenvolvimento criado. É importante notar que qualquer inserção de biblioteca no projeto, é necesário rodar o comando abaixo para atualizar o requirements.txt.
    pip freeze > requirements.txt 

## Compilação
  
  A referência para execução do compilador é que o arquivo icone, json e o python principal tenham o mesmo nome e existam.
  Caso haja inserção de bibliotecas, inserir a mesma na lista 'packages'.
  Para compilar, executar o comando abaixo:
    python compilar.py build
  Será gerado um diretório build\exe.win-amd64-3.9\ dentro do diretório do projeto. Todos os itens dentro deste diretório devem seguir juntos para que o peojeto funcione corretamente.
  Caso seja necessário realizar uma nova compilação e NÃO HAJA alterações de bibliotecas, os arquivos que deverão ser copiados são:
    O .exe dentro do diretório acima
    O arquivo library.zip que fica dentro do diretório lib

## Tabela Oracle

CREATE TABLE EDI_RELATORIOS_CARGA (
    ID                      NUMBER(10),
    ARQUIVO_LOG             VARCHAR2(100)   NOT NULL,
    ARQUIVO_ZIP             VARCHAR2(100)   ,
    ARQUIVO_NOME            VARCHAR2(100)   NOT NULL,
    QUANTIDADE_LINHAS       NUMBER(16,0)    NOT NULL,
    ACQUIRER_ID             NUMBER(2,0)     NOT NULL,
    VAN_ID                  NUMBER(5,0)     NOT NULL,
    ZERADO                  NUMBER(1,0)     NOT NULL,
    TRANSMISSAO_YYYYMMDD    NUMBER(8,0)     NOT NULL,
    TRANSMISSAO_HHMMSS      NUMBER(8,0)     NOT NULL,
    CONNECT_NAME            VARCHAR2(20)    NOT NULL,
    CONNECT_NUMBER          NUMBER(20,0)    NOT NULL,
    CONNECT_USER            VARCHAR2(20)    NOT NULL,
    CONNECT_NODE            VARCHAR2(20)    NOT NULL,
    CONNECT_STATUS          VARCHAR2(20)    NOT NULL
    );

ALTER TABLE EDI_RELATORIOS_CARGA
  ADD (
    CONSTRAINT EDI_RELATORIOS_CARGA_PK PRIMARY KEY (ID)
  );

CREATE SEQUENCE EDI_RELATORIOS_CARGA_SEQUENCE;

CREATE OR REPLACE TRIGGER EDI_RELATORIOS_CARGA_ON_INSERT
  BEFORE INSERT ON EDI_RELATORIOS_CARGA
  FOR EACH ROW
BEGIN
  SELECT EDI_RELATORIOS_CARGA_SEQUENCE.NEXTVAL
  INTO :NEW.ID
  FROM DUAL;
END;
