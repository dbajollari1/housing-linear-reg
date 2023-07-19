import numpy as np 

class LinearRegression:
    def __init__(self, data):
        self.data = data

    def hypothesis(self,x,theta): 
        return np.matmul(theta.T, x)
    
    def cost_function(self,theta,y):
        return sum((hypothesis(x) - y)**2)


