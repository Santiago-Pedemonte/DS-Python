'''
This function receives a numpy array and outputs the desired metric 
for said array over a user-selected window. The size of the output varies with
the size of the arrays and the size of the window.

The input for the function should be in the order: (array, flag, window)
With:
    -Array: A 1D numpy array to calculate Mean or Standard Deviation, or a 2D numpy array to calculate Correlation.
    -Flag: A number to denote the operation desired. 1 for Mean // 2 for SD // 3 for Correlation.
    -Window: A number to denote the size of the window over which the specified metric is to be calculated.
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