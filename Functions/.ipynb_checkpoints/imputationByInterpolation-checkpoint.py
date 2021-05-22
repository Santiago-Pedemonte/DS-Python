'''
Imputation by Interpolation

This function receives 1 argument/input:
    1) A one-dimensional array (by default a numpy array) of arbitrary length that represents a time series.
        
The function replaces any missing data by linear interpolation.

Returns the dataset with the interpolated values.

'''
def imputationByInterpolation(data):
    df = pd.DataFrame(data)
    result = df.interpolate(method = 'linear')
    return result