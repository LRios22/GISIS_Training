import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

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

#FFT for all traces
trace_fft = np.fft.fft(seismo,axis=0)
trace_fft *= 1 / np.max(np.abs(trace_fft))
#print(trace_fft.shape)

f = np.fft.fftfreq(nt,dt)             # Frequencies array
#print(f)
#print(np.sort(f))

Nyquist = 0.5*f_s                     # Max frequency of a spectrum

#c_trace_fft = trace_fft[:,100]      # Taking one trace
#plt.plot(np.abs(c_trace_fft))

r_trace_fft = trace_fft[:,111:172]       # Taking a range of columns/traces
print(r_trace_fft.shape)

#plt.imshow(seismo,aspect='auto',cmap='gray',vmin=-0.5,vmax=2)
#plt.xlabel("x = Offset (m)")
#plt.ylabel("t = TWT (s)")
#plt.xticks(ticks=[0,40,80,120,160],labels=[0,1000,2000,3000,4000])     # cmp
#plt.yticks(ticks=[0,1000,2000,3000,4000,5000],labels=[0,1,2,3,4,5])    # cmp
#plt.xticks(ticks=[0,47,94,141,188,235,282],labels=[-3525,-2350,-1175,0,1175,2350,3525])    # vibroseis
#plt.yticks(ticks=[0,250,500,750,1000,1250,1500],labels=[0,0.5,1.0,1.5,2.0,2.5,3.0])        # vibroseis

#plt.imshow(np.abs(trace_fft),aspect='auto')
plt.imshow(np.abs(r_trace_fft),aspect='auto')
plt.xlabel("x = Offset (m)")
plt.ylabel("Frequency (Hz)")
plt.colorbar()
#plt.xticks(ticks=[0,40,80,120,160],labels=[0,1000,2000,3000,4000]) # cmp
#plt.yticks(ticks=[0,1000,2000,3000,4000,5000],labels=[0,1,2,3,4,5])    # cmp
#plt.xticks(ticks=[0,47,94,141,188,235,282],labels=[-3525,-2350,-1175,0,1175,2350,3525])
plt.xticks(ticks=[0,15,30,45,60],labels=[-750,-325,0,325,750])
plt.yticks(ticks=[0,300,600,900,1200,1500],labels=[0,100,200,-200,-100,0])
#plt.yticks(ticks=[150,450,750,1050,1350],labels=[-200,-100,0,100,200])
plt.title('FFT - All Traces')

plt.show()
