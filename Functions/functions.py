import numpy as np
import pandas as pd

'''
This function receives a 1 dimensional numpy array and outputs the median absolute deviation value for said array. 

Written on Feb 24, 2021.
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

'''
This function receives a numpy array and outputs the desired metric 
for said array over a user-selected window. The size of the output varies with
the size of the arrays and the size of the window.

The input for the function should be in the order: (array, flag, window)
With:
    -Array: A 1D numpy array to calculate Mean or Standard Deviation, or a 2D numpy array to calculate Correlation.
    -Flag: A number to denote the operation desired. 1 for Mean // 2 for SD // 3 for Correlation.
    -Window: A number to denote the size of the window over which the specified metric is to be calculated.
    
Written on March 06, 2021.
'''
def slidWinDescStats(array, flag, window):
    results = np.array([]) # Creating local arrays to store our values.
    a1 = np.array([])
    a2 = np.array([])
    
    if flag == 1:    # Mean
        for i in range(len(array) - window + 1):
            results = np.append(results, round(np.mean(array[i:i+window]), 3))
        
    elif flag == 2:    # Std. Dev.
        for i in range(len(array) - window + 1):
            results = np.append(results, round(np.std(array[i:i+window]), 3))
       
    elif flag == 3:    # Correlation
        for i in range(len(array) - window + 1):
            a1 = array[i:i+window,0]
            a2 = array[i:i+window,1]
            corr = np.corrcoef(a1, a2)
            results = np.append(results, round(corr[0][1], 3))
    return results

'''
Normalized Error

This function receives two arguments/inputs, in this order:
    1) An input dataset (make it a 2D numpy array or dataframe)
    2) A flag by which power to normalize the error, for instance 1 for the mean absolute error, 
    2 for the RMSE, 3 for the cubicroot mean cubed error and so on. 
    
Produces the Normalized error, returns a single scalar.

March 28, 2021
'''
def normalizedError(array, flag):  
    n = len(array)
    tempArray = np.empty(3)
    numerator = 0
    for row in range(n):
        tempArray[0] = array[row, 0]
        tempArray[1] = array[row, 1]
        tempArray[2] = abs(tempArray[0] - tempArray[1])**flag
        numerator += tempArray[2]
    ne = (numerator/n)**(1/flag)
    return ne

'''
Category Counter

This function takes in a single variable input (1D NumPy array, list, 1-variable df, etc...)
    
Produces the count of each unique value in the input and returns a single 2D NumPy array with 
the elements in the first column and the count in the second column.

April 7, 2021
'''
def catCounter(array):  
    unique = pd.unique(array) # Gather unique values in the array.
    unique.sort() # Sort the values in ascending order (in-place)
    array = pd.DataFrame(array) # Transform array into temporary DataFrame to use Pandas functionality.
    count = np.array(array.value_counts(sort = False, ascending = True)) # Get the value counts for each element.
    output = np.empty((len(unique),2)) # Initialize output array with 2 columns and # of rows equal to # of unique elements.
    for i in range(len(unique)): # Arrange values for output.
        output[i][0] = unique[i]
        output[i][1] = count[i]
    return output

'''
Bayes' Posterior Probability Calculator

This function receives 4 arguments/inputs, in this order:
    1) Probability of A (Prior p(A))
    2) Probability of B (Prior p(B)) or, if flag == 2, p(B|~A)
    3) Probability of B given A (p(B|A), Likelihood)
    4) A flag which adopts a value of 1 for calculating the simple version of Bayes' Theorem or
        2 for the explicit version.
        
All probabilities must be between 0 and 1. The flag only takes on the values 1 and 2.

Calculates and returns the posterior probability of A|B.

April 24, 2021
'''
def bayesCalculator(priorA, priorB, likelihood, flag):  
    if flag == 1:
        numerator = likelihood * priorA
        pAB = numerator / priorB
    elif flag == 2:
        pBnotA = priorB
        numerator = likelihood * priorA
        denominator = (likelihood * priorA) + (pBnotA*(1-priorA))
        pAB = numerator / denominator
    return pAB

'''
Empirical Sample Bounds Calculator

This function receives 2 arguments/inputs, in this order:
    1) A variable that represents the dataset/distribution/sample
    2) The probability mass bounds that define the center of the distribution (e.g. 95, 99 or 50)
        
The function computes the upper bound (where the right tail starts) and the lower bound (where the left tail starts).

Returns these values as two variables.

May 01, 2021
'''
def empiricalSampleBounds(data, prob):
    if prob >= 0.01 and prob <= 99.99:
        data = np.array(data)
        data.sort()
        percentileLength = len(data)/100
        tailLength = ((100 - prob)/2) * percentileLength
        lowerBound = data[round(tailLength) - 1]
        upperBound = data[-round(tailLength)]
        return round(lowerBound,3), round(upperBound,3)
    else: return print("Probability mass bounds must be between 0.01 and 99.99.")
    
'''
Imputation by Interpolation

This function receives 1 argument/input:
    1) A one-dimensional array (by default a numpy array) of arbitrary length that represents a time series.
        
The function replaces any missing data by linear interpolation.

Returns the dataset with the interpolated values.

May 15, 2021
'''
def imputationByInterpolation(data):
    df = pd.DataFrame(data)
    result = df.interpolate(method = 'linear')
    return result


'''
Total Kolmogorov-Smirnov

This function receives 3 arguments/inputs:
    1) X1 (Sample 1)
    2) X2 (Sample2) 
    3) A flag where 1 = classical KS and 2 = total KS.
        
If the flag is set to 1, the function computes the largest distance between the two cumulative sample distributions. 
If the flag is set to 2, the function computes the total difference between the two sample distributions.

Returns the value computed.

May 18, 2021
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

# This function outputs the digitsum for input 'num'
def digitsum_func(num):
    temp = str(num) # convert it to a string
    while len(temp) > 1: # as long as it is not a single digit
        temp2 = 0 # initialize sum
        for i in range(len(temp)): # go through all digits
            temp2 = temp2 + int(temp[i]) # add the ith digit as a number to the cumulative sum
        return temp2 
    
# This function computes the M.A.D. for input 'data'
def mean_absolute_deviation_func(data):
    M = np.mean(data)
    sum = 0
    for ii in range(len(data)):
        dev = np.absolute(data[ii] - M)
        sum = sum + dev
    mad = sum/len(data)
    return mad 

# This function outputs the number of columns for input 'input_array'
def width_func(input_array): # and use it as the input to our function
    step1 = np.size(input_array) # total number of elements
    step2 = len(input_array) # total number of rows
    return int(step1/step2) # return total number of elements divided by number of rows