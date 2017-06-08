__author__ = 'chinmay kulkarni'

import csv
import random
import matplotlib.pyplot as plt


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

def center_calc(clusterList,input_file):
    '''
    Function to calculate centroid of different data points
    :param clusterList: List of clusters as instance no in original file
    :param input_file: Original CSV file as list of list
    :return:Centre list as [x,y,z]
    '''

    centroid_list=[]

    for i in range(0,len(clusterList)):


        sum_Attrib1=0
        sum_Attrib2=0
        sum_Attrib3=0

        for j in range(0,len(clusterList[i])):

            sum_Attrib1+=input_file[clusterList[i][j]][0]
            sum_Attrib2+=input_file[clusterList[i][j]][1]
            sum_Attrib3+=input_file[clusterList[i][j]][2]

        centroid_Attrib1=sum_Attrib1/len(clusterList[i])
        centroid_Attrib2=sum_Attrib2/len(clusterList[i])
        centroid_Attrib3=sum_Attrib3/len(clusterList[i])

        sub_list=[]

        sub_list.append(centroid_Attrib1)
        sub_list.append(centroid_Attrib2)
        sub_list.append(centroid_Attrib3)

        centroid_list.append(sub_list)



    return centroid_list

def SSE_calc(clusters,centers,input_file):
    '''
    Function to calculate sum of sqaured errors
    :param clusters: Clusters represented as intance number in original data file
    :param centers: list of centers for clusters
    :param input_file: original CSV file
    :return:SSE
    '''

    sum=0


    for i in range(0,len(clusters)):

        for j in range(0,len(clusters[i])):

            dist=euclidean_distance(input_file[clusters[i][j]],centers[i])
            sum+=(dist**2)

    return sum

def Kmeans(input_file):
    '''
    Function to perform Kmeans Clustering
    :param input_file: Original CSV filr
    :return:SSE list for different vslues of K
    '''

    #Sum of square list for different K's
    SSE=[]

    #K vlaues ranging from 1 to 20
    for k in range(1,20):
    #For k=8 clusters uncomment this,for (x,y)plot and comment original for loop statement
    #for k in range(8,9):

        #Random centers list for first iteration
        RandomCenters=[]


        for i in range(0,len(input_file)):

            RandomCenters.append(i)

        #selecting K random indexes from 0 to 399
        RandomCenters=random.sample(RandomCenters,k)


        #Boolean value to check if centers are chaging or not
        #Stopping condition for K means algorithm
        change_centers=True

        #no of iteration
        iteration=0

        #List to maintain different members of various clusters
        main_list=[[]]*k

        #New mean list
        new_centers=[]


        #Stopping condition set
        while(change_centers!=False):


                #for first iteration
                if iteration==0:

                    for index_all in range(0,len(input_file)):

                        nearest_center_dist=float('inf')

                        for index_random in range (0,len(RandomCenters)):

                            dist=euclidean_distance(input_file[index_all],input_file[RandomCenters[index_random]])

                            if dist<=nearest_center_dist:

                                nearest_center_dist=dist
                                final_index=index_random

                        if len(main_list[final_index])==0:

                            main_list[final_index]=[index_all]

                        else:
                            main_list[final_index].append(index_all)


                    iteration=1

                #for second iteration
                elif iteration==1:

                    new_centers=center_calc(main_list,input_file)
                    main_list=[[]]*k

                    for index_all in range(0,len(input_file)):

                        nearest_center_dist=float('inf')

                        for index_new in range (0,len(new_centers)):

                            dist=euclidean_distance(input_file[index_all],new_centers[index_new])

                            if dist<nearest_center_dist:

                                nearest_center_dist=dist
                                final_index=index_new

                        if len(main_list[final_index])==0:

                            main_list[final_index]=[index_all]

                        else:
                            main_list[final_index].append(index_all)

                    iteration=2

                #For any iteration>2
                elif iteration>1:

                    new_centers_2=center_calc(main_list,input_file)

                    #To check if centers are changing are not
                    new_centers_2.sort(key=lambda new_centers_2:new_centers_2[0])
                    new_centers.sort(key=lambda new_centers:new_centers[0])

                    #stopping condition
                    if new_centers==new_centers_2:

                        break


                    new_centers=new_centers_2




                    main_list=[[]]*k

                    for index_all in range(0,len(input_file)):

                        nearest_center_dist=float('inf')

                        for index_new in range (0,len(new_centers)):

                            dist=euclidean_distance(input_file[index_all],new_centers[index_new])

                            if dist<=nearest_center_dist:

                                nearest_center_dist=dist
                                final_index=index_new

                        if len(main_list[final_index])==0:

                            main_list[final_index]=[index_all]

                        else:
                            main_list[final_index].append(index_all)

                        iteration+=1

        #appending SSE values to each value of k , where value of k in list is index+1
        SSE.append(SSE_calc(main_list,new_centers,input_file))

    #For k=8 clusters uncomment this for plot and comment original return
    #return SSE,main_list
    return SSE


def main():

    filename="Data.csv"

    #original File as LIST
    file1=[]

    file1=CSVparser(filename)

    #Deleting Headers
    file1.pop(0)

    #String to float conversion
    for index_row in range(0,len(file1)):

        for index_col in range(0,len(file1[0])):

            file1[index_row][index_col]=float(file1[index_row][index_col])

    print(file1)



    #SSE list received
    #SSE=Kmeans(file1)
    #For k=8 clusters uncomment this for plot and comment above call to kmeans function
    #SSE,clusters=Kmeans(file1)

    #Plotting K vs SSE graph
    SSE_val=[]
    k=[]

    # for i in range(0,len(SSE)):
    #
    #     SSE_val.append(SSE[i])
    #     k.append(i+1)
    #
    # fig = plt.figure()
    # plt.scatter(k,SSE_val)
    # plt.xlabel("K value for clustering")
    # plt.ylabel("SSE for particular K")
    # fig.suptitle("K vs SSE plot",fontsize=20)
    # plt.show()



    #Uncomment to plot graph and visualise clusters, set k=8 by changing for loop in Kmeans() function
    #Comment the above stated for loop and K vs sse plot



    # coordinates_cluster_1=[]
    # coordinates_cluster_2=[]
    # coordinates_cluster_3=[]
    # coordinates_cluster_4=[]
    # coordinates_cluster_5=[]
    # coordinates_cluster_6=[]
    # coordinates_cluster_7=[]
    # coordinates_cluster_8=[]
    #
    #
    #
    # for i in range(0,len(clusters)):
    #
    #     sublist=[]
    #     xcoord=[]
    #     ycoord=[]
    #
    #     for j in range(0,len(clusters[i])):
    #
    #         xcoord.append(file1[int(clusters[i][j])][0])
    #         ycoord.append(file1[int(clusters[i][j])][1])
    #
    #     if i==0:
    #         coordinates_cluster_1.append(xcoord)
    #         coordinates_cluster_1.append(ycoord)
    #
    #     if i==1:
    #         coordinates_cluster_2.append(xcoord)
    #         coordinates_cluster_2.append(ycoord)
    #
    #     if i==2:
    #         coordinates_cluster_3.append(xcoord)
    #         coordinates_cluster_3.append(ycoord)
    #
    #     if i==3:
    #         coordinates_cluster_4.append(xcoord)
    #         coordinates_cluster_4.append(ycoord)
    #
    #     if i==4:
    #         coordinates_cluster_5.append(xcoord)
    #         coordinates_cluster_5.append(ycoord)
    #
    #     if i==5:
    #         coordinates_cluster_6.append(xcoord)
    #         coordinates_cluster_6.append(ycoord)
    #
    #     if i==6:
    #         coordinates_cluster_7.append(xcoord)
    #         coordinates_cluster_7.append(ycoord)
    #
    #     if i==7:
    #         coordinates_cluster_8.append(xcoord)
    #         coordinates_cluster_8.append(ycoord)
    #
    #
    # fig = plt.figure()
    # ax1 = fig.add_subplot(111)
    #
    # ax1.scatter(coordinates_cluster_1[0],coordinates_cluster_1[1],c='r',marker="o",label='cluster 1')
    # ax1.scatter(coordinates_cluster_2[0],coordinates_cluster_2[1],c='g',marker="o",label='cluster 2')
    # ax1.scatter(coordinates_cluster_3[0],coordinates_cluster_3[1],c='b',marker="o",label='cluster 3')
    # ax1.scatter(coordinates_cluster_4[0],coordinates_cluster_4[1],c='y',marker="o",label='cluster 4')
    # ax1.scatter(coordinates_cluster_5[0],coordinates_cluster_5[1],c='m',marker="o",label='cluster 5')
    # ax1.scatter(coordinates_cluster_6[0],coordinates_cluster_6[1],c='k',marker="o",label='cluster 6')
    # ax1.scatter(coordinates_cluster_7[0],coordinates_cluster_7[1],c='0.75',marker="o",label='cluster 7')
    # ax1.scatter(coordinates_cluster_8[0],coordinates_cluster_8[1],c='c',marker="o",label='cluster 8')
    #
    # ax1.set_xlabel("X axis")
    # ax1.set_ylabel("Y axis")
    # fig.suptitle("Clusters when K=8",fontsize=20)
    #
    # plt.legend(loc='upper left');
    #
    # plt.show()







    #plt.plot(k,SSE_val)
    #plt.show()


    #For k=8,clusters are as follows
    # for i in range(0,len(clusters)):
    #
    #     print('cluster #'+str(i+1)+' length:'+str(len(clusters[i])))
    #     print(clusters[i])
    #
    #
    #
    # print('SSE:'+str(SSE))


main()