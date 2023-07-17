import numpy as np 
import datacleaning
import matplotlib.pyplot as plt




def main():
    dataArr = datacleaning.init_data("data/housing.csv")
    arr = np.array(dataArr[1:], dtype='float32')
    print(np.flip(arr.T[0]))
    x = []
    for i in range(545): 
        x.append(i+1)
    plt.scatter(x, np.flip(arr.T[0]))
    plt.ylabel('House Prices') 
    plt.show()

if __name__=="__main__":
    main()