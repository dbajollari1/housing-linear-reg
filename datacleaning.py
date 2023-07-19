import csv
import numpy as np

def convertStringtoInt(str): 
    if str == "yes": 
        return 1 
    elif str == "no": 
        return 0

def convertFurnishedtoNum(str): 
    if str == "furnished": 
        return (1,0,0) 
    if str == "semi-furnished":  
        return (0,1,0) 
    if str == "unfurnished": 
        return (0,0,1)

def init_data(filePath): 
    returnArr = []
    with open(filePath, 'r') as file:
        csvreader = csv.reader(file)
        i = 0 
        for row in csvreader:
            if i == 0: 
                row[12] = "furnished"
                row.append("semi-furnished")
                row.append("unfurnished")
                returnArr.append(row)
                i += 1 
            else: 
                vals = convertFurnishedtoNum(row[12])
                row[12] = vals[0]
                row.append(vals[1])
                row.append(vals[2])
                row[5] = convertStringtoInt(row[5])
                row[6] = convertStringtoInt(row[6])
                row[7] = convertStringtoInt(row[7])
                row[8] = convertStringtoInt(row[8])
                row[9] = convertStringtoInt(row[9])
                row[11] = convertStringtoInt(row[11])
                returnArr.append(row)
                i += 1 
    return returnArr

def normalize(data): 
    for i in range(0,data.shape[1]-1): #loop through the columns
	    data[:,i] = ((data[:,i] - np.mean(data[:,i]))/np.std(data[:, i])) #calculate norm for entire column

            