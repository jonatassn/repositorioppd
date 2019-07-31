import json

class Pizza :
	def __init__(self,sabor,preco) :
		self.sabor = sabor
		self.preco = preco

class Cardapio :
	def __init__(self) :
		self.pizzas = []

	def getPizzas(self) :
		try:
			arq = open("pizzas.json", "r")
			string = arq.read()
			json_string = json.loads(string)

			for p in json_string :
				pizza = Pizza(**p)
				self.pizzas.append(pizza)

			arq.close()
		except Exception as e:
			pass

		
		return self.pizzas


	def addPizza(self, pizza) :
		pizzas = self.getPizzas()

		pizzas.append(pizza)
		json_string = json.dumps([p.__dict__ for p in pizzas])
		arq = open("pizzas.json", "w")
		arq.write(json_string)
		arq.close()

def cls():
	for i in range(100) :  
		print("\n")

def menu() :
	opt = -1
	cardapio = Cardapio()
	cls()
	while opt != 0 :
		

		print("0 - Sair")
		print("1 - Cadastrar Pizzas")
		print("2 - Visualizar Cardapio")
		print("3 - Realizar Pedido")
		opt = int(input("Digite a opção desejada: "))

		if opt == 0 :
			exit()
		elif opt == 1 :
			sabor = input("Digite o sabor da pizza: ")
			preco = float(input("Digite o preço da pizza de {}".format(sabor)))
			pizza = Pizza(sabor,preco)

			cardapio.addPizza(pizza)
			opt = -1
		elif opt == 2 :
			cls()
			for i,p in enumerate(cardapio.getPizzas()) :
				print("{} - Sabor: {} Preço: {}".format(i,p.sabor,p.preco))


if __name__ == '__main__':
	menu()