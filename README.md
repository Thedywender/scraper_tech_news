👨‍💻 O que foi desenvolvido

Esse projeto teve como objetivo fazer consultas em notícias sobre tecnologia.

As notícias foram obtidas através da raspagem no blog da Trybe.

<details>
  <summary>🚵 Habilidades trabalhadas</summary>
  <ul>
    <li>Utilizei o terminal interativo do Python</li>
    <li>Escrevi meus próprios módulos e os importei em outros códigos</li>
    <li>Apliquei técnicas de raspagem de dados</li>
    <li>Extraí dados de conteúdo HTML</li>
    <li>Armazenei os dados obtidos em um banco de dados</li>
    <li>Utilizei o MongoDB nesse caso.</li>
  </ul>
</details>
<details>
  <summary>🏕️ Foi criado um Ambiente Virtual</summary>
  <p>Para criar o ambiente virtual:</p>
  <pre><code class="language-bash">python3 -m venv .venv</code></pre>
  <p>Para ativar o ambiente virtual:</p>
  <pre><code class="language-bash">source .venv/bin/activate</code></pre>
  <p>Para instalar as dependências no ambiente virtual:</p>
  <pre><code class="language-bash">python3 -m pip install -r dev-requirements.txt</code></pre>
  <p>Com o ambiente virtual ativo, as dependências serão instaladas neste ambiente. Quando precisar desativar o ambiente virtual, execute o comando <code>deactivate</code>. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.</p>
</details>
<details>
  <summary>🛠 Origem dos dados de raspagem</summary>
  <p>As notícias foram raspadas no Blog da Trybe: <a href="https://blog.betrybe.com">https://blog.betrybe.com</a>. Essas notícias foram salvas no banco de dados.</p>
</details>
<details>
  <summary>🐳 Docker/MongoDB</summary>
  <p>Foi utilizado um banco de dados chamado <code>tech_news</code>. As notícias foram armazenadas em uma coleção chamada <code>news</code>.</p>
  <p>Para rodar MongoDB via Docker:</p>
  <pre><code class="language-bash">docker-compose up -d mongodb</code></pre>
    <p>Para mais detalhes acerca do mongo com o docker, olhe o arquivo docker-compose.yml</p>
  <p>Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:</p>
  <ul>
    <li><a href="https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/">Ubuntu</a></li>
    <li><a href="https://docs.mongodb.com/guides/server/install/">MacOS</a></li>
  </ul>
  <p>Com o banco de dados rodando, o MongoDB utilizará por padrão a porta 27017.</p>
</details>
<details>
    <summary>Bônus do projeto!</summary>
    <p>Há uma interface em linha de comando (CLI) para Usar e trabalhar com os dados do banco de dados assim que estiver rodando e com as dependências instaladas.</p>
    <p>Basta rodar o comando no terminal</p>
    <pre><code class="language-bash">tech-news-analizer</code></pre>
    
</details>
