import numpy as np
import matplotlib.pyplot as plt
import functions

#Dados e parâmetros relacionados à função t^2=t0^2+x^2/v^2
x = np.linspace(50,8000,319)
xs = x**2
v = 3000 #Velocidade real (m/s)
z = 500 #Profundidade real (m)
n_amp = 0.1 #Amplitude do ruído
p0 = (4*z**2)/v**2 # Igual a t0^2
p1 = 1/v**2
npar = 2 #Número de parâmetros (p0,p1)

#Tratando a função como linear e simulando dados reais (dobs=tobs=t+ruído)
ts = functions.lfunc(p0,p1,xs)
t = np.sqrt(ts)
tobs = functions.rnoise(t,n_amp)

#Plotando os gráficos de t e tobs
plt.plot(x,t,'-r',label='t')
plt.plot(x,tobs,'-b',label='tobs')
plt.xlabel("x (m)")
plt.ylabel("t (s)")
plt.legend()
plt.ylim(2.9,0.1)
plt.show()

#Construindo o espaço de soluções e a norma L2
n = 101
vr = np.linspace(v/2,3*v/2,n)
zr = np.linspace(z/2,3*z/2,n)

ml2n = functions.sspace_cmp(n,vr,zr,xs,tobs)

#Estimando os parâmetros
vest,zest = functions.lsquares(xs,npar,tobs**2)

#Plotando os resultados (ponto de mínimo da norma L2 e valores estimados para os parâmetros)
ypos_min,xpos_min = np.where(ml2n == np.min(ml2n))
ypos_min,xpos_min = ypos_min[0],xpos_min[0]
vr_min = vr[xpos_min]
zr_min = zr[ypos_min]
print('O ponto de mínimo da norma L2 está localizado em v= {}'.format(vr_min) + ' m/s e z= {}'.format(
        zr_min) + ' m')

plt.imshow(ml2n,aspect='auto',extent=[v/2,3*v/2,z/2,3*z/2])
plt.xlabel("Velocidade (m/s)")
plt.ylabel("Profundidade (m)")
plt.plot(vr_min,zr_min,'ro',label='Ponto de mínimo da norma L2')
plt.plot(vest,zest,'bo',label='Valores estimados')
plt.legend(loc='upper right')
plt.show()

#Plotando os gráficos para dobs e dprev
tprev = np.sqrt((xs + 4*zest**2)/vest**2)
vest = round(vest,2)
zest = round(zest,2)

plt.plot(x,tprev,'-r',label='dprev para v= {}'.format(vest) + ' m/s e z= {}'.format(zest) + ' m')
plt.plot(x,tobs,'-b',label='dobs para v= {}'.format(v) + ' m/s e z= {}'.format(z) + ' m')
plt.xlabel("x (m)")
plt.ylabel("t (s)")
plt.legend(loc='upper right')
plt.ylim(2.9,0.1)
plt.show()
