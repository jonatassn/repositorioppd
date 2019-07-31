import json

class Pessoa :
	def __init__(self, nome = "fulano", idade = 0) :
		self.nome = nome
		self.idade = idade

	def ehDMaior(self) :
		return self.idade >= 18

	def __str__(self) :
		return "{} {}".format(self.nome,self.idade)


class Aluno(Pessoa):
	def __init__(self,nome,idade,ra) :
		super().__init__(nome,idade)
		self.ra = ra

if __name__ == '__main__':
	'''
	pessoas = []

	for i in range(3) :
		nome = input("Digite o nome: ")
		idade = int(input("Digite a idade"))
		pessoa = Pessoa(nome,idade)
		pessoas.append(pessoa)


	for p in pessoas :
		print("{} é de maior? {}".format(p.nome,p.ehDMaior()))

		json_string = json.dumps([p.__dict__ for p in pessoas])
		arq = open("./pessoas.json","w")
		arq.write(json_string)
		arq.close()
	'''

	pessoas = []

	arq = open("pessoas.json", "r")
	string  = arq.read()
	json_string = json.loads(string)
	for s in json_string :
		pessoa = Pessoa(**s)
		pessoas.append(pessoa)

	for p in pessoas :
		print(p)
