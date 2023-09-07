#Vamos desenvolver um robô barista!

print("Olá! Bem-vindo ao Café Necro!")

nome = input("Qual é o seu nome?\n")

if nome == "Necro" or "Zackcoding36":
  print ("Opa, é bom ver você por aqui!")
else:
 print("Olá " + nome + ", obrigado por vir aqui!\n\n\n")

menu = "Café preto, Espresso, Café com leite, Cappuccino, Chocolatto, Latte, Chá."

print(nome + ", O que você gostaria de pedir do nosso menu hoje?\nVeja aqui o que estamos servindo:\n" + menu)

pedido = input()

if pedido == "Cappuccino":
  preço = 8
elif pedido == "Espresso":
  preço = 7
elif pedido == "Latte":
  preço = 6
elif pedido == "Chocolatto":
  preço = 9
else:
 preço = 5

quantidade = input("Você gostaria de quantos?\n")

total = preço * int(quantidade)

print("Okay, o valor total do seu pedido será de: R$" + str(total))

pagamento = input("Você vai pagar com cartão,dinheiro ou vale?")

print("Ok.\nPronto " + nome + ", a gente servirá o seu pedido em alguns minutos.")

input()

print("Pode contar com a gente para o que você precisar! ;)")