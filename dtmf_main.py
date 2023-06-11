from scipy.io.wavfile import read
from IPython.display import Audio
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1,44100)
samplerate, loaded_signal = read("dtmf_signal.wav")
signal = loaded_signal

fv1 = 697
fv2 = 770
fv3 = 852
fv4 = 941
fh1 = 1209
fh2 = 1336
fh3 = 1477
sin_fv1 = np.sin(2*np.pi*fv1*t)
sin_fv2 = np.sin(2*np.pi*fv2*t)
sin_fv3 = np.sin(2*np.pi*fv3*t)
sin_fv4 = np.sin(2*np.pi*fv4*t)
sin_fh1 = np.sin(2*np.pi*fh1*t)
sin_fh2 = np.sin(2*np.pi*fh2*t)
sin_fh3 = np.sin(2*np.pi*fh3*t)


dtmf_signal_1 = sin_fv1 + sin_fh1
dtmf_signal_2 = sin_fv1 + sin_fh2
dtmf_signal_3 = sin_fv1 + sin_fh3
dtmf_signal_4 = sin_fv2 + sin_fh1
dtmf_signal_5 = sin_fv2 + sin_fh2
dtmf_signal_6 = sin_fv2 + sin_fh3
dtmf_signal_7 = sin_fv3 + sin_fh1
dtmf_signal_8 = sin_fv3 + sin_fh2
dtmf_signal_9 = sin_fv3 + sin_fh3
dtmf_signal_steric = sin_fv4 + sin_fh1
dtmf_signal_0 = sin_fv4 + sin_fh2
dtmf_signal_hash = sin_fv4 + sin_fh2

dtmf_digit_signal=[dtmf_signal_1,dtmf_signal_2,dtmf_signal_3,dtmf_signal_4,dtmf_signal_5,dtmf_signal_6,dtmf_signal_7,dtmf_signal_8,dtmf_signal_9,dtmf_signal_steric,dtmf_signal_0,dtmf_signal_hash]
value = []
for digit_signal in dtmf_digit_signal:
    out = np.sum(signal*digit_signal)
    value.append(out)
max_index = value.index(max(value))
print("Signal has most similarity with digit",max_index)
if max_index == 10:
    max_index = "*"
elif max_index == 12:
    max_index = "#"