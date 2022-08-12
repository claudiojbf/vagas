def confirmacao(nome,cnpj,email):
    if nome != "" and cnpj != "" and email != "":
        return True

def confima_senha(senha, senha2):
    if senha == senha2:
        return True
