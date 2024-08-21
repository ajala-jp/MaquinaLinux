class Pessoa:
	def __init__(self, nome, idade, telefone):
		self.nome = nome
		self.idade = idade
		self.telefone = telefone

	def getName(self):
		print(f"O seu nome é:{self.nome}")

	def getIdade(self):
		print(f"A sua idade é:{self.idade}")

	def getTelefone(self):
		print(f"Número de telefone:{self.telefone}")



pessoa1 = Pessoa("João",19,123456789)

pessoa1.getName()

pessoa1.getIdade()

pessoa1.getTelefone()
