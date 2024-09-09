def ler_chave_publica():
    arq = open("chavePublica.txt", "r")
    texto = arq.read()
    e = ""
    n = ""
    var = True
    for numero in texto:
        if var:
            e += numero
            if numero == ";":
                var = False
        else:
            n += numero      
    e = int(e)
    n = int(n)
    return (e, n)

def ler_chave_privada():
    arq = open("chavePublica.txt", "r")
    texto = arq.read()
    d = ""
    n = ""
    var = True
    for numero in texto:
        if var:
            d += numero
            if numero == ";":
                var = False
        else:
            n += numero      
    d = int(d)
    n = int(n)
    return (d, n)

def criptografa(dicionario):
    pass  # Função ainda não implementada

def descriptografa_para_dic(arquivo):
    num1 = ler_chave_privada()[0]
    num2 = ler_chave_privada()[1]
    arq = open(arquivo, "r")
    texto = arq.read()
    
    for elemento in texto:
        chr((elemento**num2) % num1)
        # Processamento adicional pode ser necessário

def escreve_no_arquivo():
    pass  











