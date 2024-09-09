def ler_chave_publica():
    arq = open("chavePublica.txt", "r")
    texto = arq.read
    e = ""
    n = ""
    var = True
    for numero in texto:
        if var == True:
            e += numero
            if numero == ";":
                var = False
        else:
            n += numero      
    e = int(e)
    n = int(n)
    return (e,n)

def ler_chave_privada():
    arq = open("chavePublica.txt", "r")
    texto = arq.read
    e = ""
    n = ""
    var = True
    for numero in texto:
        if var == True:
            e += numero
            if numero == ";":
                var = False
        else:
            n += numero      
    d = int(d)
    n = int(n)
    return (d,n)

def criptografa(dicionario):

    chaves_dic = dicionario.keys()
    
def descriptografa_para_dic(arquivo):
    num1 = ler_chave_privada()[0]
    num2 = ler_chave_privada()[1]
    elemento_final = ""
    arq = open(arquivo, "r")
    texto = arq.read()
    
    for elemento in texto:
        letra = chr((elemento**num2) % num1)
        elemento_final += letra







def escreve_no_arquivo():
 x+1   












