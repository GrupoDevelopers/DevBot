# DevBot
Este é um projeto criado no [Grupo Developers](https://t.me/devs_brasil) que tem como intuito trazer conhecimento para o grupo e melhorar suas habilidades como desenvolvedores.
O DevBot tem como premissa ser um bot de gamificação para ser usado em grupos do Telegram, ou seja, ajudará a tornar os grupos mais dinâmicos e ativos, criando ranking, sistema de XP, reputação de membros e etc.

<br>

### 1. Especificações
O DevBot está sendo programado em *Python 3.7* utilizando a biblioteca [AIOGram](https://aiogram.readthedocs.io/en/latest/), uma biblioteca que facilita a utilização da [API de bots do Telegram](https://core.telegram.org/bots/api). Também utilizamos outras bibliotecas/tecnologias como *[Pyscaffold](https://pyscaffold.org/en/latest/)* e *[mysqlclient](https://mysqlclient.readthedocs.io/)*.

<br>

### 2. Instalação
Primeiro deve ser instalado o [Python 3.7](https://www.python.org/downloads/), [PIP](https://pip.pypa.io/en/stable/installing/) (gerenciador de bibliotecas do Python) e o [MySQL](https://www.mysql.com/) respectivo ao seu sistema operacional, após isso será necessário algumas instalações antes de instalar a biblioteca do mysqlclient conforme o [manual de instalação no README do projeto](https://github.com/PyMySQL/mysqlclient-python). Então agora você poderá executar o comando que instalará as bibliotecas Python utilizadas no projeto:

     $ pip3 install -r requirements.txt

ou

     $ python3.7 -m pip install -r requirements.txt

<br>

### 3. Executando
Para a execução deste código você precisará criar um bot no Telegram para fazer os testes, então após seguir os passos acima, a execução do Bot seguirá da seguinte forma:

1. A criação de bots do Telegram é feita através do @BotFather ([criando um bot em 10 passos](https://medium.com/tht-things-hackers-team/10-passos-para-se-criar-um-bot-no-telegram-3c1848e404c4));

2. Atribua o **token** do seu bot (dado pelo @BotFather) como valor na variável **API_TOKEN** do arquivo `DevBot/.env`. *(se você ainda não possui o arquivo `.env`, você precisa fazer uma cópia do `.env.example` e renomear esta cópia para `.env`)*;

3. Crie um banco de dados e importe o script SQL `devbot.sql` para a criação da estrutura do banco

4. Então execute o script principal: `$ python3.7 src/main.py`;

5. Abra seu bot de testes e mande pra ele a palavra **devbot**, se ele respondeu... Pronto! Está tudo funcionando!

<br>

### 4. Como colaborar com o DevBot?
Este projeto é totalmente dependente do [Grupo Developers](https://t.me/devs_brasil), não é possível colaborar com este projeto sem ao menos participar do grupo privado de discussão sobre o bot, de lá surgem todas as discussões necessárias e decisões tomadas sobre o desenvolvimento do bot. Para ter acesso ao grupo de discussões você precisa primeiramente acessar o [Grupo Developers](https://t.me/devs_brasil) para poder solicitar ser incluído no grupo de discussões. Então após a solicitação aos admins, eles lhe encaminharão toda a documentação e explicação o processo e regras para o desenvolvimento do bot.

As criações de novas implementações e correções do DevBot são feitas no Trello, através da criação de tarefas, estas tarefas são oriundas de sugestões dos membros do [Grupo Developers](https://t.me/devs_brasil)ou das idéias que surgem no grupo de discussão.