# Lab 1: Linear Regression (corresponding to lecture handout 1)
import numpy as np

# This function computes the polynomial of order 'order' corresponding to a least-squares fit
# to the data (x, y), where 'y' contains the observed values and 'x' contains the x-ordinate
# of each observed value.
#
# The normal equation is sloved in the function 'linear regression'.
def LS_poly(x, y, order, eps = 0):
    # First build the polynomial design matrix (relies only x-ordinates, not observed values)
    X = polynomial_design_matrix(x, order);
    # Then find the polynomial using this matrix and the values 'y'.
    w = linear_regression(X, y, eps=eps);
    return w

# Computes the polynomial design matrix.
#
# For a vector 'x', this contains all powers up to 'order'
# of each element of 'x'.  This kind of matrix is also called
# a Vandermonde matrix.
#
# The numpy array 'x' contains the x-ordinates (x-axis
# values) which we are analyzing.
def polynomial_design_matrix(x, order=1):
    # Create a matrix of zeros, with 'length-of-x' rows and 'order+1' cols
    X = np.zeros(shape=(x.size,order+1))

    # EXERCISE 1: fill the body of this function.
    # The exponentiation (power) operator in Python is '**'.
    for p in range(0, order+1):
        for i in range(x.size):
            X[i][p] = x[i] ** p
    return X


# Given values 'y' and the polynomial design matrix for the x-ordinates of those
# values in 'X', find the polynomial having the best fit:
#
# theta = ((X'X + I)^(-1))*X'y
#
# This uses numpy to solve the normal equation (see slide 16 of handout 1)
def linear_regression(X, y, eps=0):
    order = X.shape[1] - 1;
    M = np.dot(X.transpose(), X)

    # EXERCISE 2: implement Tikhonov regularisation.
    # See lecture handout 1, slide 35.
    print("Eps: " + str(eps))
    # <add 'eps' times the identity matrix to M>
    M = M + np.identity(X.shape[1])*eps
    theta = np.dot(np.linalg.inv(M), np.dot(X.transpose(), y))
    return theta

# EXERCISE 3: implement computation of mean squared error between two vectors
def mean_squared_error(y1, y2):
    diff_sum = 0
    for i in range(y1.size):
        diff = y1[i] - y2[i]
        sqr = diff**2
        diff_sum += sqr
    
    return diff_sum/y1.size 

# EXERCISE 4: return the number of the best order for the supplied
# data (see the notebook).
def question_4():
    return 3   # replace '0' with your answer.
