__author__ = 'chinmay'

import json
import re,csv,os,glob
import nltk
from nltk.corpus import stopwords
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()


#Function to read dictionary of eords as list
def wordlist():
    with open('words.txt') as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    return content




#method to parse JSON file
def parseJson(filename):

        with open(filename) as data_file:
                data = json.load(data_file)

        return data


#method to convert json file data to individual text files
def JsonToTxt(data,content):

        category=[]
        title=[]
        summary=[]
        description=[]
        tags=[]

        count=0

        for i in range(0,len(data["api"])):

                category.append(data['api'][i]['category'])

                if isinstance(data['api'][i]['title'],list):

                        titleStr=""

                        for j in range(0,len(data['api'][i]['title'])):

                                titleStr+=data['api'][i]['title'][j]

                        titleFinal=re.sub('&039;.','',titleStr)


                        title.append(titleFinal)

                else:
                        title.append(data['api'][i]['title'])


                if isinstance(data['api'][i]['summary'],list):

                        summaryStr=""

                        for j in range(0,len(data['api'][i]['summary'])):

                                summaryStr+=data['api'][i]['summary'][j]

                        FinalSummary=re.sub('(&amp;039;.)|(&amp;039;)','',summaryStr)
                        summary.append(FinalSummary)

                else:

                        summary.append(data['api'][i]['summary'])

                if isinstance(data['api'][i]['description'],list):

                        descriptionStr=""

                        for j in range(0,len(data['api'][i]['description'])):

                                descriptionStr+=data['api'][i]['description'][j]

                        Finaldes=re.sub('(&amp;039;.)|(&amp;039;)','',descriptionStr)

                        description.append(Finaldes)

                else:

                        description.append(data['api'][i]['description'])

                if isinstance(data['api'][i]['Tags'],list):

                        tagsStr=""

                        for j in range(0,len(data['api'][i]['Tags'])):

                                tagsStr+=" "+data['api'][i]['Tags'][j]


                        tags.append(tagsStr)

                else:
                        tags.append(data['api'][i]['Tags'])


        #TOkenizing The words present in individual API text file
        for i in range(0,len(category)):

                print(i)

                WordList=""

                WordList+=str(title[i])
                WordList+=" "+str(category[i])
                WordList+=" "+str(tags[i])
                WordList+=" "+str(summary[i])
                WordList+=" "+str(description[i])

                WordList1=WordList.split(" ")

                WordList2=[]

                for k in range(0,len(WordList1)):

                        WordList2.append(re.sub(r'[\W_]+|\d+', '', WordList1[k].lower()))



                filtered_words = [word for word in WordList2 if word not in stopwords.words('english')]
                filtered_words=[word for word in filtered_words if word not in ['']]
                filtered_words=[word for word in filtered_words if word in content]

                #print(filtered_words)


                try:
                        filename=re.sub("\/|\?|\*","",title[i])
                        theFile=open("F:/api_data/"+str(filename)+".txt", 'w+')

                        OutList=""

                        for l in range(0,len(filtered_words)):

                                OutList+=str(filtered_words[l])+" "

                        theFile.write(OutList)
                except:
                        print(title[i])
                        continue

#method to return stemmed words
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

#Method to return tokenize words
def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)


    return stems


def main():

        content=wordlist()
        apiData=parseJson("api_json",content)
        JsonToTxt(apiData)





        path = 'F:/api_data'
        token_dict = {}




        count=0

        filePathList=[]

        #parsing text files of individual APIs
        for subdir, dirs, files in os.walk(path):
            for file in files:
                file_path = subdir + os.path.sep + file

                filePathList.append(file_path)

        final_files=random.sample(filePathList,11184)


        for i in range(0,len(final_files)):
                count+=1


                nameList=final_files[i].split("\\")

                shakes = open(final_files[i], 'r')
                text = shakes.read()
                lowers = text.lower()

                fileName=str(nameList[1])


                token_dict[fileName] = lowers



        #TF-IDF matrix generation of al files
        tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english',use_idf=True)
        tfs = tfidf.fit_transform(token_dict.values())

        #TF-IDF values of individual array
        tf_idf_values=tfs.toarray()

        #Words as features
        features=tfidf.get_feature_names()

        #Filenames
        file_name=list(token_dict.keys())




        main_csv=[]

        sublist=[]

        for i in range(0,len(features)+1):

            if i<len(features):

                sublist.append(features[i])

            if i==len(features):

                sublist.append("FileName")



        print(len(sublist))

        main_csv.append(sublist)

        for j in range(0,len(file_name)):

            sublist1=[]

            FileName=file_name[j]




            for k in range(0,len(tf_idf_values[j])):

                sublist1.append(tf_idf_values[j][k])

            sublist1.append(FileName)


            main_csv.append(sublist1)

        #writing file as CSV

        with open("data1.csv", "w",newline="") as f:
            writer = csv.writer(f)
            writer.writerows(main_csv)


main()