# pip install customtkinter

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("500x300")

def clique():
    print("Fazer Login")
    # print(email._entry.__dict__)

texto = customtkinter.CTkLabel(window, text="Fazer Login")
email = customtkinter.CTkEntry(window, placeholder_text="Email")
senha = customtkinter.CTkEntry(window, placeholder_text="Senha", show="*")
botao = customtkinter.CTkButton(window, text="Login", command=clique)

texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)

window.mainloop()