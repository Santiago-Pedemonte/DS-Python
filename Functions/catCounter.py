'''
Category Counter

This function takes in a single variable input (1D NumPy array, list, 1-variable df, etc...)
    
Produces the count of each unique value in the input and returns a single 2D NumPy array with 
the elements in the first column and the count in the second column.

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