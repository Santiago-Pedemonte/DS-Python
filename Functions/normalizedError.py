'''
Normalized Error

This function receives two arguments/inputs, in this order:
    1) An input dataset (make it a 2D numpy array or dataframe)
    2) A flag by which power to normalize the error, for instance 1 for the mean absolute error, 
    2 for the RMSE, 3 for the cubicroot mean cubed error and so on. 
    
Produces the Normalized error, returns a single scalar.
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