import numpy as np 
import datacleaning
import matplotlib.pyplot as plt


def plot_initial_data(data): 
    #plot house price to area
    plt.scatter(np.flip(data.T[1]), np.flip(data.T[0]))
    plt.xlabel('Area')
    plt.ylabel('House Prices') 
    plt.show()

def main():
    dataArr = datacleaning.init_data("data/housing.csv")
    data = np.array(dataArr[1:], dtype='float32')

    datacleaning.normalize(data)
    np.random.shuffle(data) #randomize rows in data
  

    # number of rows in data equals 545 so to make around 80/20 training and test split, we need to split array into 435 training examples, and 90 test examples 
    data_train, data_test = data[:435,:], data[435:,:]
    
    zeroFeature = np.zeros(data.shape[1]) #need to make x0 feautre to make operations cleaner and easier 
    data_train = np.vstack((zeroFeature,data_train))
    data_test = np.vstack((zeroFeature,data_test))

    
    X_train = data_train[:,1:-1]
    Y_train = data_train[:,0]

    X_test = data_test[:,1:-1]
    Y_test = data_test[:,0]


    

if __name__=="__main__":
    main()