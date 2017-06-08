__author__ = 'chinmay kulkarni'

import csv

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

    for i in range(1,13):

        sum=sum+((x[i]-y[i])**2)

    return (sum**0.5)

def centroid(file1,index1,index2,clusters,clusters2):
    '''
    function to calculate centroid
    :param file1: file as list of list
    :param index1: the index to be merged in
    :param index2: the index to be merged
    :param clusters: clusters in the form of tree as an array
    :param clusters2: list of clusters
    :return:clusters,clusters2 and updated file
    '''





    for index in range(1,len(file1[index1])):


        file1[index1][index]=(file1[index1][index]+file1[index2][index])/2.0

    #cluster 2 is always mereged ,irrespective of its size
    #print((len(clusters2[index2])))
    #if minimum size is desired then,
    #print(min((len(clusters2[index2]),len(clusters2[index1]))))


    #the index2 instance in file is popped because it is merged in indx1
    file1.pop(index2)

    #Normal cluster list
    clusters2[index1]=clusters2[index1]+clusters2[index2]

    #clusters in a form of tree as an array
    if(len(clusters[index1])==1):
         clusters[index1]=clusters[index1]+clusters[index2]

    else:

        if len(clusters[index2])==1:

            b=clusters[index2][0]

            d=[]

            d.append(clusters[index1])

            d.append(b)

            clusters[index1]=d

        else:
            for i in range(0,len(clusters[index2])):

                d=[]

                d.append(clusters[index2][i])

                c=[]

                c.append(clusters[index1])


                c.append(d)


                clusters[index1]=c

    #clusters[index1].append(clusters[index2])



    clusters.pop(index2)
    #clusters2.pop(index2)


    return clusters,file1,clusters2



def agglomerative_clustering(file1,clusters,clusters2):
    '''
    recursive function to perform clystering
    :param file1:file as list of list
    :param clusters: list of 100 clusters
    :param clusters2:list of 100 clusters
    :return:clusters as tree and normal clusters
    '''

    #list of list in the form of [recevd distance, index1, index2]
    main_list=[]

    #to loop through every instance
    for i in range(0,len(file1)):


        for j in range(i+1,len(file1)):

            sublist=[]

            rcvd_distance=euclidean_distance(file1[i],file1[j])

            sublist.append(rcvd_distance)
            sublist.append(i)
            sublist.append(j)

            #adding every combination of diffrent instances distances and index
            main_list.append(sublist)


    #sorting list accrding to the distance
    main_list.sort(key=lambda main_list:main_list[0])
    #print(main_list)

    #the sorted list will give out indices of instances with least distances
    small_index=main_list[0][1]
    big_index=main_list[0][2]



    #calling function to calculate centroid and update smaller index instance with centroid values of small index and big index
    clusters,file1,clusters2=centroid(file1,small_index,big_index,clusters,clusters2)




    #base case, if we change it to "==1" it will give out one big cluster
    if(len(file1)==3):


        return clusters,file1,clusters2

    else:

        return agglomerative_clustering(file1,clusters,clusters2)



def main():
    '''
    main functione operating the flow of whole program
    :return:none
    '''


    file1name='Data.csv'

    file1=CSVparser(file1name)

    #headers removed
    file1.pop(0)

    #intializing 100 clusters
    clusters=[]

    for i in range(1,101):

        individual_clusters=[]

        individual_clusters.append(i)

        clusters.append(individual_clusters)

    clusters2=clusters



    #string to float conversion of values
    for i in range(0,len(file1)):

        for j in range(1,len(file1[0])):

            file1[i][j]=float(file1[i][j])



    clusters,file2,clusters2=agglomerative_clustering(file1,clusters,clusters2)

    print("Cluster 1: 50 IDs")
    print(clusters[0])
    print()

    print("Cluster 2: 17 IDs ")
    print(clusters[1])
    print()

    print("Cluster 3: 33 IDs")
    print(clusters[2])








main()