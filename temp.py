from scipy.io.wavfile import read
import scipy.signal as signal
from scipy.ndimage import gaussian_filter1d
from scipy.ndimage import median_filter
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt
import convert_formant_to_list
import statistics 
import convert_pitch_to_list

data = convert_pitch_to_list.func1("test_mor.PitchTier")
f1 = data[0,0,:]
f2 = data[1,0,:]

fy1 = gaussian_filter1d(f1, 3)
fy2 = gaussian_filter1d(f2, 3)
lenn = int(len(fy2)//10)-1
array = np.ndarray(lenn)
for i in range(lenn):
    array[i] = statistics.variance(fy2[i*10:i*10+20])

dev = np.zeros((len(fy2)))
for i in range(1,len(data)-1):
    dev[i] = fy2[i+1] - fy2[i-1]

plt.subplot(211)
plt.title("source")
#plt.plot(data[0,1,:],f1,".", label='original data f1',linestyle = " ",color = "r")
# plt.plot(fy1, '.', label='filtered data f1',linestyle = " ",color = "b")
# plt.plot(data[0,1,:],f2, '.', label='original data f2',linestyle = " ",color = "r")
plt.plot(data[0,1,:],fy2, '.', label='filtered data f2',linestyle = " ",color = "b")
plt.subplot(212)
plt.title("variance")
plt.plot(array,"k")




plt.legend()
plt.grid()
plt.show()