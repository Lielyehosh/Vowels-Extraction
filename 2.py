from scipy.io.wavfile import read
import scipy.signal as signal
from scipy.ndimage import gaussian_filter1d
from scipy.ndimage import median_filter
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt
import convert_formant_to_list
import statistics
# np.random.seed(280490)
# data = convert_formant_to_list.func3("test.FormantGrid")
# x = data[0,0,:]

# y3 = gaussian_filter1d(x, 3)
# y6 = gaussian_filter1d(x, 6)
# plt.subplot(211)
# plt.title("source")
# plt.plot(x,linestyle = " ", color = "r" ,label='original data',marker='.')


# plt.legend()
# plt.grid()
# plt.show()
data = np.zeros(10)
dev = np.zeros(10)

data[1] = 5
data[2] = 10
data[3] = 51
data[4] = 11
data[5] = 13
data[6] = 12
data[7] = 15
data[8] = 2
data[9] = 21

for i in range(1,len(data)-1):
    dev[i] = data[i+1] - data[i-1]

print(dev)
# try:
#     print(statistics.variance(data[data!=None],))
# except:
#     print("couldnt")
