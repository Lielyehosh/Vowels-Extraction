import csv
import os
import numpy as np
from os.path import join
import matplotlib.pyplot as plt
from praatio import pitch_and_intensity
from praatio import praat_scripts
from praatio import tgio
from praatio.utilities import utils

def printFormantsToCSV(filename: str):
    wavPath = os.path.abspath(join(".","data"))
    rootOutputFolder = os.path.abspath(join(".","data","praat_extraction"))
    pitchPath = join(rootOutputFolder, "pitch")
    formantsPath = join(rootOutputFolder, "formants")

    # make the directories 
    praatEXE = r"D:\voice\Praat.exe"
    utils.makeDir(rootOutputFolder)
    utils.makeDir(formantsPath)
    utils.makeDir(pitchPath)

    formantData = praat_scripts.getFormants(praatEXE,
                            join(wavPath, filename + ".wav"),
                            join(formantsPath, filename + "_formants.txt"),
                            5000,0.001,0.025)

def getFormants(filename: str):
    path = os.getcwd();
    with open(join(path,"data","praat_extraction","formants",filename)) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        formant1 = []
        time1 = []
        formant2 = []
        time2 = []
        for row in readCSV:
            if(row[0] == "time"):
                continue
            time = float(row[0])
            if (row[1] != '--undefined--'):
                formant1.append(float(row[1]))
                time1.append(float(time))
            if (row[2] != '--undefined--'):
                formant2.append(float(row[2]))
                time2.append(float(time))
        size = max(len(formant1),len(formant2))
        final = np.zeros((2,2,size))
        final[0,0,:] = formant1
        final[1,0,:] = formant2
        final[0,1,:] = time1 
        final[1,1,:] = time2
        temp = final[0,0,:]>1100
        final[0,0,temp] = None
        return final

    #----------------------------------------

    # plt.figure()
    # plt.plot(final[0,1,:],final[0,0,:],".",color="red")
    # plt.plot(final[1,1,:],final[1,0,:],".",color="blue")
    # plt.show()

    #----------------------------------------
