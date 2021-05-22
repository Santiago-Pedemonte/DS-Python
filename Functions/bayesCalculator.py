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