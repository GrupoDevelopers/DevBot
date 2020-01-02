# 1 Uma rápida descrição sobre o "DevBot"

O seguinte projeto tem como finalidade de criar um *Bot de Gameficação* para o [Telegram](https://telegram.org/), onde terá um sistema de EXP, Ranks, Reputações dos Membros, etc.

# 2 Parte Técnica

O "[DevBot](https://github.com/GrupoDevelopers/DevBot)" está sendo programado em *Python 3.7* utilizando a biblioteca [AIOGram](https://aiogram.readthedocs.io/en/latest/) uma [API de construção de Bot do Telegram](https://core.telegram.org/bots/api). Assim como *[Pyscaffold](https://pyscaffold.org/en/latest/)*, *[mysqlclient](https://mysqlclient.readthedocs.io/)*, *Git* e *Git Flow*.

## 2.1 Instalação dos Pre-requisitos
Requisitos: 
     - Python 3.7
     - Mysql

No Linux, execute o seguinte comando para instalar os componentes necessários:

     pip3 install -r requirements.txt


## 2.2 Executando

Para a execução deste código você precisará criar um bot no Telegram, então após seguir os passos acima, a execução do Bot seguirá da seguinte forma:

     1. Crie um bot pelo @BotFather ([criando um bot em 10 passos](https://medium.com/tht-things-hackers-team/10-passos-para-se-criar-um-bot-no-telegram-3c1848e404c4));
     
     2. Encontre o *token* do bot que você acabou de criar;
     
     3. Atribua o *token* como valor na variável *API_TOKEN* do arquivo *DevBot/.env* (Se você ainda não possui o arquivo `.env`, você precisa fazer uma cópia do `.env.example` e renomear para `.env`);

     4. Crie um banco de dados e rode o Script SQL `devbot.sql` para a criação do banco de dados
     
     5. Então execute o script *DevBot/src/devbot/main.py*, `$ python3.7 src/devbot/main.py`;
     
     6. Escreva e envie, somente a palavra, devbot* pelo chat do Bot que você criou e espere o resultado.
     
*\* Não é case-sensitive, ou seja, não é sensível a maiúsculas e minúsculas.*

No atual estado do Bot, ele está somente respondendo de forma aleatória.

# 3 Funcionamento do Projeto

Aqui está uma rápida descrição para o desenvolvimento e prosseguimento do projeto nos seguintes ambientes.

## 3.1 no Trello

As criações de novas *Tarefas* vão ser feitas pelo ADM do projeto, para não causar confusões sobre o desenvolvimento e fluxo do projeto.

As *Tarefas* disponíveis estará com o status *TO DO*. Para entrar em uma tarefa já em progresso entre em contato com os já "*INGRESSADOS*" na tarefa, caso for necessária a ajuda de mais participantes.

Após escolher a tarefa de seu agrado, mude o status da tarefa para *DOING*, caso ainda estiver com status *TO DO*, e clique em *INGRESSAR*, para que outros participantes possam saber quais tarefas já estão sendo feitas e por quantas pessoas, para um melhor gerenciamento.

Logo após o término da tarefa, mude o seu status novamente agora para *DONE*, para que os participantes do projeto possam ficar atualizado do progresso do projeto.

Tente manter uma descrição concisa e coerente da sua tarefa.

## 3.2 no GitHub

Leia sobre na [Documentação](https://docs.google.com/document/d/1DVZ_7xSwBKXlbptykHyIb9Iu_6bCf0uwx3Xvv5t8Ork) do projeto.

# 4 Contribuições

Primeiramente, o projeto tem o objetivo, além do supracitado, construir novas habilidades e experiências, desconsiderando o nível que cada um já possui. Pois, muitos podem já ter mais experiências que outros, que é óbvio, mas estamos aqui para aprender.

Seria útil para todos nós o compartilhamento de conhecimento e possuir paciência com todos, por exemplo, explicações, dicas ou, simplesmente, indicações de conteúdos, para quem ainda não conseguiu compreender alguma parte do projeto ou conteúdo. Desta forma, manter um ambiente saudável e possibilitar que nós alcancemos nossos objetivos, em geral.
