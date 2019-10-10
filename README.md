# 1 Uma rápida descrição sobre o "DevBot"

O seguinte projeto tem como finalidade de criar um *Bot de Gameficação* para o [Telegram](https://telegram.org/), onde terá um sistema de EXP, Ranks, Reputações dos Membros, etc.

# 2 Parte Técnica

O "[DevBot](https://github.com/GrupoDevelopers/DevBot)" está sendo programado em *Python 3.7* utilizando a biblioteca [AIOGram](https://aiogram.readthedocs.io/en/latest/) uma [API de construção de Bot do Telegram](https://core.telegram.org/bots/api). Assim como *[Pyscaffold](https://pyscaffold.org/en/latest/)*, *Git* e *Git Flow*.

## 2.1 Instalação dos Pre-requisitos

No Linux, execute o seguinte comando para instalar os componentes necessários:

     pip3 install -r requirements.txt

<!---Processos para a instalação dos pacotes, caso algum erro aconteçar durante as instalações pelo requirements.txt:

     apt install python3.7

     sudo apt install python3-pip

     python3.7 -m pip install pip

     pip3.7 install idna==2.8

     pip3.7 install yarl==1.3.0

     pip3.7 install aiohttp==3.6.1

     pip3.7 install aiogram==2.3
-->

## 2.2 Executando

A seguir as devidas instalações dos componentes básicos, e baixado o *[projeto](https://github.com/GrupoDevelopers/DevBot)* pelo *GitHub*, a execução do Bot seguirá da seguinte forma:

     1- Crie um bot pelo @BotFather;
     
     2- Encontre o *token* do bot que você acabou de criar;
     
     3- Atribua o *token* como valor na variável *API_TOKEN* do arquivo *DevBot/.env*;
     
     4- Execute o script *DevBot/src/devbot/main.py*;
     
     5- Escreva e envie, somente a palavra, devbot* pelo chat do Bot que você criou e espere o resultado.
     
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
