import tkinter as tk

dicVenda = {}
dicCompra = {}
dicUsuario = {}
listaVenda = []
listaCompra = []
dicEstoque = {}  
LABEL_NOME = "Nome:"

def historico_de_venda():
     return dicVenda

def historico_de_compra():
     return dicCompra

def banco_de_usuarios():
     return dicUsuario

def estoque_total():
     return dicEstoque

def cria_janela_transacao():
    
    #----------------------FUNCIONAMENTO DA JANELA TRANSAÇAO-----------------------------
    #VENDAS
    def registra_transacao_venda():
        chave_venda = produto_entrada.get()
        quantidade_venda = quantidade_entrada.get()
        preco_venda = preco_entrada.get()
        tupla_venda = (quantidade_venda, preco_venda)
        if chave_venda in dicVenda and chave_venda in dicEstoque:
            lista_venda = dicVenda[chave_venda]
            lista_venda.append(tupla_venda)
            dicVenda[chave_venda] = listaVenda#---------------------->>> ESCREVER NO ARQUIVO
        else:
            if chave_venda in dicEstoque:
                lista_venda = []
                lista_venda.append(tupla_venda)
                dicVenda[chave_venda] = listaVenda
        if chave_venda in dicEstoque:
            dicEstoque[chave_venda] += -int(tupla_venda[0])
            if dicEstoque[chave_venda] <= 0:
                dicEstoque.pop(chave_venda)
            
        else:
            dicEstoque[chave_venda] = -int(tupla_venda[0])
            if dicEstoque[chave_venda] < 0:
                dicEstoque.pop(chave_venda)
        
        print(dicEstoque)
        print(dicVenda) 
        
    #COMPRAS
    def registra_transacao_compra():
        chave_compra = produto_entrada.get()
        quantidade_compra = quantidade_entrada.get()
        preco_compra = preco_entrada.get()
        tupla_compra = (quantidade_compra, preco_compra)
        if chave_compra in dicCompra:
            lista_compra = dicCompra[chave_compra]
            lista_compra.append(tupla_compra)
            dicCompra[chave_compra] = listaCompra#---------------------->>> ESCREVER NO ARQUIVO
        else:
            lista_compra = []
            lista_compra.append(tupla_compra)
            dicCompra[chave_compra] = listaCompra
        if chave_compra in dicEstoque:
            dicEstoque[chave_compra] += int(tupla_compra[0])
            
        else:
            dicEstoque[chave_compra] = int(tupla_compra[0])
        
        print(dicCompra) 
        print(dicEstoque)

    #-----------------LAYOUT JANELA TRANSAÇAO--------------------
    janela_transacao = tk.Tk()
    janela_transacao.title("Registrar Transação")
    janela_transacao.geometry("400x200+525+270")
    
    #--------------------LAYOUT DOS BOTOES--------------------------
    produto = tk.Label(janela_transacao, text="Produto:")
    produto.place(x=20,y=20)
    
    produto_entrada = tk.Entry(janela_transacao,width="30")
    produto_entrada.place(x=105,y=20)

    produto_quantidade = tk.Label(janela_transacao, text="Quantidade:")
    produto_quantidade.place(x=20,y=50)

    quantidade_entrada = tk.Entry(janela_transacao,width="30" )
    quantidade_entrada.place(x=105,y=50)

    produto_preco = tk.Label(janela_transacao, text="Preço:")
    produto_preco.place(x=20,y=80)

    preco_entrada = tk.Entry(janela_transacao, width="30")
    preco_entrada.place(x=105,y=80)

    botao_venda = tk.Button(janela_transacao, text="Registrar Venda", width="17", command=registra_transacao_venda)
    botao_venda.place(x=20,y=110)
    
    botao_compra = tk.Button(janela_transacao, text="Registrar Compra", width="17", command=registra_transacao_compra)
    botao_compra.place(x=190 ,y=110)

    botao_cancela = tk.Button(janela_transacao, text="Cancelar", width="38", command=janela_transacao.destroy)
    botao_cancela.place(x=20,y=140)
    botao_cancela["bg"] = "red"
    
    janela_transacao.mainloop()

#------------------------------FUNÇAO JANELA GERENCIAMENTO DE USUARIO-----------------------------
def cria_janela_gerenciamento():
    #---------------------------FUNCIONAMENTO GERENCIAMENTO DE USUARIO -----------------------------
    def gerencia_usuario():
        chave_nome = entrada_nome_usuario.get()
        cpf = entrada_cpf.get()
        telefone = entrada_telefone.get()
        senha = entrada_senha.get()
        nivel = entrada_nivel.get()        
        tupla_usuario = (senha, nivel, telefone, cpf)
        if chave_nome in dicUsuario:
            dicUsuario[chave_nome] = tupla_usuario#---------------------->>> ESCREVER NO ARQUIVO
        else:
            lista_usuario = []
            lista_usuario.append(tupla_usuario)
            dicUsuario[chave_nome] = lista_usuario
        print(dicUsuario) 

    #---------------------------------FUNCIONAMENTO PESQUISA DE USUARIO----------------------------
    def pesquisa_usuario():
        pesquisa_nome = pesquisa_entrada.get()
        if pesquisa_nome in dicUsuario:
            resultado_nome["text"] = LABEL_NOME,pesquisa_nome
            resultado_cpf["text"] = "CPF:" ,dicUsuario[pesquisa_nome][0][3]
            resultado_telefone["text"] = "Telefone:" ,dicUsuario[pesquisa_nome][0][2]
            resultado_nivel["text"] = "Nível:" ,dicUsuario[pesquisa_nome][0][1]
        else:
            resultado_nome["text"] = ""
            resultado_cpf["text"] = "ERRO: Usuário não cadastrado no sistema" 
            resultado_telefone["text"] = "" 
            resultado_nivel["text"] = "" 

    #------------------------------FUNCIONAMENTO BOTAO EXCLUIR------------------------------------
    def excluir_usuario():
        exclui_nome = pesquisa_entrada.get()
        if exclui_nome in dicUsuario:
            dicUsuario.pop(exclui_nome)
            print(dicUsuario)
            resultado_nome["text"] = ""
            resultado_cpf["text"] = "" 
            resultado_telefone["text"] = "" 
            resultado_nivel["text"] = "" 
            resultado_exclusao["text"] = "USUÁRIO EXCLUÍDO COM SUCESSO!"
        else:
            resultado_nome["text"] = ""
            resultado_cpf["text"] = "" 
            resultado_telefone["text"] = "" 
            resultado_nivel["text"] = "" 
            resultado_exclusao["text"] = "IMPOSSÍVEL EXCLUIR"
            
    #--------------------------LAYOUT JANELA GERENCIAMENTO----------------------------
    
    janela_de_gerenciamento = tk.Tk()
    janela_de_gerenciamento.geometry("530x420+525+0")
    janela_de_gerenciamento.title("Gerenciamento de Usuário")

    #--------------------------BOTOES ADICIONAR USUARIO------------------------------
    nome_usuario = tk.Label(janela_de_gerenciamento, text="Nome do usuário:")
    nome_usuario.place(x=20,y=20)

    entrada_nome_usuario = tk.Entry(janela_de_gerenciamento, width="42")
    entrada_nome_usuario.place(x=150,y=20)

    cpf_usuario = tk.Label(janela_de_gerenciamento, text="CPF do usuário:")
    cpf_usuario.place(x=20,y=50)

    entrada_cpf = tk.Entry(janela_de_gerenciamento, width="42")
    entrada_cpf.place(x=150,y=50)

    telefone_usuario = tk.Label(janela_de_gerenciamento, text="Telefone do usuário:")
    telefone_usuario.place(x=20,y=80)

    entrada_telefone = tk.Entry(janela_de_gerenciamento, width="42")
    entrada_telefone.place(x=150,y=80)

    senha_usuario = tk.Label(janela_de_gerenciamento, text="Senha do usuário:")
    senha_usuario.place(x=20,y=110)

    entrada_senha = tk.Entry(janela_de_gerenciamento, width="42")
    entrada_senha.place(x=150,y=110)

    nivel_usuario = tk.Label(janela_de_gerenciamento, text="Digite o nível de acesso:\n\nNível 1:Acesso mínimo | Nível 2:Acesso intermediário | Nível 3: Acesso máximo")
    nivel_usuario.place(x=20,y=140)

    entrada_nivel = tk.Entry(janela_de_gerenciamento, width="2")
    entrada_nivel.place(x=340,y=140)

    botao_add_usuario = tk.Button(janela_de_gerenciamento, text="Atualizar usuário", command=gerencia_usuario)
    botao_add_usuario.place(x=200,y=190)

    #-----------------------------------BOTOES PESQUISAR USUARIO-----------------------------------
    nome_pesquisa = tk.Label(janela_de_gerenciamento, text=LABEL_NOME)
    nome_pesquisa.place(x=20,y=270)

    pesquisa_entrada = tk.Entry(janela_de_gerenciamento, width="40")
    pesquisa_entrada.place(x=70, y=270)

    botao_pesquisar = tk.Button(janela_de_gerenciamento, text="Pesquisar", command=pesquisa_usuario)
    botao_pesquisar.place(x=400,y=267)
    #----------------------------------RESULTADO DA PESQUISA---------------------------------------
    resultado_nome = tk.Label(janela_de_gerenciamento, text="")
    resultado_nome.place(x=170,y=300)

    resultado_cpf = tk.Label(janela_de_gerenciamento, text="")
    resultado_cpf.place(x=170,y=315)

    resultado_telefone = tk.Label(janela_de_gerenciamento, text="")
    resultado_telefone.place(x=170,y=330)

    resultado_nivel = tk.Label(janela_de_gerenciamento, text="")
    resultado_nivel.place(x=170,y=345)
    #------------------------------BOTAO PARA EXCLUIR USUARIO---------------------------------------
    botao_excluir = tk.Button(janela_de_gerenciamento, text="Excluir\nUsuário",height="3", command=excluir_usuario)
    botao_excluir["bg"] = "red"
    botao_excluir.place(x=70,y=300)
    #-----------------------------RESULTADO DA AÇAO EXCLUIR---------------------------------------
    resultado_exclusao = tk.Label(janela_de_gerenciamento, text="")
    resultado_exclusao.place(x=160,y=400)

#-----------------------------FUNÇAO CRIA JANELA PESQUISAR PRODUTO---------------------------------
def cria_janela_pesquisa_produto():
    
    #---------------------------FUNCIONAMENTO BOTOES PESQUISA PRODUTO-------------------------------
    def pesquisa_produto():
        pesquisa_produto_nome = entrada_nome_produto.get()
        if pesquisa_produto_nome in dicEstoque:
            produto_resultado_nome["text"] = LABEL_NOME,pesquisa_produto_nome
            produto_resultado_quantidade["text"] = "Qtd em estoque:",dicEstoque[pesquisa_produto_nome]
            janela_pesquisa_produto.geometry("415x140+525+270")
        else:
            produto_resultado_nome["text"] = pesquisa_produto_nome,"em falta!"
            produto_resultado_quantidade["text"] = ""

    #-------------------------------LAYOUT JANELA PESQUISA PRODUTO---------------------------------
    janela_pesquisa_produto = tk.Tk()
    janela_pesquisa_produto.geometry("415x100+525+270")
    janela_pesquisa_produto.title("Pesquisa Produto")

    #-----------------------------LAYOUT BOTOES PESQUISA PRODUTO-----------------------------------
    nome_produto = tk.Label(janela_pesquisa_produto, text="Nome do produto:")
    nome_produto.place(x=20,y=20)

    entrada_nome_produto = tk.Entry(janela_pesquisa_produto, width="30")
    entrada_nome_produto.place(x=140, y=20)

    botao_procurar = tk.Button(janela_pesquisa_produto, text="Pesquisar", command=pesquisa_produto)
    botao_procurar.place(x=160,y=50)

    produto_resultado_nome = tk.Label(janela_pesquisa_produto, text="")
    produto_resultado_nome.place(x=140,y=80)

    produto_resultado_quantidade = tk.Label(janela_pesquisa_produto, text="")
    produto_resultado_quantidade.place(x=125,y=100)
    

#------------------------------------FUNÇAO TELA ADMIN--------------------------------------
def tela_do_administrador(x):
    #--------------------LAYOUT JANELA ADMIN----------------------
    x.destroy()
    janela = tk.Tk()
    janela.geometry("470x340+525+270")
    janela.title("Controle de Estoque - LPtech (Administrador)")

    #----------------------LAYOUT DOS BOTOES--------------------------
    botao_transacao = tk.Button(janela, text="Registrar Transação", width="50", height="3", command=cria_janela_transacao)
    botao_transacao.place(x=20,y=20)

    botao_cadastro = tk.Button(janela, text="Gerenciamento de Usuário", width="50", height="3", command=cria_janela_gerenciamento)
    botao_cadastro.place(x=20,y=80)

    botao_pesquisa = tk.Button(janela, text="Pesquisar Produto", width="50", height="3", command=cria_janela_pesquisa_produto)
    botao_pesquisa.place(x=20,y=140)

    botao_historico = tk.Button(janela, text="Histórico de Transações", width="50", height="3")
    botao_historico.place(x=20,y=200)

    botao_estoque = tk.Button(janela, text="Checar Estoque", width="50", height="3")
    botao_estoque.place(x=20,y=260)

    janela.mainloop()
    
#----------------------------------FUNÇAO DE LOGIN---------------------------------
def acesso(p1,p2,p3,p4):
    
    usuario = p1.get()
    password = p2.get()
    aviso = p3
    if usuario == "admin" and password == "admin":
        tela_do_administrador(p4)
    elif usuario == "admin2" and password == "admin2":
        cria_janela_gerenciamento()
    else:
        aviso["text"] = "Usuário ou senha incorretos"
        
