import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import answer

delta = 0.025
x = np.arange(-1.5, 1.5, delta)
y = np.arange(-2.5, 0.5, delta)
X, Y = np.meshgrid(x, y)
Z2 = answer.f2(X,Y)

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z2,20)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('gradient descent for f2(x), step_size=0.27')

def plot2Dpoint(x,y):
	ax.hold(True)
	plt.scatter(x, y)
	
def grad3(x,y):
	gama = 0.27
	for i in range(50):
		s1=x
		s2=y
		print('s1 :',s1)
		print('s2 :',s2)
		g1=answer.grad_f2([float(x),float(y)])[0]
		g2=answer.grad_f2([float(x),float(y)])[1]
		x=x-(gama)*g1
		y=y-(gama)*g2 
		t1=-(gama)*g1
		t2=-(gama)*g2 
		print('t1 :',t1)
		print('t2 :',t2)
		ax.arrow(s1,s2,t1,t2, head_width=0.02, head_length=0.03, fc='k', ec='k')
		if(i==49):
			plot2Dpoint(x,y)

plot2Dpoint(1,-1)
grad3(1,-1)
plt.show()
