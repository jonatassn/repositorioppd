#if __name__ == '__main__' :

idade = int(input("Digite sua idade: "))
print(idade)

if idade < 18 and idade < 1 :
	print("D menor e bebe")
elif idade < 18 :
	print("D menor")
elif idade >= 60 :
	print("D maior e idoso")
else :
	print("D Maior")