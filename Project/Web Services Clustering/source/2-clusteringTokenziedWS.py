__author__ = 'chinmay'



import pandas as pd
import random
from sklearn.externals import joblib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA



#Cluster Prototype for 11184 services
df_all_Clus = pd.read_csv('all_clusters.csv')
category_names_all=list(df_all_Clus['Category'])
clust_nums_all=list(df_all_Clus['Clust'])



#Reading Tf-Idf matrix for all APIs
df = pd.read_csv('data1.csv', low_memory=False,encoding = "ISO-8859-1")
print("File Read")

#Diiferent Word as Features
features=list(df.columns[:-1])

X=df[features]
filenames_list=list(df['FileName'])

##Principle component analysis On the TF-IDF matrix loaded using pickle object
# pca = PCA(n_components=3).fit(X)
# pca = pca.transform(X)
# joblib.dump(pca,  'doc_PCA_all_3d.pkl')
# print("pca done")


###K means code commented due to long running time and saved as pickle object
##which is loaded to display the results of clustering.


# km = KMeans(n_clusters=34) #for i in Ks]
# km.fit(X)
#joblib.dump(km,  'doc_cluster_all.pkl')

km = joblib.load('doc_cluster_all.pkl')

clusters=(km.labels_.tolist())

#Creating dictionary for cluster name and cluster id
web_services={'title':filenames_list,'cluster':clusters}
frame = pd.DataFrame(web_services,index=[clusters],columns = ['title','cluster'])


order_centroids = km.cluster_centers_.argsort()[:, ::-1]

print("The clusters formed are as follows")

#Print cluster prototypes and API names
for i in range(34):
    print("Cluster "+str(i+1)+" Prototypes(Keywords):")

    for ind in order_centroids[i, :20]:
        print(features[ind].split(' '), end=',')
    print()
    print()

    print("Cluster"+str(i+1)+" Memebers:")
    for title in frame.ix[i]['title']:

         temp=title.encode("utf-8")

         print(str(temp), end=',')
    print()
    print()
    print("---------------------------------------------")

#creating color map of 34 colors to show 34 clusters
cmap = plt.cm.get_cmap("hsv", 35)

#importing pca 3d model
pca_3d= joblib.load('doc_PCA_all_3d.pkl')

xs, ys, zs= pca_3d[:, 0], pca_3d[:, 1],pca_3d[:, 2]



#grouping clusters and infered category of clustrs using cluster prototype
cluster_list=range(0,34)
cluster_colors=[]
for i in range(0,34):
    cluster_colors.append(cmap(i))

cluster_colors_dict = dict(zip(cluster_list,cluster_colors))
cluster_name_dict=dict(zip(clust_nums_all,category_names_all))

#Dataframe created for PCA components
df = pd.DataFrame(dict(x=xs, y=ys,z=zs,label=clusters, title=list(frame['title'])))

groups = df.groupby('label')


#plotting 3d plot for PCA componenets
import pylab
from mpl_toolkits.mplot3d import Axes3D
fig = pylab.figure()
ax = Axes3D(fig)


for name,group in groups:


    ax.scatter(group.x, group.y,group.z,marker='o',label=cluster_name_dict[name], c=cluster_colors_dict[name])
    ax.set_aspect('auto')
    ax.set_xlabel("PCA component 1")
    ax.set_ylabel("PCA component 2")
    ax.set_zlabel("PCA component 3")
    plt.title("CLUSTERS PLOT FOR 3 PCA COMPONENTS")


#plotting 2d plot for PCA componenets
ax.legend(numpoints=1,loc='best')

plt.show()

fig, ax = plt.subplots(figsize=(17, 9))
ax.margins(0.05)




for name,group in groups:


    ax.scatter(group.x, group.y,marker='o',label=cluster_name_dict[name], c=cluster_colors_dict[name])
    ax.set_aspect('auto')
    plt.xlabel("PCA component 1")
    plt.ylabel("PCA component 2")

    plt.title("CLUSTERS PLOT FOR 2 PCA COMPONENTS")



ax.legend(numpoints=1,loc='best')

plt.show()





