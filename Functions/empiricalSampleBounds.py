'''
Empirical Sample Bounds Calculator

This function receives 2 arguments/inputs, in this order:
    1) A variable that represents the dataset/distribution/sample
    2) The probability mass bounds that define the center of the distribution (e.g. 95, 99 or 50)
        
The function computes the upper bound (where the right tail starts) and the lower bound (where the left tail starts).

Returns these values as two variables.

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