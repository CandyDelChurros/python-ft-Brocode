nome = "Cayo Henrique Mercadante"

primeiro_nome = nome[0:4]
ultimo_nome = nome[14:24]
funky_nome = nome[::2]
nome_invertido = nome [::-1]

print("Seu ultimo nome is " +primeiro_nome)
print("Seu ultimo nome is " +ultimo_nome)
print(funky_nome)
print("Seu nome de trás para frente fica: " +nome_invertido)

website = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)
print(website)
print(website2)
print(website[slice])
print(website2[slice])


