classes=['A','B','C','D','E','F','G','H','I','J']
drivers =[]
#regrouping each driver trip data from 4 different trips in separate data frame
for c in classes:
    drivers.append(data[data['Class']==c])
    
dataa=[]
#reset of data index of each driver 
#assign 3 trips data for training, and the last trip data for validation
for c in range(len(drivers)):
    nt=0
    nv=0
    drivers[c]=drivers[c].reset_index(drop=True)
    idxs=drivers[c][drivers[c]['Time(s)']==1].index.values
    for i in range(len(idxs)):
      if i <(len(idxs)-1):
        nt=nt+1
        dataa.append(drivers[c][idxs[i]:idxs[i+1]])
      if i==(len(idxs)-1):
        nv=nv+1
        dataa.append(drivers[c][idxs[i]:])
    print("Driver : "+str(c)+" number of trips :"+str(len(idxs))+ "  For Train : "+str(nt)+"  For valid :"+str(nv))
    
#sliding window of 60s without overlapping 
drivers=[]
ss=0
for i in range(len(dataa)):
    #print(n)
    n=int(len(dataa[i])/60)
    #print(" Drive "+str(i)+" contains "+str(n)+" subdriversets")
    dd=0
    for j in range(n):
        #print(j)
        temp=dataa[i][dd:dd+60]
        temp=temp.reset_index(drop=True)
        drivers.append(temp)
        ss=ss+1
        dd=dd+60
print("total is "+str(ss))



columns2=["Long_Term_Fuel_Trim_Bank1","Intake_air_pressure","Accelerator_Pedal_value","Fuel_consumption","Torque_of_friction","Maximum_indicated_engine_torque","Engine_torque","Calculated_LOAD_value",
"Activation_of_Air_compressor","Engine_coolant_temperature","Transmission_oil_temperature","Wheel_velocity_front_left-hand","Wheel_velocity_front_right-hand","Wheel_velocity_rear_left-hand",
"Torque_converter_speed"]

samples = list()
labels=list()

for c in drivers:
    labels.append(c['Class'][0])
    del c['Class']
    del c['Time(s)']
    samples.append(c.values)
data = np.array(samples)
print(data.shape)



from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(labels)
labels=le.transform(labels) 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=100)
