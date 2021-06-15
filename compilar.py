# python compilar.py build
# python compilar.py bdist_msi
import glob
import os
from cx_Freeze import setup, Executable

for icone in glob.glob(f'{os.path.dirname(__file__)}/*.ico'):
    break

program_name = icone.split('\\')[-1][:-4]

with open(f'{icone[:-4]}.py', 'r') as arquivo:
    conteudo = arquivo.readlines()

for versao in conteudo:
    if '__version__' in versao:
        version = versao.split(' ')[-1].replace("'","")
        break

keywords = 'SCRIPTS DE APOIO'
long_description = 'DIVERSOS SCRIPTS DE APOIO PYTHON'

executables = [Executable(f"{program_name}.py",
                          base=None, icon=f"{program_name}.ico")]
#files = ['instantclient_19_10', f'{program_name}.json']
files = [f'{program_name}.json']
options = {
    'build_exe': {
        "include_files": files,
    },
}
f'{program_name}.ico'
setup(
    name=f'{program_name}',
    options=options,
    version=version,
    author='Daniel Alves Dias Junior',
    description=f'{program_name}',
    author_email='juninhoboni@gmail.com',
    license='GNU GENERAL PUBLIC LICENSE',
    long_description=long_description,
    keywords=keywords,
    platforms='Windows, Python',
    requires='Windows',
    executables=executables
)
