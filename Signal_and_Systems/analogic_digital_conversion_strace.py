import numpy as np
import matplotlib.pyplot as plt

#Reading seismograms (binary files):
#nt = 5001       # Number of samples
nt = 1501
#dt = 1e-3       # Time interval between samples (T_s=1/f_s)
dt = 2e-3
total_time = int(dt*nt)
f_s = 1/dt

#nx = 161
nx = 282
dx = 25

#filename = f"cmp_gather_{nt}x{nx}_{dt*1e6:.0f}us.bin"
filename = f"open_data_seg_poland_vibroseis_{dt*1e3:.0f}ms_{nt}x{nx}_shot_1.bin"

seismo = np.fromfile(filename, dtype = np.float32, count = nt*nx)
seismo = np.reshape(seismo, [nt,nx], order = "F")

trace_time = np.linspace(0,total_time,nt)
trace_seismo = seismo[:,100]


n = np.arange(nt)                      # Samples array
discrete_time = n*dt                   # Discrete time array

trace_fft = np.fft.fft(trace_seismo)
trace_fft *= 1 / np.max(np.abs(trace_fft))

f = np.fft.fftfreq(nt,dt)             # Frequencies array

Nyquist = 0.5*f_s                     # Max frequency of a spectrum

fig, ax = plt.subplots(ncols = 1, nrows = 3, figsize = (15, 9))

ax[0].plot(trace_time, trace_seismo)
ax[0].set_xlim([0, total_time])
ax[0].set_title("Seismic Trace - Real Signal", fontsize = 18)
ax[0].set_xlabel("Time [s]", fontsize = 15)
ax[0].set_ylabel(r"$x(t)$", fontsize = 15)

ax[1].plot(n,trace_seismo, "--o")
ax[1].set_xlim([0, nt-1])
ax[1].set_title("Discrete Signal", fontsize = 18)
ax[1].set_xlabel(r"Discrete time $n$", fontsize = 15)
ax[1].set_ylabel(r"$x[n]$", fontsize = 15)

ax[2].plot(np.fft.fftshift(f), np.fft.fftshift(np.abs(trace_fft)))
ax[2].set_xlim([-Nyquist,Nyquist])
ax[2].set_title("Fast Fourier Transform - FFT", fontsize = 18)
ax[2].set_xlabel("Frequency [Hz]", fontsize = 15)
ax[2].set_ylabel(r"$X(f)$", fontsize = 15)

fig.tight_layout()
plt.grid(axis = "y")
plt.show()
