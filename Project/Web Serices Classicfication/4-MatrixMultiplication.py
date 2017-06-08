__author__ = 'chinmay'


import numpy as np
import csv

def CSVparser(filename):

    file=[]

    with open(filename, 'r') as f:

        data = csv.reader(f)

        for row in data:

            file.append(row)
    return file


#Method to Multiply TF-IDF matrix and Semantic Similarity
def main():

    SM=CSVparser('C:/Users/chinmay/Desktop/ws/similarity-matrix.csv')
    TfIdf=CSVparser('C:/Users/chinmay/Desktop/ws/Tf-Idf-matrix.csv')

    for i in range(0,len(SM)):

        for j in range(0,len(SM[0])):

            SM[i][j]=float(SM[i][j])

    for k in range(0,len(TfIdf)):

        for l in range(0,len(TfIdf[0])):

            TfIdf[k][l]=float(TfIdf[k][l])






    res_array=(np.matmul(TfIdf,SM))

    res_list=res_array.tolist()

    with open("MultipliedData.csv", "w",newline="") as f:

        writer = csv.writer(f)
        writer.writerows(res_list)



main()




