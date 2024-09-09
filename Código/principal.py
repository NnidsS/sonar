import tkinter as tk
from criptoarquivo import historico_de_venda, historico_de_compra, banco_de_usuarios, estoque_total
from interface import acesso

Venda = historico_de_venda()
Compra = historico_de_compra()
Usuarios = banco_de_usuarios()
Estoque = estoque_total()

#---------------------------------FUNÇÃO JANELA DE TRANSAÇÕES-----------------------------------

#---------------------------LAYOUT JANELA DE LOGIN--------------------------------
window = tk.Tk()
window.title("Controle de Estoque - LPtech")
window.geometry("350x200+525+270")

titulo = tk.Label(text="Usuário:")
titulo.place(x=50, y=50)

entrada1 = tk.Entry()
entrada1.place(x=105, y=50)

senha = tk.Label(text="Senha:")
senha.place(x=50, y=75)

entrada2 = tk.Entry()
entrada2.place(x=105, y=75)

aviso = tk.Label(text="")
aviso.place(x=0, y=0)

botao1 = tk.Button(text="Entrar", command=lambda: acesso(entrada1, entrada2, aviso, window))
botao1.place(x=150, y=105)

window.mainloop()

