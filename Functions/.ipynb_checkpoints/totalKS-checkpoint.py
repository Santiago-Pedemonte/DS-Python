'''
Total Kolmogorov-Smirnov

This function receives 3 arguments/inputs:
    1) X1 (Sample 1)
    2) X2 (Sample2) 
    3) A flag where 1 = classical KS and 2 = total KS.
        
If the flag is set to 1, the function computes the largest distance between the two cumulative sample distributions. 
If the flag is set to 2, the function computes the total difference between the two sample distributions.

Returns the value computed.
'''
def totalKS(x1, x2, flag):
    D = []
    y1 = 0
    y2 = 0
    probPerValue = 100 / len(x1)
    sample = []
    raw_value = []


    for i in range(len(x1)):
        sample.append(1)
        raw_value.append(x1[i])
    for i in range(len(x2)):
        sample.append(2)
        raw_value.append(x2[i])


    tempArray = np.empty((len(sample), 2))


    for i in range(len(x1) + len(x2)):
        tempArray[i][0] = sample[i]
        tempArray[i][1] = raw_value[i]


    sortedArray = tempArray[np.argsort(tempArray[:, 1])]
    y_array = np.empty((len(sortedArray), 2))


    for i in range(len(sortedArray)):
        if sortedArray[i][0] == 1:
            y1 += probPerValue
            y_array[i][0] = y1
            y_array[i][1] = y2
        elif sortedArray[i][0] == 2:
            y2 += probPerValue
            y_array[i][0] = y1
            y_array[i][1] = y2


    for i in range(len(sortedArray)):
        D.append(abs(y_array[i][0] - y_array[i][1]))


    if flag == 1:
        return max(D)
    elif flag == 2:
        return np.array(D).mean()