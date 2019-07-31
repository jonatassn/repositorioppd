



if __name__ == '__main__':
	
	soma = 0
	for n in range(1,1000) :
		if( (n % 3) == 0 ) :
			soma += n
		elif( (n % 5) == 0 ) :
			soma += n

	print("soma dos multiplos de 3 ou 5 {}".format(soma))