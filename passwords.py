import os
import base64
import getpass
import gnupg
import sys

pathname = os.path.dirname(sys.argv[0])
filePathTxt = os.path.abspath(pathname)+"/passwords.txt"
filePathEncrypted = os.path.abspath(pathname)+"/passwords.txt.gpg"

def main():
    print("Menu:")
    print("0:Sair 1:Adicionar Senha 2:Ver Senhas")
    x = input()
    if x == "0":
        print("Digite seu email da chave gpg ou o nome da chave: ")
        chave = input()
        encrypt(chave)
    elif x == "1":
        print("Digite a quantidade de caracteres que a senha deve ter: ")
        n = input()
        print("Digite um titulo para sua senha: ")
        titulo = input()
        salvar(gerar_senha(int(n)), titulo)
        main()
    elif x == "2":
        try:
            f = open(filePathTxt, 'r')
            text = f.readlines()
            if text != []:
                for t in text:
                    print(t)
            else:
                print("Nenhuma senha")
            main()
        except FileNotFoundError:
            f = open(filePathTxt, 'w')
            print("Nenhuma senha")
            main()



def gerar_senha(n):
    qt_bits = n * 6
    qt_bytes, resto = divmod(qt_bits, 8)
    if resto:
        qt_bytes += 1
    octetos = os.urandom(qt_bytes)
    return base64.b64encode(octetos)[:n].decode('ascii')

def salvar(senha, titulo):
    f = open(filePathTxt, 'r')
    text = f.readlines()
    text.append(titulo + ": " + senha + "\n")
    f = open(filePathTxt, 'w')
    f.writelines(text)
    f.close()

def encrypt(chave):
    gpgPath = os.path.expanduser("~/.gnupg")
    gpg = gnupg.GPG(gnupghome=gpgPath)
    with open(filePathTxt, 'rb') as f:
        status = gpg.encrypt_file(
            f, recipients=[chave],
            output='passwords.txt.gpg')
    os.remove(filePathTxt)

def decrypt(chave):
    gpgPath = os.path.expanduser("~/.gnupg")
    gpg = gnupg.GPG(gnupghome=gpgPath)
    with open(filePathEncrypted, 'rb') as f:
        status = gpg.decrypt_file(f, passphrase=chave, output=filePathTxt)

def iniciar():
    if os.path.isfile(filePathEncrypted):
        print("Digite sua senha de decriptação: ")
        pw = getpass.getpass()
        decrypt(str(pw))
    elif not os.path.isfile(filePathTxt):
        os.mknod(filePathTxt)

iniciar()
main()