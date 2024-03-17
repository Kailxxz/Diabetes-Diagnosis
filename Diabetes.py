#Importing the required modules and libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
import warnings
import pickle
warnings.filterwarnings('ignore')

#Dataframe
df = pd.read_csv(r"C:\\Users\\91638\\Desktop\\Data Analytics\\Projects\\Diabetes Prediction\\diabetes.csv")

features=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']
X=pd.get_dummies(df[features])
y=df.Outcome

#Scaling the datas using standar scaler 
scaler = StandardScaler()
standardized_data = scaler.fit_transform(X)
X=standardized_data

#splitting the datas for training and testing
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=1/11,random_state=242)

#Model
lda = LinearDiscriminantAnalysis()
lda.fit(x_train,y_train)
X_train_prediction = lda.predict(x_test)

#Linking with streamlit for web application
pickle.dump(lda,open('model.pkl','wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))