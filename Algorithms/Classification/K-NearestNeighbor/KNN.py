__author__ = 'chinmay kulkarni'

import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

def CSVparser(file1name):
    '''
    Function to parse csv
    :param file1name: name of file to be parsed
    :return:file as list of list
    '''

    file1=[]

    with open(file1name, 'r') as f:

        data = csv.reader(f)

        for row in data:
            file1.append(row)

    return file1


def euclidean_distance(x,y):
    '''
    function to calculate euclidean distance
    :param x:instance 1
    :param y: instance 2
    :return:distance between 2 instances
    '''

    sum=0

    for i in range(0,len(x)):

        sum=sum+((x[i]-y[i])**2)

    return (sum**0.5)

def most_common(input_file):
    """

    :param input_file: input list
    :return:Most common element in the list
    """

    return max(set(input_file), key=input_file.count)

def misclassifications(input_file,mainlist,k):
    """

    :param input_file:input csv file as list of list
    :param mainlist:list of each index with nearest neighbors
    :param k:number of neighbor
    :return:count of missclassified instances, indexes of missclassified indexes
    """

    neighbor_classlist=[]

    #misclassified instances count
    count=0

    for i in range(0,len(input_file)):

        sublist=[]
        for j in range(0,k+1):

            sublist.append(input_file[mainlist[i][j][2]][3])


        neighbor_classlist.append(sublist)

    misclassified_instance_list=[]

    for i in range (0,len(neighbor_classlist)):

        class_val=most_common(neighbor_classlist[i])

        if input_file[i][3]!=class_val:

                misclassified_instance_list.append(i)
                count+=1

    return count,misclassified_instance_list

def KNN(input_file):
    """

    :param input_file:Input csv fiels as list of list
    :return:list of misclassified instances at each value of k, list of misclassified instances index at k
    in both of these index of list is considered to be k
    """

    #Count of misclassified instances
    misclassification_no=[]

    #indices of misclassified instances
    misclassified_instances_final=[]

    #list of nearest neighbors of each instance value
    mainlist_1=[]



    for i in range(0,len(input_file)):


         mainlist=[]

         for j in range(0,len(input_file)):
                sublist=[]

                if i==j:

                    continue

                first_point=[]
                second_point=[]

                x1=input_file[i][0]
                y1=input_file[i][1]
                z1=input_file[i][2]

                x2=input_file[j][0]
                y2=input_file[j][1]
                z2=input_file[j][2]

                first_point.append(x1)
                first_point.append(y1)
                first_point.append(z1)

                second_point.append(x2)
                second_point.append(y2)
                second_point.append(z2)

                distance=euclidean_distance(first_point,second_point)

                sublist.append(distance)
                sublist.append(i)
                sublist.append(j)

                mainlist.append(sublist)

         #sorting neighbor list on the basis of distance
         mainlist.sort(key=lambda mainlist:mainlist[0])
         mainlist_1.append(mainlist)


    #checking for misclassification for k 1 to 30
    for k in range(0,31):

        misclassified_instances,count=misclassifications(input_file,mainlist_1,k)



        misclassification_no.append(count)
        misclassified_instances_final.append(misclassified_instances)

    return misclassification_no,misclassified_instances_final

def main():

     filename="DATA.csv"

     file1=CSVparser(filename)

     #Deleting Headers
     file1.pop(0)

     #String to float conversion
     for index_row in range(0,len(file1)):

        for index_col in range(0,len(file1[0])):

            file1[index_row][index_col]=float(file1[index_row][index_col])


     #list of misclassified instances and coun on given K
     instances,no=KNN(file1)

     #used pandas package for quickly deleting missclassified instances from file to
     #avoid noise values
     #at k=21, I got least misclassified instances i.e. 104
     df=pd.read_csv("Data.csv")
     df = df[df.index.isin(instances[21]) == False]



     





main()
