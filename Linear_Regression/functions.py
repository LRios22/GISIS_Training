import numpy as np
import matplotlib.pyplot as plt

#Função - equação da reta
def lfunc(a0,a1,x):
    y = a0 + a1*x
    return y

#Função - aplica um ruído aleatório sobre a variável y obtida através da função linear
def rnoise(y,n_amp):
    yn = y + n_amp*(0.5 - np.random.rand(len(y)))
    return yn

#Função - calcula a norma L2
def l2norm(dobs,dprev):
    l2n = np.sqrt(np.sum((dobs - dprev)**2))
    return l2n

#Função - determina o espaço de soluções, os dados previstos e a norma L2
def sspace_cmp(n,vr,zr,xs,dobs):
    ml2n = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            dprev = np.sqrt((xs + 4*zr[i]**2)/vr[j]**2)
            ml2n[i,j] = l2norm(dobs,dprev)

    return ml2n

#Função - determina os parâmetros que minimizam a norma L2
def lsquares(xs,npar,dobs):
    G = np.zeros((len(xs),npar))

    for i in range(len(xs)):
        for j in range(npar):
            if j == 0:
                G[i,j] = 1
            else:
                G[i,j] = xs[i]

    GT = G.transpose()
    M1 = np.matmul(GT,G)
    M2 = np.matmul(GT,dobs)
    M1inv = np.linalg.inv(M1)

    pest = np.matmul(M1inv,M2)
    vest = np.sqrt(1/pest[1])
    zest = (vest/2)*np.sqrt(pest[0])
    print('Os parâmetros estimados são: v= {}'.format(vest) + ' m/s e z= {}'.format(zest) + ' m')

    return vest,zest








