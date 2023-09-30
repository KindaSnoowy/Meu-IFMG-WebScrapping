# WebScrapping de notas do site Meu IFMG 📓

# Resumo
Projeto feito em Python usando Requests e BeautifulSoup para extração de notas do site MeuIFMG. 
Também conta com uma API do Discord para comandos e notificação de alteração das notas.

# Como funciona?
**Comandos**

  O módulo [discordapi.py](https://github.com/KindaSnoowy/Meu-IFMG-WebScrapping/blob/main/discord/discordapi.py) ouve o canal especificado para possíveis comandos, caso encontre, busca as notas no site MeuIFMG utilizando o usuário e senha fornecidos no script, extrai as notas e envia elas formatadas.

**Notificador**

  Periodicamente, o script analisa o site das notas e salva elas em um arquivo .json, caso as novas notas sejam diferentes das antigas, notifica no canal exatamente o que mudou.

# Setup
1) Baixe as bibliotecas utilizadas:
   
   `pip install beautifulsoup4`
   
   `pip install requests`

2) Em [config.py](https://github.com/KindaSnoowy/Meu-IFMG-WebScrapping/blob/main/config.py), atualize as varíaveis username e password para seu usuário e senha no MeuIFMG:

   ```
   config.py
   
   ##Usuário e senha para acesso ao site meu.ifmg
   username = "" <--
   password = "" <--
   ```

3) [Crie um bot](https://discord.com/developers/docs/getting-started#step-1-creating-an-app) e troque a varíavel Token em [config.py](https://github.com/KindaSnoowy/Meu-IFMG-WebScrapping/blob/main/config.py) para o Token do seu bot.

   ```
   config.py
   
   ##Discord
   token = "" ## Token do bot <--
   url = "https://discord.com/api/v9/channels/<channel id>/messages" ## Canal das mensagens enviadas
   ```

4) [Convide seu bot para um servidor](https://discord.com/developers/docs/getting-started#adding-scopes-and-bot-permissions)
   
5) Com o bot no servidor, extraia o ID do Canal desejado para os comandos e notificações clicando com o botão direito e em `Copiar ID do canal`
   
   ![image](https://github.com/KindaSnoowy/Meu-IFMG-WebScrapping/assets/118382917/b9f893a9-7ca0-41fa-9e88-fff45cb69e56)

6) Atualize a varíavel url em [config.py](https://github.com/KindaSnoowy/Meu-IFMG-WebScrapping/blob/main/config.py) colocando o ID do canal selecionado no lugar de <channel id>

   ```
   config.py
   
   ##Discord                                      Aqui
   token = ""                                   ↓↓↓↓↓↓↓↓
   url = "https://discord.com/api/v9/channels/<channel id>/messages" ## Canal das mensagens enviadas
   ```

7) Rode [main.py](https://github.com/KindaSnoowy/Meu-IFMG-WebScrapping/blob/main/main.py) :D!

# Avisos
O código provavelmente não seja o mais estável possível, então é provável que ele possa quebrar com muitos requests ou algo do tipo, contudo, não aconteceu em nenhum dos meus testes. (O código também não tem tratamento de erros próprios, eventualmente planejo fazer algo que funcione como um)

Esse código só vai funcionar se você usar uma conta do Segundo Ano cursando Informática, pois somente as disciplinas de tal curso estão disponíveis no config.py, é possível customizar e o código aceitaria normalmente se customizar os dicionários, planejo trazer suporte pra outros cursos no futuro.

Pro código rodar 24/7 você ou vai ter que deixar o código rodando no seu computador ou hostear ele em algum lugar, sites como [PythonAnywhere](www.pythonanywhere.com) não funcionam pois o firewall do discord bloqueia os requests que vem do IP dessas hosts. O único site que eu testei e funciona gratuitamente é o [Replit](www.replit.com) que fornece [suporte de até 24 horas](https://stackoverflow.com/a/64601788) até ele parar e ter que ser novamente ligado manualmente.

Eu pretendo manter atualizando esse repositório pra tornar ele mais estável e ser utilizado de forma mais simples e sem precisar de tanto esforço.
