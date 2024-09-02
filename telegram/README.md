# Criando um BOT com Telegram no Python

> No Telegram porcurar por @botfather

Botfather é o chefe dos bots do Telegram!

> Comece uma conversa com o BotFather clicando no botão Iniciar (ou Start, na versão em inglês).

    What can this bot do?
    
    BotFather is the one bot to rule them all. Use it to create new bot accounts and manage your existing bots.

    About Telegram bots:
    https://core.telegram.org/bots
    Bot API manual:
    https://core.telegram.org/bots/api

    Contact @BotSupport if you have questions about the Bot API.

> Digite /newbot e siga as instruções para configurar um novo bot. O BotFather dará a você um token que você usará para autenticar seu bot e conceder a ele acesso à API do Telegram.

    Alright, a new bot. How are we going to call it? Please choose a name for your bot.

> Digite o nome do canal

    Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.

> Digite o username para o bot

    exemplo_bot

    Done! Congratulations on your new bot. You will find it at t.me/exemplo_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

    Use this token to access the HTTP API:
    2346985476958:hgsfdliughsldghsdghusiudfhglisuhg
    Keep your token secure and store it safely, it can be used by anyone to control your bot.

    For a description of the Bot API, see this page: https://core.telegram.org/bots/api

> Salvar o TOKEN em uma variável de ambiente

    export BOT_TOKEN=2346985476958:hgsfdliughsldghsdghusiudfhglisuhg

> Para conferir as variáveis de ambiente

    env


> Consultar as credenciais

Crie um arquivo consulta_id.py

    import os
    import requests
    TOKEN = os.environ.get('BOT_TOKEN')
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    print(requests.get(url).json())

No retorno terá o ID que será usado para o envio da mensagem.
Salvar o ID em outra variável de ambiente

    export BOT_ID=1543546235

> Enviando mensagem

Crie um arquivo enviando_mensagem.py

    import os
    import requests
    TOKEN = os.environ.get('BOT_TOKEN')
    chat_id = os.environ.get('BOT_ID')
    message = "hello from your telegram bot"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # this sends the message

> As mensgens serão enviadas para o link com o nome do bot criado.

    t.me/exemplo_bot