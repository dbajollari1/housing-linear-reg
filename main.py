import numpy as np 
import datacleaning
import matplotlib.pyplot as plt




def main():
    dataArr = datacleaning.init_data("data/housing.csv")
    data = np.array(dataArr[1:], dtype='float32')

    #plot house price to area
    # plt.scatter(np.flip(data.T[1]), np.flip(data.T[0]))
    # plt.xlabel('Area')
    # plt.ylabel('House Prices') 
    # plt.show()

    datacleaning.normalize(data)
    print(data)

if __name__=="__main__":
    main()