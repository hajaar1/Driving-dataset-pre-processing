import pandas as pd
import numpy as np
from sklearn import preprocessing

pd.options.display.max_columns = 999
pd.options.display.max_rows = 50
data=[]
#appending the 10 files of 10 drivers in one dataframe
for i in range(1,11):
  data.append(pd.read_csv('dataset_web/participant_'+str(i)+'.csv',sep=';'))
for i in range(len(data)):
  data[i]["driver"]=i

columns=[
    'AccelX',
    'AccelY',
    'AccelZ',
    'Lightning',
    'Speed_GPS',
    'ECG',
    'SCR',
    'Temp',
    'HR',
    'HRV_LF'
]

#splitting training and validation data (90%-10%)
training_data=[]
validation_data=[]
for i in range(len(data)):
  c=round(data[i].shape[0]*90/100)
  training_data.append(data[i][0:c])
  validation_data.append(data[i][c:])
print(len(training_data))
print(len(validation_data))

#sliding window of 60s with overlapping of 10s
train=[]
ss=0
for i in range(len(training_data)):
    #print(n)
    n=int(len(training_data[i])/100)
    print(" driver "+str(i)+" contains "+str(n)+" subdriversets")
    dd=0
    for j in range(n):
        #print(j)
        temp=training_data[i][dd:dd+600]
        temp=temp.reset_index(drop=True)
        train.append(temp)
        ss=ss+1
        dd=dd+100
print("total is "+str(ss))


valid=[]
ss=0
for i in range(len(validation_data)):
    #print(n)
    n=int(len(validation_data[i])/600)
    print(" driver "+str(i)+" contains "+str(n)+" subdriversets")
    dd=0
    for j in range(n):
        #print(j)
        temp=validation_data[i][dd:dd+600]
        temp=temp.reset_index(drop=True)
        valid.append(temp)
        ss=ss+1
        dd=dd+600
print("total is "+str(ss))

print("train : "+str(len(train)))
print("valid : "+str(len(valid)))

#Normalisation and scaling
#shaping training and validation data into arrays
train_samples = list()
train_labels=list()
n=0
for i in range(len(train)):
  try:
    temp=train[i][columns]
    temp=preprocessing.normalize(temp)
    temp=preprocessing.scale(temp)
    if(temp.shape[0]==600):
      train_samples.append(temp)
      train_labels.append(train[i]['driver'][0])
  except :
    print("error in file ",str(n))
  n=n+1
train_data = np.array(train_samples)
print(train_data.shape)


valid_samples = list()
valid_labels=list()
n=0
for i in range(len(valid)):
  try:
    temp=valid[i][columns]
    temp=preprocessing.normalize(temp)
    temp=preprocessing.scale(temp)
    if(temp.shape[0]==600):
      valid_samples.append(temp)
      valid_labels.append(valid[i]['driver'][0])
  except :
    print("error in file ",str(n))
  n=n+1
valid_data = np.array(valid_samples)
print(valid_data.shape)


le = preprocessing.LabelEncoder()
le.fit(train_labels)
train_labels=le.transform(train_labels)
valid_labels=le.transform(valid_labels)
