# meusLivrosLidos
Projeto feito utilizando Python + Django, utilizando Class-Based-Views como base. A princípio este projeto nasce com intuito de produzir um software simples no qual usuário poderá cadastrar os livros que ele leu. A ideia é que as evoluções do software sejam feitas por mim durante meus estudos ou por qualquer um que deseja viver uma experiência com django, sendo que tenho interesse em auxiliar outros programadores em suas codificações, aprender com programadores mais experientes que eu em python e com isso promover disceminação de conhecimento.

Obs.: Para montar ambiente é necessário ter o docker e docker-compose instalados. Vide links úteis:
* Docker - https://docs.docker.com/install/linux/docker-ce/ubuntu/
* docker-compose - https://docs.docker.com/compose/


Projeto hospedado no heroku: https://meuslivroslidos.herokuapp.com/.

Para montar ambiente basta:

<h3>Baixar o repositório utilizando o comando:</h3>

* git clone https://github.com/andreiflavio/meusLivrosLidos.git

<h3>Executar os comandos abaixo:</h3>

* cd meusLivrosLidos/

* docker-compose up -d

Para executar o projeto:

* docker-compose run web bash

* ip addr (este comando permite verificar qual é o ip do container onde a aplicação django está sendo executada. Tal informação será útil para acessar sistema nos próximos passos)

* python manage.py runserver 0.0.0.0:8000 (O ip 0.0.0.0 serve para indicar que qualquer chamada feita contra a porta 8000 do container deverá dar acesso ao django)

Feito isso basta acessar sistema utilizando o ip indicado via ip addr:porta desejada

Obs.: Ao baixar repositório está havendo um problema com arquivos estáticos que havia sido solucionado e voltou a acontecer. Assim que encontrar uma solução atualizo documentação.

Obs.2: Sou novo no universo docker então creio que as explicações dos comandos careçam de melhorias que vou providenciá-las logo.

