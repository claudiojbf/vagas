# vagas
-------------------------------------------------------------------------------
Requisitos

Para conseguir executar este projeto você presisara ter instaldo em seu computador o pytho3 a versão utilizada foi:

Python 3.10.5

E tambem sera nescessario esta intaldo o postgresql a versão utilizada foi:

Postgres 14.5


Venv

Este projeto ja esta inclusa a venv com todas as bibliotecas nescessarias para a execução do arquivo basta com o arquivo aberto iniciar a venv se o seu sistema operaracional
for Windows basta digitar no terminal o comando:

cmd.exe

<venv>\Scripts\activate.bat

PowerShell

<venv>\Scripts\Activate.ps1

Se o seu SO for Linux:

bash/zsh

$ source <venv>/bin/activate

fish

$ source <venv>/bin/activate.fish

csh/tcsh

$ source <venv>/bin/activate.csh

PowerShell Core

$ <venv>/bin/Activate.ps1


Com o venv iniciado todas as bibliotecas nescessarias para rodar o codigo estarao presentes apos isso você tera que configurar o banco de dados onde neste projeto eu
estou utilizando o postgresql no seu servidor crie um banco de dados com as seguintes informações:

Nome : projeto_vagas

User : postgres

Senha : 172596

obs: se você quiser trocar alguma configuração do banco para o acesso va na pasta p_vagas_todo, acesse o arquivo settings.py e apartir da linha 81 você podera encontrar as 
configurações do banco.

Com o banco configurado você tera no seu terminal executar o comando:

python manage.py migrate

Este comando serve para você conseguir trasferir todas as informações para o seu banco de dados habilitando as tabelas dele.

Com tudo concluido você ira executar o comando:

python manage.py runserver

Com este comando executado você podera acessar a aplicação funcionando onde você tera a tela principal que contera as vagas cadastradas e na parte de cima no canto superior direito
tera uma parte onde você podera acessar o menu que tera disponivel as opções para cadastrar e fazer o login.

Cadastro:
Na parte de cadastro você encontra duas opções o cadastro de empresa e o de candidato onde a empresa podera realizar o cadastro de novas vagas e acompanhar as inscrições, 
já o candidato podera se increver na vaga desejada.
