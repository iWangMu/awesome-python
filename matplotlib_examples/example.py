import numpy as np
import matplotlib.pyplot as plt


theta = np.linspace( 0 , 2 * np.pi , 100 )
 
# radius = 0.4
figure, axes = plt.subplots( 1 )

for radius in np.arange(0.0, 3.01, 0.1):
    a = radius * np.cos( theta )
    b = radius * np.sin( theta )
    
    axes.plot( a, b ,linewidth=10)

axes.set_aspect(1)
 
plt.title( 'Parametric Equation Circle' )
plt.show()


