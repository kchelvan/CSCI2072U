# Keshopan Arunthavachelvan
# 100694939
# January 21, 2020
# Assignment One Part Two

def steffensen(f, df, x, epsilon, iterations):
    '''
    Description: Calculates solution of iterations using Newton's method with using recursion

    Parameters
    f: function that is being used for iteration (residual)
    df: derivative of the function f
    x: initial point
    epsilon: lower bound for when the iteration should terminate (estimated error)
    iterations: maximum number of iterations
    '''
    # Iterates through the Steffensen's iteration
    for i in range(0, iterations):
        # Variable Instantiation
        y1 = x
        # Performs Newton's step and stores values
        y2 = x - float(f(y1))/float(df(y1))
        y3 = x - float(f(y2))/float(df(y2))

        # Using the previously saves values from Newton's Steps, perform an iteration with Steffensen's iterations
        x = y1 - ((y2 - y1) ** 2 / (y3 - (2 * y2) + y1))

        # If current solution is less than the estimated error or residual, then print converged and break the loop
        print('The solution at the ' + str(i) + 'th iteration is ' + str(f(x)) + '.')
        if (f(x) < epsilon):
            print "Converged"
            return x
    
    # If current iteration exceeds maximum number of iterations, print the current solution and return null
    print('Next iteration exceeds maximum number of iterations. Current solution is ' + str(f(x)) + ". \nDoes not Converge.") 
    return None
