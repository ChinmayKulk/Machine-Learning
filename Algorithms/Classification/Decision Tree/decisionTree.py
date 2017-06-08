__author__ = 'chinmay kulkarni'

import csv

#list of training file data
file_training=[]

def CSVparser(filename):
    '''
    Function to parse csv
    :param filename: name of file to be parsed
    :return:none
    '''
    

    with open(filename, 'r') as f:

        data = csv.reader(f)

        for row in data:
            file_training.append(row)



def gini_calc(a,b,c,d):
    '''
    function to calculate gini coefficient
    :param a:<= the value and belongs to class 1
    :param b:> the value and belongs to class 1
    :param c:<= the value and belongs to class 0
    :param d:> the value and belongs to class 0
    :return:gini coefficient
    '''

    #weighted values
    n1=(a+c)/(a+b+c+d)
    n2=(b+d)/(a+b+c+d)

    #individual probabilities of each class
    p1=(a)/(a+c)
    p2=(c)/(a+c)
    if b==0.0 and d==0.0:
        p3=0
        p4=0
    else:
        p3=(b)/(b+d)
        p4=(d)/(b+d)


    #calculating gini using individual probabilities
    gini1=1-((p1**2)+(p2**2))
    gini2=1-((p3**2)+(p4**2))

    #calculating weighted gini index using individiual gini coefficients
    final_gini=float('%.5f' % round((n1*gini1)+(n2*gini2),5))


    return final_gini



def best_Gini_index(array_file,height):
    '''
    Recursive Function to calculate best gini index among all attributes
    :param array_file:training file as list of list
    :param height:height of tree
    :return:none
    '''

    #list of best_gini_index list
    best_list=[]


    #loop for each attribute
    for k in range(0,3):

        bestGiniIndex=float('inf')

        #loop for each value at that attribute
        for i in range(0,len(array_file)):


            best_split=array_file[i][k]


            j=0

            a=0
            b=0
            c=0
            d=0


            while(j<len(array_file)):



                if(array_file[j][k]<=best_split and array_file[j][3]==1.0):

                    a+=1


                elif(array_file[j][k]<=best_split and array_file[j][3]==0.0):
                    #print("in c")
                    c+=1

                elif(array_file[j][k]>best_split and array_file[j][3]==1.0):
                    #print("in b")
                    b+=1


                elif(array_file[j][k]>best_split and array_file[j][3]==0.0):
                    #print("in d")
                    d+=1

                j=j+1

            #sending a,b,c,d values to function GiniINdex for gini index value
            GiniIndex=gini_calc(a,b,c,d)


            #minimum gini index
            if(GiniIndex<bestGiniIndex):

                bestGiniIndex=GiniIndex
                index=i

        #list of [gini,value,attribute number]
        best_gini_index_list=[]

        best_gini_index_list.append(bestGiniIndex)
        best_gini_index_list.append(array_file[index][k])
        best_gini_index_list.append(k+1)
        best_list.append(best_gini_index_list)


    #to sort best list on the basis of coloumn 1 ie gini index
    best_list.sort(key=lambda best_list:best_list[0])

    print(best_list)


    #best threshold out of all values
    best_threshold=best_list[0][1]

    #best attribute with lowest gini index
    best_attribute=best_list[0][2]

    #print(best_attribute)

    #sorting whole file on best attribute
    array_file.sort(key=lambda array_file:array_file[best_attribute-1])

    #print(array_file)


    #finding the index of best attribute after sorting
    for i in range(0,len(array_file)):

        if (array_file[i][best_attribute-1]==best_threshold):
            index=i


    #splitting the list
    left=array_file[0:index]
    right=array_file[index+1:len(array_file)+1]



    #for left split
    #purity check
    if(all(item[3]==0 for item in left )):

        print("attr"+str(best_attribute)+" <= "+str(best_threshold)+"----->"+"class 0"+"------"+str(height))

    elif(all(item[3]==1 for item in left )):

       print("attr"+str(best_attribute)+" <= "+str(best_threshold)+"----->"+"class 1"+"------"+str(height))

    #if not pure then again recursive splitting takes place untill pure
    else:

        best_Gini_index(left,height+1)


    #for right split
    if(all(item[3]==0 for item in right )):

        print("attr"+str(best_attribute)+" > "+str(best_threshold)+"----->"+"class 0"+"------"+str(height))

    elif(all(item[3]==1 for item in right )):

        print("attr"+str(best_attribute)+" > "+str(best_threshold)+"----->"+"class 1"+"------"+str(height))

    else:

        best_Gini_index(right,height+1)


def main():
    '''
    main function which helps in building decison tree and writes it to classifier program
    :return:none
    '''

    CSVparser('TrainingData.csv')

    #Deleting headers
    file_training.pop(0)

    for i in range(0,len(file_training)):

        for j in range(0,len(file_training[i])):

            file_training[i][j]=float(file_training[i][j])






    best_Gini_index(file_training,1)

    
main()