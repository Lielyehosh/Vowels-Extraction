
plt.subplot(211)
plt.title("sound wave")
plt.plot(time,audio)
plt.xlim(xmin=interval[0],xmax = interval[1])


plt.subplot(212)
plt.title("formants")
plt.plot(pitch_data[1,:],pitch_data[0,:],".",color="black")
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


# plt.plot(splited2[1],splited2[0],color="g")
plt.xlim(xmin=interval[0],xmax = interval[1])



plt.show()
