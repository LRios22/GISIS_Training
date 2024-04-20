import numpy as np
import matplotlib.pyplot as plt

#Building continuous and sampled signals
sine_amplitudes = [3, 10, -1]
sine_frequencies = [5, 15, 30]      # [hz]

total_time = 1      # [s]
#n_s = 100                # Number of samples (in total_time)
#T_s = total_time/ns      # Time between samples [s] = dt
#f_s = 1/Ts               # Sampling frequency [hz] (In fact, f_s depends on the device that measures the signal)
f_s = 100           # [hz]

analogic_time = np.linspace(0, total_time, int(1e6)) 
analogic_sine = np.zeros_like(analogic_time)

for k, freq in enumerate(sine_frequencies):
    w_0 = 2*np.pi*freq
    analogic_sine += sine_amplitudes[k]*np.sin(w_0*analogic_time)

''' 
    Analytical representation of a digital signal

    w_s = 2 pi f_0 / f_s

    f_0 -> analogic signal frequency
    f_s -> sampling frequency
    w_s -> discrete signal angular frequency
'''

dt = 1 / f_s                           # Time spacing
nt = int(total_time / dt)              # Total samples

n = np.arange(nt)                      # samples array
discrete_time = n*dt                   # discrete time array

discrete_sine = np.zeros(nt)

for k, freq in enumerate(sine_frequencies):
    w_s = 2*np.pi*freq/f_s
    discrete_sine += sine_amplitudes[k]*np.sin(w_s * n)  

discrete_sine_fft = np.fft.fft(discrete_sine)
discrete_sine_fft *= np.max(sine_amplitudes) / np.max(np.abs(discrete_sine_fft))

f = np.fft.fftfreq(nt, dt)             # frequencies array

Nyquist = 0.5*f_s                      # Max frequnecy of a spectrum

fig, ax = plt.subplots(ncols = 1, nrows = 3, figsize = (15, 9))

ax[0].plot(analogic_time, analogic_sine)
ax[0].stem(discrete_time, discrete_sine, markerfmt = "k", linefmt = "k--", basefmt = "k")
ax[0].set_xlim([0, total_time])
ax[0].set_title("Analogic - Digital Conversion", fontsize = 18)
ax[0].set_xlabel("Time [s]", fontsize = 15)
ax[0].set_ylabel(r"$x(t)$", fontsize = 15)

ax[1].plot(n, discrete_sine, "--o")
ax[1].set_xlim([0, nt-1])
ax[1].set_title("Discrete Signal", fontsize = 18)
ax[1].set_xlabel(r"Discrete time $n$", fontsize = 15)
ax[1].set_ylabel(r"$x[n]$", fontsize = 15)

ax[2].stem(f, np.abs(discrete_sine_fft))
ax[2].set_xlim([1-Nyquist,Nyquist-1])
ax[2].set_title("Fast Fourier Transform - FFT", fontsize = 18)
ax[2].set_xlabel("Frequency [Hz]", fontsize = 15)
ax[2].set_ylabel(r"$X(f)$", fontsize = 15)

fig.tight_layout()
plt.grid(axis = "y")
plt.show()
