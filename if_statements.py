idade = int(input("Qual sua idade?: "))

if idade == 100:
    print("Você se tornou um monge, atingiu o centenario")
elif idade >= 18:
    print("Você é maior de idade")
elif idade < 0:
    print("Você nem nasceu ainda")
else:
    print("você é menor de idade")