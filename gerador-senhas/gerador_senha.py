import string as s
from secrets import SystemRandom as Sr

def gerar_senha():
    senha=(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))
    print("Minha senha é:", senha)