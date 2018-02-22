
###################Decision tree################
import pandas as pd 
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

input='melb_data.csv' 
df=pd.read_csv(input)
#print (df.describe())
df=df.dropna(axis=0)#clean the missingdata 
column=df.columns
#############start the prediction: choose target and predictors
y=df.Price# d
predictor=['Bathroom', 'Landsize', 'BuildingArea','YearBuilt', 'Lattitude', 'Longtitude','Rooms']#define the predictors or features
X=df[predictor]
Prediction1=DecisionTreeRegressor()# define the model
Prediction2=RandomForestRegressor()

#Prediction1.fit(X,y)#fit the model
#Prediction2.fit(X,y)#fit the model

#PP=Prediction1.predict(X)#make the prediction
#PPP=Prediction2.predict(X)
#print ('Potential price is : ',PP)
###############Model validation: mean absolute error
#Validation=mean_absolute_error(y,PP)
#print (Validation)

###############Model validation/accuracy:cross validation
#split the data into training and testing set
from sklearn.model_selection import train_test_split
trainX,testX,trainy,testy=train_test_split(X,y,random_state=0)
Prediction1.fit(trainX,trainy)#fit the model with the training dataset
Prediction2.fit(trainX,trainy)
pp=Prediction1.predict(testX)#make the prediction on the testing set
ppp=Prediction2.predict(testX)

print ('decision tree prediction: ',pp)

print (mean_absolute_error(testy,pp))
print
print
print ('random forest prediction: ',ppp)

print (mean_absolute_error(testy,ppp))
print (column)
#########################################################
