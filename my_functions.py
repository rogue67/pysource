##################################
#   Function for linear regression.
#   lin_reg(x,y)
#   Roger Forsman & ??
#
##################################
import numpy as np
import matplotlib.pyplot as plt

def lin_reg(x, y):
    values, cov = np.polyfit(x,y,1, cov = True)
    k = values[0]
    m = values[1]
    # Osäkerheter
    u_k = np.sqrt(np.diag(cov))[0]
    u_m = np.sqrt(np.diag(cov))[1]
    return [k, m, u_k, u_m]

def main():
    X = [1,2,3,4,5]
    Y = [6,7,8,9,10]
    ans = lin_reg(X,Y)
if __name__ == "__main__":
    main()