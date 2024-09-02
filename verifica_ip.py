# Docs: https://github.com/Almas-Ali/SpyIP
# pip install spyip

from spyip import trace_ip
ip = trace_ip('179.233.96.24')
print(ip.json(indent=4))