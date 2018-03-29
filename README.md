# meusLivrosLidos
Projeto feito utilizando Python + Django, utilizando Class-Based-Views como base. A princípio este projeto nasce com intuito de produzir um software simples no qual usuário poderá cadastrar os livros que ele leu. A ideia é que as evoluções do software sejam feitas por mim durante meus estudos ou por qualquer um que deseja viver uma experiência com django, sendo que tenho interesse em auxiliar outros programadores em suas codificações, aprender com programadores mais experientes que eu em python e com isso promover disceminação de conhecimento.

Obs.: para habilitar debug, criar dentro do diretório meusLivrosLidos arquivo com o nome ".env" e inserir o seguinte conteúdo nele:

DEBUG=True

Se utilizar base postgresql localmente configurar as seguintes variáveis no arquivo ".env":
DB_NAME = Nome do banco de dados
DB_USER = usuário OWNER do banco
DB_PASSWORD = senha do usuário
DB_HOST = ip do host. Geralmente 'localhost' resolve
DB_PORT = porta onde está rodando postgresql. Geralmente é a porta '5432'

Se preferir usar sqllite3, basta descomentar a configuração para este banco no settings.py


Projeto hospedado no heroku: https://meuslivroslidos.herokuapp.com/ (ainda é necessário resolver hospedagem dos arquivos estáticos.)

Quem quiser fazer um frontend utilizando qualquer tecnologia, vide documentação da api:
