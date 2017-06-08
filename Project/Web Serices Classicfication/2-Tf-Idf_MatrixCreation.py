__author__ = 'chinmay'

import nltk,os,csv
from sklearn.feature_extraction.text import TfidfVectorizer


path = 'F:/OWLS-TC'
token_dict = {}

#tokenizing the txt files
def tokenize(text):
    tokens = nltk.word_tokenize(text)

    return tokens

#loops to parse all the files in the OWLS tokens generated folder for each category
for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file

        category=subdir.split("\\")


        shakes = open(file_path, 'r')
        text = shakes.read()
        lowers = text.lower()

        file=file+"$"+str(category[1])

        token_dict[file] = lowers


#TF-IDF matrix creation
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english', min_df = 0)
tfs = tfidf.fit_transform(token_dict.values())

tf_idf_values=tfs.toarray()
features=tfidf.get_feature_names()
file_name=list(token_dict.keys())

main_csv=[]

sublist=[]

#Writing the TF-IDF matrix to a csv

for i in range(0,len(features)+2):

    if i<len(features):

        sublist.append(features[i])

    if i==len(features):

        sublist.append("FileName")

    if i==len(features)+1:

        sublist.append("Category")

print(len(sublist))

main_csv.append(sublist)

for j in range(0,len(file_name)):

    sublist1=[]

    res=file_name[j]
    name=res.split("$")

    FileName=name[0]
    Category=name[1]



    for k in range(0,len(tf_idf_values[j])):

        sublist1.append(tf_idf_values[j][k])

    sublist1.append(FileName)
    sublist1.append(Category)

    main_csv.append(sublist1)

with open("data.csv", "w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(main_csv)
