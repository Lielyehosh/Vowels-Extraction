from scipy.spatial import distance
import numpy as np

def closest_node(node, nodes):
    closest_index = distance.cdist([node], nodes).argmin()
    return closest_index

def closest_diff(nodes, node):
     nodes = np.asarray(nodes) 
     idx = (np.abs(nodes - node)).argmin() 
     return idx 


vowelPoints = [ ('235', '2100'), ('240', '2400'), ('250', '595'), ('300', '1390'),
            ('360', '640'), ('370', '1900'), ('390', '2300'), ('460', '1310'),
            ('500', '700'), ('585', '1710'), ('600', '1170'), ('610', '1900'),
            ('700', '760'), ('750', '940'), ('820', '1530'), ('850', '1610')]
vowelChars = ['y','i','u','ɯ','o','ø','e','ɤ','ɔ','œ','ʌ','ɛ','ɒ','ɑ','ɶ','a']


# vowels for hebrew
hebVowelPoints = [ (240, 2400), (250, 595),(360, 640), (390, 2300), (850, 1610)]
hebVowelChars = ['i','u','o','e','a']
hebVowelDiff = [2160,345,280,1910,760]


def getVowelChar(formant1,formant2):
    point = (formant1,formant2)
    index = closest_node(point,vowelPoints)
    return vowelChars[index]

def getHebVowelChar(formant1,formant2):
    point = (formant1,formant2)
    index = closest_node(point,hebVowelPoints)
    # index = closest_diff(hebVowelDiff,abs((formant1-formant2)))
    return hebVowelChars[index]
