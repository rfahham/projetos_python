# pip install time
# pip install tqdm
# pip install urllib3
# pip install requests

import time
from tqdm import tqdm
import requests
import urllib3

count = 0
for i in tqdm(range(600)):
    urllib3.disable_warnings()
    r = requests.get('https://www.globo.com', verify=False)
    if r.status_code != 200:
        break
    time.sleep(0.001)
    count += 1
print("total de requests:", count)