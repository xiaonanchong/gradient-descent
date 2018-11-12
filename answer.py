# -*- coding: utf-8 -*-

"""
Use this file for your answers. 

This file should been in the root of the repository 
(do not move it or change the file name) 

"""

# NB this is tested on python 2.7. Watch out for integer division
from __future__ import division
#import numpy as np
import autograd.numpy as np
from autograd import grad

   
def grad_f1(x):
    return np.array([8*x[0]-2*x[1]-1, 8*x[1]-2*x[0]-1])
    """
    4 marks

    :param x: input array with shape (2, )
    :return: the gradient of f1, with shape (2, )
    """
    pass

def grad_f2(x):
    a = x[0]
    b = x[1]
    p1 = np.cos(a**2 - 2*a + b**2 +1)*(2*a-2)+6*a-2*b-2
    p2 = np.cos(a**2 - 2*a + b**2 +1)*(2*b)+6*b-2*a+6
    return np.array([p1, p2])
    """
    6 marks

    :param x: input array with shape (2, )
    :return: the gradient of f2, with shape (2, )
    """
    pass

def f2(x, y):
    return np.sin(x**2 + y**2 -2*x +1) + 3*x**2 + 3*y**2 - 2*x*y - 2*x + 6*y +3

def f3(x):
    a = x[0]
    b = x[1]
    p1 = -(a**2 - 2*a + b**2 +1)
    #print(np.exp(p1))
    p2 = -(3*a**2 + 3*b**2 - 2*a*b - 2*a + 6*b +3)
    #print(np.exp(p2))
    p3 = (1/10)*np.log((a**2+1/100)*(b**2+1/100)-(a*b)**2)
    #print(p3)
    p= np.exp(p1) + np.exp(p2)- p3
    return 1-p

def grad_f3(x):
    g_f3 = grad(f3)
    return g_f3(x)    
    """
    This question is optional. The test will still run (so you can see if you are correct by
    looking at the testResults.txt file), but the marks are for grad_f1 and grad_f2 only.

    Do not delete this function.

    :param x: input array with shape (2, )
    :return: the gradient of f3, with shape (2, )
    """
    pass

print(f2(1,-1))
#print(grad_f3([1.0,-1.0]))


