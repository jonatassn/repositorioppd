#import math
#from math import sqrt,cos,sin
from math import sqrt as raiz
import sys

if __name__ == '__main__':
	inicio = int(sys.argv[1])
	fim = int(sys.argv[2])
	for i in range(inicio,fim) :
		print("raiz de {} é {:.2f}".format(i,raiz(i)))