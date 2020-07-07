import numpy as np
import time
from matplotlib import pyplot as plt
import os
import csv
from os.path import join


pars_value = lambda x:float(x.split("value =")[1].split("\n")[0])
pars_number = lambda x:float(x.split("value =")[0].split("number = ")[1])

def func1(string:str):
    """
    convert pitchtier to array
    2d
    d1 = val
    d2 = number
    """
    with open(string,"r") as file:
        data = file.read()
    size = int(data.split("points: size =")[1].split("\n")[0])
    print("size is:",size)
    final = np.zeros((2,size))
    data

    final[:,:] = list(map(pars_value,data.split("points ")[1:])),list(map(pars_number,data.split("points ")[1:]))
    return final

# by liel - get pitch list from csv file
def func2(filename):     
    path = os.getcwd();
    with open(join(path,filename)) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        values = []
        time = []
        for row in readCSV:
            if (row[0] == "time"):
                continue
            if (row[1] != '--undefined--'):
                values.append(float(row[1]))
                time.append(float(row[0]))
        size = len(values)
        final = np.zeros((2,size))
        final[0,:] = values
        final[1,:] = time
        return final


def func4(filename):  
    path = os.getcwd();
    with open(join(path,filename)) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        formant1 = []
        time1 = []
        formant2 = []
        time2 = []
        for row in readCSV:
            if (row[0] == "time"):
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

if __name__ == "__main__":
    start = time.time()
    data = func1("data\\test_mor.PitchTier")
    print("this script took {}".format(time.time()-start))
