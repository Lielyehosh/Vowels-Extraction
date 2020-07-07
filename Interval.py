import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.ndimage import median_filter
import statistics
class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end




    def split(self,array):
        """
        :param ndarray, shape (2,n), first val, second place:
        :return: array start to end
        """
        if(str(type(array)) != "<type 'numpy.ndarray'>"):
            assert("array is not a numpy.ndarray")
        assert len(str(np.shape(array)).split((","))) == 2 and\
            int(str(np.shape(array)).split("(")[1].split(",")[0]) == 2 \
            , "wrong shape of ndarray"


        s = np.searchsorted(array[1,:],self.start)
        e = np.searchsorted(array[1,:],self.end)
        return array[:,s:e]

    def intersects(self,in1):
        """
        :param in1:
        :return: intersects interval if bigger the 0.6 precent
        """
        precent = 0.6
        t =self.is_contain(in1)
        if(t != None):
            return t

        max_start = max(self.start,in1.start)
        min_end = min(self.end,in1.end)
        if(max_start>min_end):
            return None
        pos_diff = min_end-max_start
        neg_diff = (max_start - min(self.start,in1.start)) + max(self.end,in1.end)-min_end
        def_precent = pos_diff/(neg_diff+pos_diff)
        if(def_precent> precent or pos_diff > 0.035):
            return Interval(max_start,min_end)
        else:
            return None

    def is_contain(self,in1):
        if(self.start >=in1.start and self.end <= in1.end):
            return Interval(self.start,self.end)
        if(in1.start >= self.start and in1.end <=self.end):
            return Interval(in1.start,in1.end)
        return None

def div_array_5(array):
    if(str(type(array)) != "<type 'numpy.ndarray'>"):
        assert("array is not a numpy.ndarray")
    assert len(str(np.shape(array)).split((","))) == 2 and\
        int(str(np.shape(array)).split("(")[1].split(",")[0]) == 2 \
        , "wrong shape of ndarray"
    dev = array.copy()
    # dev[0,:] = gaussian_filter1d(dev[0,:],3)
    dev[0,:] = median_filter(dev[0,:],3)
    for i in range(2,len(dev[0])-3):
        dev[0,i] = dev[0,i+1]-dev[0,i-1]
    return dev

def formants_to_interval():
    pass

def div_array(array):
    if(str(type(array)) != "<type 'numpy.ndarray'>"):
        assert("array is not a numpy.ndarray")
    assert len(str(np.shape(array)).split((","))) == 2 and\
        int(str(np.shape(array)).split("(")[1].split(",")[0]) == 2 \
        , "wrong shape of ndarray"
    dev = array.copy()
    # dev[0,:] = gaussian_filter1d(dev[0,:],3)
    # dev[0,:] = median_filter(dev[0,:],3)
    for i in range(len(dev[0])-1):
        dev[0,i] = dev[0,i+1]-dev[0,i]
        dev[0,len(array[0])-1] = dev[0,len(array[0])-2]
    return dev


def var_over_div(array_div):
    if(str(type(array_div)) != "<type 'numpy.ndarray'>"):
        assert("array is not a numpy.ndarray")
    assert len(str(np.shape(array_div)).split((","))) == 2 and\
        int(str(np.shape(array_div)).split("(")[1].split(",")[0]) == 2 \
        , "wrong shape of ndarray"

    var = array_div.copy()
    # var[0,:] = median_filter(var[0,:],5)

    for i in range(2,len(var[0])-2):
        var[0,i] = statistics.variance(array_div[0,i-2:i+2])

    return var


def find_max_interval(array,index):
    if(str(type(array)) != "<type 'numpy.ndarray'>"):
        assert("array is not a numpy.ndarray")
    assert len(str(np.shape(array)).split((","))) == 2 and\
        int(str(np.shape(array)).split("(")[1].split(",")[0]) == 2 \
        , "wrong shape of ndarray"
    if(index< len(array[0])-2):
        v1 = Interval(array[1][index],array[1][index+2])
        index = index+1
        var = v1.split(array)

        while(statistics.variance(var[0]) <1500):
            try:
                index = index+1
                var = np.concatenate((var,array[:,index:index+2]), axis=1)
            except:
                return var,index
        return var,index
    return None,index



def full_list(array):
    if(str(type(array)) != "<type 'numpy.ndarray'>"):
        assert("array is not a numpy.ndarray")
    assert len(str(np.shape(array)).split((","))) == 2 and\
        int(str(np.shape(array)).split("(")[1].split(",")[0]) == 2 \
        , "wrong shape of ndarray"
    l = []
    i = 0
    index = 0
    while i<len(array[0]):
        if i<index:
            i = index+1
        in1,index = find_max_interval(array,i)
        if(index>int(len(array[0])*0.99)):
            break
        else:
            l.append(in1)
            i+=1
    new_l = []
    for val in l:
        if(val[1][-1]-val[1][0] >0.03):
            new_l.append(val)
    return new_l

