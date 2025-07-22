
#Pra separar os dados
espa = f'''__________________________________________'''

#dados de strings
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

#dados de numeros int e float
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em Kg: "))

#fazer o nome completo
nome_completo = nome + ' ' + sobrenome

#nome completo , idade e peso
print(f'Seu nome completo e \t {nome_completo}')

print(f'Sua idade e de {idade} Anos')

print(f'E seu peso de {peso}Kg')

#separar os itens
print(espa)

#ver se tem 18 anos ou mais , entre 14 a 18 anos , e menos q 14
if idade >= 18:
    print('Voce ja pode trabalhar de carteira assinada e tirar carteira de motorista')
    print('E tambem pode ser preso ne kkk')

elif idade <= 18 and idade >= 14:
    print('Com essas idade vc ja pode ser menor aprendiz e responder por menor infrator ')
    print('Epoca da puberdade e muitooo hormonio')
else:
    print('Tu ainda e apenas um criança mesmo nao sendo inocente ')

#Fim do progama
print(espa,'\n', 'Esse foi o teste de idade e alguns de seus direitos','\n',espa)


