# pip install locate

import locale
from datetime import datetime

# Configurar o locale para Português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

data = datetime.now().strftime("%d de %B de %Y")

print("Rio de Janeiro, data.)

## Em alguns sistemas o locate não está instalado

Verifique os locales disponíveis:

No terminal, execute o comando:

```bash
locale -a
```

Isso exibirá uma lista de todos os locales instalados no seu sistema. Procure por pt_BR.utf8 ou pt_BR.UTF-8 na lista. Se estiver presente, o locale está disponível.

Verifique se o locale está configurado:

Para verificar a configuração do locale, você pode usar o comando:

```bash
locale
```

Isso mostrará o locale atual usado para várias categorias. Verifique se LC_TIME está configurado como pt_BR.UTF-8 ou similar.

Instale o locale se necessário:

Se o locale não estiver disponível, você pode instalá-lo. Em sistemas baseados em Debian (como Ubuntu), você pode usar:

```bash
sudo locale-gen pt_BR.UTF-8
sudo update-locale
```