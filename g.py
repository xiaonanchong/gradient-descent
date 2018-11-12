from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import answer

def f2(x, y):
    return np.sin(x**2 + y**2 -2*x +1) + 3*x**2 + 3*y**2 - 2*x*y - 2*x + 6*y +3
'''
def f3(x ,y):
    a = x
    b = y
    p= np.exp(-(a**2 - 2*a + b**2 +1)) + np.exp(-(3*a**2 + 3*b**2 - 2*a*b - 2*a + 6*b +3))+ (1/10)*np.log((a**2+1/100)*(b**2+1/100)-(a*b)**2)
    return 1-p
'''
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)

X, Y = np.meshgrid(x, y)
Z2 = f2(X, Y)
Z3 = answer.f3([X,Y])

fig = plt.figure()
ax = plt.axes(projection='3d')
### set fn here
ax.contour3D(X, Y, Z3, 100, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('gradient descent for f3(x)');

'''
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface');
'''

def plot_point3(x,y,c):
	p = np.array([x,y,answer.f3([x,y])])
	ax = plt.gca()
	ax.hold(True)
	ax.scatter(p[0], p[1], p[2], color=c)
	
def plot_point2(x,y,c):
	p = np.array([x,y,f2(x,y)])
	ax = plt.gca()
	ax.hold(True)
	ax.scatter(p[0], p[1], p[2], color=c)

def gradient_descent(s,t,fn):
	for i in range(50):
		if(fn==2):
			g1=answer.grad_f2([s,t])[0]
			g2=answer.grad_f2([s,t])[1]
		if (fn==3):
			g1=answer.grad_f3([float(s),float(t)])[0]
			g2=answer.grad_f3([float(s),float(t)])[1]
		s=s-(0.05)*g1
		t=t-(0.05)*g2
		if(fn==2):
			print('2')
			if(i==49):
				plot_point2(s,t,'blue')
			if(g1 > 0.01 or g2 > 0.01):
				plot_point2(s,t,'black')
			else: 
				plot_point2(s,t,'green')
				print('minimum point reached!')
		if(fn==3):
			print('3')
			if(i==49):
				plot_point3(s,t,'blue')
			if(g1 >0.001 or g2 >0.001):
				plot_point3(s,t,'black')
			else: 
				plot_point3(s,t,'green')
				print('minimum point reached!')			

### set fn here
plot_point3(1.0,-1.0,'red')
gradient_descent(1, -1, 3)
plot_point3(1.0,-1.0,'red')

ax.view_init(60, 35)
plt.show()


