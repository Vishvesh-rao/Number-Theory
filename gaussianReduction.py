#!/usr/bin/env python2

from numpy import linalg as la
import numpy as np
from math import *

# def norm(vector):
# 	size = 0
# 	for i in range(len(vector)):
# 		size += vector[i]*vector[i]
# 	return sqrt(size)

# def dotProduct(v1,v2):
# 	prdt = 0
# 	vectorLen = min(len(v1),len(v2))
# 	for i in range(vectorLen):
# 		prdt += v1[i]*v2[i]
# 	return prdt

def gaussianReduction(v,u):
	while(1):
		if la.norm(u) < la.norm(v):
			v,u = u,v
		m = floor(np.dot(v,u)/np.dot(v,v))
		
		if m == 0:
			return v,u

		u = [u[0] - m*v[0], u[1] - m*v[1]]
		#u = u - m*v		

if __name__ == '__main__':
	
	v = [846835985, 9834798552]
	u = [87502093, 123094980]

	v,u = gaussianReduction(v,u)
	print(v,u)
	print(np.dot(v,u))