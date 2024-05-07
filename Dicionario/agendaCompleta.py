agenda_completa = {
    'vitor':{
        'email': 'vitor@gmail.com',
        'telefones':[1158647596,1145783146],
        'idade':25
         },    
    'livia':{
        'email': 'livia@gmail.com',
        'telefones':[1147257596,114652146],
        'idade':14
        },
    'Edilane':{
        'email': 'Edilane@gmail.com',
        'telefones':[1158647724,1145743946],
        'idade':41
        }
    }

def criarPessoa(agenda, pessoa, telefone, email):
    #criando um dicionario para armazenar os dados da pessoa
    dados_pessoa = {}
    dados_pessoa["telefones"] = [telefone]
    dados_pessoa["email"] = email

    #adciona os dados da pessoa á agenda
    agenda[pessoa]= dados_pessoa

    return "Usuario adicionado."

criarPessoa(agenda_completa,'Danilo',11975483749,'danilo@gmail.com')

print(agenda_completa)