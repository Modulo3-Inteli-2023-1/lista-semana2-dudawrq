#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def conta_palavras_unicas(frase):
    frase = frase.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace('-', '')
    palavras = frase.split()
    palavras_unicas = set()
    for palavra in palavras:
        palavras_unicas.add(palavra)
    
    return len(palavras_unicas)






# Teste a sua função aqui (caso ache necessário)











