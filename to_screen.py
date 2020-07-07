from scipy.io.wavfile import read
import scipy.signal as signal
import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.io.wavfile import write
from scipy.ndimage import median_filter
import statistics
import matplotlib.pyplot as plt
import convert_formant_to_list as forman
import fromCSV as from_csv
import convert_pitch_to_list as pitch
import Interval
import VowelIdentifier


# read audio samples
audio_name = "O"
input_data = read("data\\"+ audio_name + ".wav")
from_csv.printFormantsToCSV(audio_name)
audio = input_data[1]
fs = input_data[0]
time  = np.ndarray((len(audio)))
for i in range(len(audio)):
    time[i] = i/fs
# time & value
# pitch_data = pitch.func1("data\\A.PitchTier")
# forman_data = forman.func3("data\\A.FormantGrid")
forman_data = from_csv.getFormants(audio_name + "_formants.txt")
interval = [0,len(audio)/fs]


# data_audio = np.vstack((audio, time))

# forman_data [ # formants , val = 0 /sec = 1 ,  ]
# forman_data[0,1,:]

formant1 = Interval.full_list(forman_data[0,:,:])
formant2 = Interval.full_list(forman_data[1,:,:])

##################################
new_list = []
for i in range(len(formant1)):
    for j in range(len(formant2)):
        in1 = Interval.Interval(formant1[i][1][0],formant1[i][1][-1])
        temp = in1.intersects(Interval.Interval(formant2[j][1][0],formant2[j][1][-1]))
        if(temp != None):
            new_list.append(temp)

##################################
plt.subplot(211)
plt.title("sound wave")
plt.plot(time,audio)
plt.xlim(xmin=interval[0],xmax = interval[1])


plt.subplot(212)
plt.title("formants")
# plt.plot(pitch_data[1,:],pitch_data[0,:],".",color="black")
# plt.plot(splited1[1],splited1[0],color="b")
plt.plot(forman_data[1,1,:],forman_data[1,0,:],".",color="pink")
plt.plot(forman_data[0,1,:],forman_data[0,0,:],".",color="red")
flag = 0
for val in formant1:
    if(flag):
        plt.plot(val[1],val[0],color = "g",linewidth=2)
        flag =0
    else:
        plt.plot(val[1],val[0],color = "b",linewidth=2)
        flag = 1
for val in formant2:
    if(flag):
        plt.plot(val[1],val[0],color = "g",linewidth=2)
        flag =0
    else:
        plt.plot(val[1],val[0],color = "b",linewidth=2)
        flag = 1



plt.xlim(xmin=interval[0],xmax = interval[1])
flag = 0
for l in new_list:
    if(flag):
        plt.axvspan(l.start,l.end,color="turquoise")
        flag = 0
    else:
        plt.axvspan(l.start, l.end, color="green")
        flag = 1

vowels_l = []
for inter in new_list:
    temp1 = statistics.median(inter.split(forman_data[0,:,:])[0])
    temp2 = statistics.median(inter.split(forman_data[1,:,:])[0])
    ch = VowelIdentifier.getHebVowelChar(temp1,temp2)
    vowels_l.append(ch)

print(vowels_l)

plt.show()

