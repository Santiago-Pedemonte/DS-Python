import numpy as np
'''
This function receives a 1 dimensional numpy array and 
outputs the median absolute deviation value for said array. 

'''
def medAbsDev(array):
    writtenBy = 'Santiago Pedemonte'
    meds = []
    med = np.median(array)
    for element in array:
        meds.append(abs(element - med))
    meds_arr = np.array(meds)
    medabsdev = np.median(meds_arr)
    return medabsdev