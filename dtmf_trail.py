#coverting wave in Audio
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0,1,44100)
fv1 = 941
fh1 = 1477
v1 = np.sin(2*((np.pi*fv1*t)))
v2 = np.sin(2*((np.pi*fh1*t)))
signal = v1+v2
#lets display first 500 samples of signal
plt.figure(7)
plt.plot(t[:500],signal[:500],color="orange",label="v1+v2")
plt.legend()
plt.grid()
plt.xlabel("Time(sec)")
plt.ylabel("Amplitude(Hz)")
from IPython.display import Audio
Audio(signal,rate = 44100)  #convert signal into audio


#Check for 1 and 2
#dtmf signal for digit 1 and 2
t = np.linspace(0,1,44100)
fv1 = 697
fh1 = 1209
fh2 = 1336
sin_fv1 = np.sin(2*np.pi*fv1*t)
sin_fh1 = np.sin(2*np.pi*fh1*t)
sin_fh2 = np.sin(2*np.pi*fh2*t)

dtmf_signal_1 = sin_fv1+sin_fh1
dtmf_signal_2 = sin_fv1+sin_fh2

dtmf_digit_signal=[dtmf_signal_1,dtmf_signal_2]
value =[]

for a in dtmf_digit_signal:
    out = np.sum(signal*a)
    value.append(out)
print(value)
print("MAX value=",max(value))
max_index = value.index(max(value))
print("The digit with most resemblance is",max_index)