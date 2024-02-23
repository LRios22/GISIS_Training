import numpy as np
import matplotlib.pyplot as plt

#Função - retorna y(x), onde a relação entre x e y é linear
def lfunc(a0,a1,x):
    y = a0 + a1*x
    return y

#Função - aplica um ruído aleatório sobre a variável y
def rnoise(y):
    yn = y + np.random.rand(len(y))
    return yn

#Função - visualização da reta
def plot_lfunc(x,y):
    fig,ax = plt.subplots()
    ax.plot(x,y)
    plt.show()

#Função - cria espaço de soluções com os valores de a0 e a1
#Função - correlação através da norma L2
def sol_space(x,y):
    n = 1001
    a0 = np.linspace(-5,5,n)
    a1 = np.linspace(-5,5,n)

    a0,a1 = np.meshgrid(a0,a1)

    ml2n = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            yss = a0[i,j] + a1[i,j]*x
            ml2n[i,j] = np.sqrt(np.sum((y - yss)**2))

    return ml2n



#Função - plota o espaço de soluções