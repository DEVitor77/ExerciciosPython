agenda = {}

def consulta(agenda, pessoa):
    return agenda[pessoa]

def adciona(agenda, pessoa, telefone):
    #agenda_exemplo['marcos']=123216846
    agenda[pessoa]= telefone
    return 'adcionei'

adciona(agenda,'vitor',154569)
print(consulta(agenda,"vitor"))