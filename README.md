
👨‍💻 O que foi desenvolvido

Esse projeto teve como objetivo fazer consultas em notícias sobre tecnologia.

As notícias foram obtidas através da raspagem no blog da Trybe.

<details>
  <summary>🚵 Habilidades trabalhadas</summary>
Utilizei o terminal interativo do Python
Escrevi meus próprios módulos e os importei em outros códigos
Apliquei técnicas de raspagem de dados
Extraí dados de conteúdo HTML
Armazenei os dados obtidos em um banco de dados
Utilizei o MongoDB nesse caso.
</details>
<details>
  <summary>🏕️ Foi criado um Ambiente Virtual</summary>
Para criar o ambiente virtual:

bash
Copiar código
python3 -m venv .venv
Para ativar o ambiente virtual:

bash
Copiar código
source .venv/bin/activate
Para instalar as dependências no ambiente virtual:

bash
Copiar código
python3 -m pip install -r dev-requirements.txt
Com o ambiente virtual ativo, as dependências serão instaladas neste ambiente. Quando precisar desativar o ambiente virtual, execute o comando deactivate. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

</details>
<details>
  <summary>🛠 Origem dos dados de raspagem</summary>
As notícias foram raspadas no Blog da Trybe: https://blog.betrybe.com. Essas notícias foram salvas no banco de dados.

</details>
<details>
  <summary>🐳 Docker/MongoDB</summary>
Foi utilizado um banco de dados chamado tech_news. As notícias foram armazenadas em uma coleção chamada news.

Para rodar MongoDB via Docker:

bash
Copiar código
docker-compose up -d mongodb
Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:

Ubuntu
MacOS
Com o banco de dados rodando, o MongoDB utilizará por padrão a porta 27017.

</details>
