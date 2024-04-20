import numpy as np
import matplotlib.pyplot as plt

#Continuous function
domain = int(1e6)
t = np.linspace(-np.pi, np.pi, domain)

#Numerical series f(t) : R -> R
frequencies = np.array([5, 10])  # hz
nt = 50 # Number of terms in the series (for the examples)
signal = np.zeros(domain)

for f in frequencies:
    signal += np.sin(2*np.pi*f*t)

#Plot
xloc = np.linspace(-np.pi, np.pi, 9)
xlab = [r"$-\pi$", r"$\dfrac{-3\pi}{4}$", r"$\dfrac{-\pi}{2}$", r"$\dfrac{-\pi}{4}$",
        r"$0$", r"$\dfrac{\pi}{4}$", r"$\dfrac{\pi}{2}$", r"$\dfrac{3\pi}{4}$", r"$\pi$"]

fig, ax = plt.subplots(num = "Simple signal", figsize = (15,5))
ax.plot(t, signal)
ax.set_xticks(xloc)
ax.set_xticklabels(xlab)
ax.set_xlim([-np.pi, np.pi])
ax.set_xlabel("t [s]", fontsize = 15)
ax.set_ylabel("Amplitude", fontsize = 15)
ax.set_title('Sum of functions $\sin(2\pi f_i t)$ for $f_0$ = {}'.format(frequencies[0]) + ' hz and $f_1$ = {}'.format(frequencies[1]) + ' hz')

fig.tight_layout()
plt.show()

#Plot - first example
#title = "First example"

#a = 2 * np.sinh(np.pi)/np.pi
#signal = a/2 + np.zeros(domain)

#for n in range(1,nt):
#    c = a * (-1)**n / (1 + n**2)
#    signal += c*np.cos(n*t) + n*c*np.sin(n*t)

#Plot - second example
#title = "Second example"

#signal = np.zeros(domain)

#for n in range(1,nt):
#    signal += -2*np.sin(n*t)/n * ((-1)**n + np.sin(n*np.pi)/(n*np.pi))

#Plot - third example
title = "Third example"

a = 2*(np.pi)**2/3
signal = a + np.zeros(domain)

for n in range(1,nt):
    signal += 4*(-1)**(n+1)/n**2 * np.cos(n*t)

fig, ax = plt.subplots(num = title, figsize = (15,5))

#ax.plot(t, signal, label = "Fourier series")
#ax.plot(t, np.exp(-t), "--", label = "Real function")
#ax.set_title('$f(t)=exp(-t)$; number of terms in the series: $n$ = {}'.format(nt))

#ax.plot(t, signal, label = "Fourier series")
#ax.plot(t, t, "--", label = "Real function")
#ax.set_title('$f(t)=t$; number of terms in the series: $n$ = {}'.format(nt))

ax.plot(t, signal, label = "Fourier series")
ax.plot(t, np.pi**2 - t**2, "--", label = "Real function")
ax.set_title('$f(t)=\pi^2 - t^2$; number of terms in the series: $n$ = {}'.format(nt))

ax.set_xticks(xloc)
ax.set_xticklabels(xlab)
ax.set_xlim([-np.pi, np.pi])
ax.set_xlabel("t [s]", fontsize = 15)
ax.set_ylabel("Amplitude", fontsize = 15)
ax.legend(loc = "upper left", fontsize = 15)
ax.grid(True)

fig.tight_layout()
plt.show()
