from math import log10,floor

def sigFigs(number, numFigs):
    return round(number, (numFigs-1)-int(log10(number)))