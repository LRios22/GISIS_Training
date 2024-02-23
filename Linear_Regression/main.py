import numpy as np
import matplotlib.pyplot as plt
import functions

#Parâmetros da função linear
x = np.linspace(-2,2,101)
a0 = -2
a1 = 1

#Saída da função linear
y = functions.lfunc(a0,a1,x)

#Saída da função linear com ruído aleatório adicionado
yn = functions.rnoise(y)

#Construindo a matriz com os valores da norma L2 e achando seu ponto de mínimo
ml2n = functions.sol_space(x,y)
vmin_l2n = np.min(ml2n)
a0min_ind, a1min_ind = np.where(ml2n == vmin_l2n)
a0min_ind, a1min_ind = a0min_ind[0], a1min_ind[0]

#Gerando o gráfico
#functions.plot_lfunc(x,y)
#functions.plot_lfunc(x,yn)
plt.imshow(ml2n,extent=[-5,5,-5,5])
#plt.imshow(ml2n)
#plt.plot(a1min_ind,a0min_ind,"ro")
plt.show()
