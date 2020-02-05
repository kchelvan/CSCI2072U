# Keshopan Arunthavachelvan
# 100694939
# January 21, 2020
# Assignment One Part One


def iteration(x0, f, df, tolerance, max_iterations):
    '''
    Description: Calculates solution of iterations using Newton's method with for loop

    Parameters
    x0: initial point
    f: function that is being used for iteration (residual)
    df: derivative of the function f
    tolerance: lower bound for when the iteration should terminate (estimated error)
    max_iterations: maximum number of iterations
    '''

    # Instantiates the current node with the first point
    cur_node = float(x0)
    residual = f(x0)
    # Iterates until the maximum number of iterations is exceeded or the current node is less than the tolerance value
    for i in range(0, max_iterations):
         # If current node is less than the tolerance, print the current solution and return the current node
        if (abs(f(cur_node)) < tolerance):
            print("Found solution of " + str(cur_node) + " at the " + str(i) + "th iteration.")
            print("The estimated error is " + str(abs(residual - cur_node)) + " and the residual is " + str(f(cur_node)))
            return cur_node

        # Uses Newton's step to calculate next solution step
        cur_node = cur_node - float(f(cur_node))/float(df(cur_node))
    
    # If current iteration exceeds maximum number of iterations, print the current solution and return null
    print('Next iteration exceeds maximum number of iterations. Current solution is ' + str(cur_node) + ". \nDoes not Converge.")
    return None
