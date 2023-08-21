#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def is_anagram(palavra1, palavra2):

    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()

    if len(palavra1) != len(palavra2):
        return False
    
    contar_palavra1 = {}
    contar_palavra2 = {}
    
    for i in palavra1:
        contar_palavra1[i] = contar_palavra1.get(i, 0) + 1
    
    for i in palavra2:
        contar_palavra2[i] = contar_palavra2.get(i, 0) + 1
    
    return contar_palavra1 == contar_palavra2






# Teste a sua função aqui (caso ache necessário)











