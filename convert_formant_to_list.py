import numpy as np
import time
import os
import csv
from os.path import join


def func1(string:str):
    """
    convert formants grid into a dict 
    dict contain 2 keys, for each formant
    each formant has list of a tuple arg1 = place, arg2 = value
    """
    with open(string,"r") as file:
        data = file.read()
    final = {}
    for i in range(1,3):
        final["formants [{}]".format(i)] = np.ndarray(0)

    data = data.split("bandwidths [1]:")[0]
    my_list = data.split("formants")
    for j in range(2,4):
        temp = my_list[j].split("value = ")
        for i in range(1,len(temp)):
            final["formants [{}]".format(j-1)] = np.append(final["formants [{}]".format(j-1)],float(temp[i].split("\n")[0]))
    return final

pars_formants = lambda x:x.split("formants")
pars_points = lambda x:(float(x.split("value =")[0].split("number = ")[1]),float(x.split("value =")[1].split("\n")[0]))

pars_value = lambda x:float(x.split("value =")[1].split("\n")[0])
pars_number = lambda x:float(x.split("value =")[0].split("number = ")[1])



def func2(string:str):
    """
    convert formants grid into a dict 
    dict contain 2 keys, for each formant
    each formant has list of a tuple arg1 = place, arg2 = value
    faster code using map and lambda
    """
    with open(string,"r") as file:
        data = file.read()
        data = data.split("bandwidths [1]:")[0]

    final = {}
    for i in range(1,3):
        final["formants [{}]".format(i)] = []
    my_list = data.split("formants")
    for i in range(2,4):
      final["formants [{}]".format(i-1)].extend(list(map(pars_points,my_list[i].split("points ")[1:])))
    return final

def func3(string:str):
    """
    convert formants grid into a np.ndarray
    3d
    d1 = formants
    d2 = which place
    d3 = value or place
    faster code using map and lambda 
    note: if formant 1 has more then 1100 value, automatic deleted
    
    """
    with open(string,"r") as file:
        data = file.read()
        data = data.split("bandwidths [1]:")[0]
    size = int(data.split("points: size =")[1].split("\n")[0])
    print("size is:",size)
    final = np.zeros((2,2,size))
    my_list = data.split("formants")[2:5]
    for i in range(2):
        final[i,:,:] = list(map(pars_value,my_list[i].split("points ")[1:])),list(map(pars_number,my_list[i].split("points ")[1:]))
    temp = final[0,0,:]>1100
    final[0,0,temp] = None
    return final


if __name__ == "__main__":
  start = time.time()
  data = func3("my_new_formants")
  print("this script took {}".format(time.time()-start))
