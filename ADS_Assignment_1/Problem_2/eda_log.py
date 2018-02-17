
#Importing Python Libraries
from lxml.html import parse
import numpy as np
from urllib.request import urlopen
import requests,zipfile,io
import pandas as pd
import math
import seaborn as sns
import re
import numpy as np
import matplotlib.pyplot as plt
import os
get_ipython().magic('matplotlib inline')
import time
import datetime
import logging


    
#defining log function
def main():
    
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S')
    
    y = sys.argv[1]
    
    logfilename = 'log_Edgar_'+ '_' + y + '.txt' 
    logging.basicConfig(filename=logfilename, level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info("Extracting specific file for a month from the EDGAR link")
    

    month=1
    logging.info(path = +++++++'./files/'+ y
    for i in range(0,12):

        if month in range(1,4):qtr = 1; month = "0"+str(month)
        elif month in range(4,7):qtr = 2; month = "0"+str(month)
        elif month in range(7,10): qtr = 3; month = "0"+str(month)
        elif month in range(10,13): qtr = 4
        else :pass
   
    logging.info(parsed = parse(urlopen("http://www.sec.gov/dera/data/Public-EDGAR-log-file-data/"+year+"/Qtr"+qtr+"/log"+year+month+"01.zip"))
    r = requests.get("http://www.sec.gov/dera/data/Public-EDGAR-log-file-data/"+y+"/Qtr"+str(qtr)+"/log"+y+str(month)+"01.zip")
    z =zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    month = int(month) + 1

    logging.info(http://www.sec.gov/dera/data/Public-EDGAR-log-file-data/2003/Qtr2/log20030501.zip


    


    month = 1
    for i in range(0,12):
        if month in range(1, 10) :
            data = pd.read_csv("log"+y+"0"+str(month)+"01.csv")
            print(y+"/Qtr"+str(qtr)+"log"+y+"0"+str(month)+"01.csv")
        elif month in range(10, 13) :
            data = pd.read_csv("log"+y+str(month)+"01.csv")      
            print(y+"/Qtr"+str(qtr)+"log"+y+str(month)+"01.csv")
                 
        month = month +1


    logging.info("Reading the extracted csv file")
    data = pd.read_csv("log20040101.csv")


    logging.info("Computing head values of the data")
    data.head()



    logging.info("Exploring all the variables of data")
    data.info()


    logging.info("Checking count of null values in the data")
    data.isnull().sum()



    logging.info("Exploring structure of data")
    data.describe()


    logging.info("From the above calculations we can say that there are missing values in the data")


    logging.info("Extracting extention from the filename in variable 'extention")
    data['extention'] = data['extention'].apply(lambda x: re.findall("\..*", x)[0][1:])


    logging.info("Extracting extention from the filename in variable 'extention'")
    data['extention']


    logging.info("checking counts of different types of extention")
    data['extention'].value_counts


    logging.info("Exploring unique values of extentions")
    data['extention'].unique()


    logging.info("Plotting countplot for extention variable")
    plt.subplots(figsize=(10,10))
    sns.countplot(x=data['extention'],order=data['extention'].value_counts().index)
    plt.show()


    logging.info("Checking count of null values in the variable 'browser'")
    data['browser'].isnull().sum()


    logging.info("Exploring unique values of browsers")
    data['browser'].unique()



    logging.info("Plotting countplot for browser variable")
    plt.subplots(figsize=(10,10))
    sns.countplot(x=data['browser'],order=data['browser'].value_counts().index)
    plt.show()


    302
                 


    logging.info("Plotting Boxplot between extention and size")
    sns.boxplot(x='extention', y='size', data=data)


    logging.info("Data Cleaning")

    


    logging.info("Filling NULL data in 'size' by the mean of the all the existing values")


    logging.info("Filling NULL data in 'size' by the mean of the all the existing values")
    data['size'].fillna(data['size'].mean(), inplace = True)


    logging.info("Now checking if size variable consists any null or not")
    data['size'].isnull().any()


    logging.info("Checking count of nullvalues if still exist in the data")
    data.isnull().sum()



    logging.info("Since 'browser' contains categorial data so here we replace the NULL values in the browser by the most occuring value")



    logging.info("checking counts of different types of browser")
    data['browser'].value_counts()



    logging.info("Assigning variable x to value of most occurring browser type")
    x=data['browser'].mode()



    logging.info("Imputing value of most occuring browser type in the Null values") 
    data['browser'].fillna(x[0], inplace = True)


    logging.info("checking counts of different types of extention ")
    data['browser'].value_counts()



    logging.info("Now checking if data still has any missing or null values")
    data.isnull().sum()


    logging.info("From above operations we have cleansed our data from all missing and Null values")


    logging.info("Encoding categorical data into numerical data")

    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder = LabelEncoder()
    for i in ['ip','date','time','accession','extention','browser']:
       data[i] = labelencoder.fit_transform(data[i])
    data.head()


    logging.info("Exploring all the variables of data after Encoding")
    data.info()


    logging.info("From above operation we have conerted all out object variables into numeric to explore relationship between variables")


    logging.info("Expolring Data")


    logging.info("Plotting countplot of variable browser to analyze type and count relationship")
    plt.subplots(figsize=(10,10))
    sns.countplot(x=data['browser'],order=data['browser'].value_counts().index)
    plt.show()


    logging.info("Plotting countplot of variable find to analyze type and count relationship")
    plt.subplots(figsize=(10,10))
    sns.countplot(x=data['find'],order=data['find'].value_counts().index)
    plt.show()


    logging.info("Plotting countplot of variable crawler to analyze type and count relationship")
    plt.subplots(figsize=(10,10))
    sns.countplot(x=data['crawler'],order=data['crawler'].value_counts().index)
    plt.show()


    logging.info("Plotting countplot of variable idx to analyze type and count relationship")
    plt.subplots(figsize=(10,10))
    sns.countplot(x=data['idx'],order=data['idx'].value_counts().index)
    plt.show()



    logging.info("Plotting box plot between browser and filesize")
    plt.figure(figsize=(14,12))
    sns.boxplot(x='browser', y='size', data=data);



    logging.info("Plotting subplot to analyze distribution of 'find' variable")
    plt.subplots(figsize=(15,8))
    data['find'].hist(bins=50)
    plt.xticks(list(range(0,110,5)))
    plt.title('find Distribution')
    plt.show()



    logging.info("Plotting subplot to analyze distribution of 'browser' variable")
    plt.subplots(figsize=(15,8))
    data['browser'].hist(bins=50)
    plt.xticks(list(range(0,110,5)))
    plt.title('Browser Distribution')
    plt.show()



    logging.info("Plotting subplot to analyze distribution of 'size' variable")
    plt.subplots(figsize=(15,8))
    data['size'].hist(bins=50)
    plt.xticks(list(range(0,110,5)))
    plt.title('Size Distribution')
    plt.show()


    logging.info("Plotting Correlation and heat map")
    correlation = data.corr()
    sns.set_context("notebook", font_scale = 1.0, rc = {"lines.linewidth" : 2.5})
    plt.figure(figsize=(13, 7))
    a = sns.heatmap(correlation,annot = True, fmt = '.2f')

    rotx = a.set_xticklabels(a.get_xticklabels(), rotation=90)
    roty = a.set_yticklabels(a.get_yticklabels(), rotation=30)



    logging.info("Creating a histogram")
    data.hist()


    logging.info("Plotting density plot for browser")
    sns.distplot(data["browser"])

    logging.info("Plotting density plot for size")
    sns.distplot(data["size"])





    logging.info("Plotting density plot for find")
    sns.distplot(data["find"])


    


    logging.info("Plotting density plot for accession")
    sns.distplot(data["accession"])


    


    logging.info("Plotting density plot for crawler")
    sns.distplot(data["crawler"])


    


    logging.info("Plotting Pie chart for browser for percentage distribution")
    data['browser'].value_counts().plot.pie(figsize=(6, 6), autopct = '%.2f')
    plt.title("Browser pie diagram")
    plt.ylabel('Number of Browser')
    plt.xlabel('Browser Type');
    plt.show()


    


    logging.info("Plotting Pie chart for noagent for percentage distribution")
    data['size'].value_counts().plot.pie(figsize=(6, 6), autopct = '%.2f')
    plt.title("noagent pie diagram")
    plt.ylabel('Number of noagent')
    plt.xlabel('noagent Type');
    plt.show()


    logging.info( data['norefer'].value_counts().plot.pie(figsize=(6, 6), autopct = '%.2f'))
    logging.info( plt.title("norefer pie diagram"))
    logging.info( plt.ylabel('Number of norefer'))
    logging.info( plt.xlabel('norefer Type'))
    logging.info( plt.show())

    logging.info("Summary Metrics")

    


    logging.info("From tha above plots we concluded that amoung all the variables only few of them are required for analysis ")


    


    logging.info("Taking those variables into consideration")


    


    logging.info("Defining new object for considering few variables of data")
    data_new=data[['extention','norefer','noagent','idx','find','browser']]


    


    logging.info("Computing head values of the new data")
    data_new.head(15)


    


    logging.info("Now analyzing considering these reuired variables")


    


    logging.info("Plotting boxplot to evaluate relationship between variables browser and find")
    sns.boxplot(x="browser", y="find", data=data_new)


    


    logging.info("Plotting boxplot to evaluate relationship between variables browser and norefer")
    sns.boxplot(x="browser", y="norefer", data=data_new)


    


    logging.info("Plotting boxplot to evaluate relationship between variables browser and noagent")
    sns.boxplot(x="browser", y="noagent", data=data_new)


    


    logging.info("Plotting boxplot to evaluate relationship between variables browser and extension")
    sns.boxplot(x="browser", y="extention", data=data_new)
                 
    logging.info( In[ ]:


    logging.info( Summarizing data)

    date = data['date'].max()
    
                 
    date logging.info( Computing date of the data)



    tot_record = len(data)

    tot_recordlogging.info( computing total number of records)

    max_c=data['cik'].value_counts() 

    max_cik= max_c.max()

    max_ciklogging.info( Max count value of cik

    max_size = data['size'].max()logging.info( Computing maximum size)

    max_size

    sum_size = data['size'].sum()

    length_size = len(data)

    avg_size= sum_size/length_sizelogging.info( computing average of size)

    avg_size

    max_ext = data['extention'].value_counts()

    extention_max = data.extention[max_ext.max()]

    extention_max logging.info(Computing maximum extention used)

    max_brw = data['browser'].value_counts()

    max_brw.max()

    brw_max = data.browser[max_brw.max()]

    brw_max logging.info( Computing most occur browser)

    row_entry = pd.Series([date, tot_record, max_cik, max_size, avg_size, extention_max, brw_max])

    row_entry

    logging.info( Creating Summary metrics)
    summary_metrics = pd.DataFrame(columns=['Date','Total Records','Most Cik',
                                             'Maximum File Size','Average File size','Most used extention','Most used browser'])

    summary_metrics

    import csv

    courses_list=[]

    summary_metrics = summary_metrics.append(
                    pd.Series([d
       ate, tot_record, max_cik, max_size, avg_size, extention_max, brw_max],
                                           index=['Date','Total Records','Most Cik',
                                               'Maximum File Size','Average File size','Most used extention','Most used browser'])
                        ,ignore_index=True)

    summary_metrics
    

    
    
if __name__ == '__main__':
    main()

