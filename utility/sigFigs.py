from math import log10,floor

def sigFigs(number, numFigs):
    if abs(number)>1:
        return round(number, (numFigs-1)-int(log10(number)))
    else:
        return round(number, numFigs-int(log10(number)))