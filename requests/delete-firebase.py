# python3 -m venv ./venv && source venv/bin/activate
# pip3 install requests

import requests

requisicao = requests.delete("https://requests-f7f13-default-rtdb.firebaseio.com/-N9J1Covb09NMAQWK1Ix/.json")

print(requisicao)
print(requisicao.json())
