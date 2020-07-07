import os
from os.path import join
from praatio import pitch_and_intensity
from praatio import praat_scripts
from praatio import tgio
from praatio.utilities import utils

def printFormantsToCSV(args):
        

    wavPath = os.path.abspath(join(".","data"))
    # tgPath = os.path.abspath(join(".", "files"))
    rootOutputFolder = os.path.abspath(join(".","data","praat_extraction"))
    pitchPath = join(rootOutputFolder, "pitch")
    formantsPath = join(rootOutputFolder, "formants")


    # make the directories 
    praatEXE = r"D:\voice\Praat.exe"
    utils.makeDir(rootOutputFolder)
    utils.makeDir(formantsPath)


    def printFormantToCSVFile(filename:str):    
        formantData = praat_scripts.getFormants(praatEXE,
                                join(wavPath, filename),
                                join(formantsPath, filename + "_formants.txt"),
                                5500,0.001,0.050)
