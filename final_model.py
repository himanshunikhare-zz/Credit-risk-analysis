import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv('application_train.csv')
for column in data.columns:
    data[column].fillna(data[column].mode()[0], inplace=True)
print("Shape of Training Data : ",data.shape)
#Dropping the redundant features
remove_class=['SK_ID_CURR', 'FLAG_OWN_CAR', 'FLAG_MOBIL', 'FLAG_CONT_MOBILE', 'FLAG_DOCUMENT_2', 'FLAG_DOCUMENT_4', 'FLAG_DOCUMENT_7', 'FLAG_DOCUMENT_10', 'FLAG_DOCUMENT_12', 'FLAG_DOCUMENT_17', 'FLAG_DOCUMENT_19', 'FLAG_DOCUMENT_21','NONLIVINGAREA_MODE', 'ELEVATORS_AVG', 'FLOORSMIN_MODE', 'AMT_ANNUITY', 'LANDAREA_MODE', 'FLOORSMIN_MEDI', 'FLOORSMAX_MODE', 'LIVINGAREA_MODE', 'BASEMENTAREA_MODE', 'ELEVATORS_MEDI', 'ENTRANCES_MEDI', 'FLOORSMAX_MEDI', 'OBS_60_CNT_SOCIAL_CIRCLE', 'NONLIVINGAREA_MEDI', 'NONLIVINGAPARTMENTS_MEDI', 'BASEMENTAREA_AVG', 'APARTMENTS_MODE', 'ELEVATORS_MODE', 'ENTRANCES_MODE', 'COMMONAREA_MODE', 'LIVINGAPARTMENTS_MEDI', 'DEF_60_CNT_SOCIAL_CIRCLE', 'NONLIVINGAREA_AVG', 'LIVE_CITY_NOT_WORK_CITY', 'AMT_GOODS_PRICE', 'LIVINGAREA_MEDI', 'YEARS_BEGINEXPLUATATION_MEDI', 'COMMONAREA_MEDI', 'YEARS_BEGINEXPLUATATION_MODE', 'LIVINGAPARTMENTS_MODE', 'REGION_RATING_CLIENT_W_CITY', 'NONLIVINGAPARTMENTS_MODE', 'YEARS_BUILD_MEDI', 'YEARS_BUILD_MODE', 'BASEMENTAREA_MEDI', 'LIVINGAPARTMENTS_AVG', 'LIVINGAREA_AVG', 'APARTMENTS_MEDI', 'TOTALAREA_MODE', 'LANDAREA_MEDI', 'CNT_FAM_MEMBERS', 'YEARS_BUILD_AVG']
data.keys()
data.drop(labels=remove_class, axis=1, inplace=True)

le = LabelEncoder()

for col in data:
    if data[col].dtype == 'object':
        if len(list(data[col].unique())) <= 2:
            le.fit(data[col])
            data[col] = le.transform(data[col])
print("Label Encoder ",data.shape)
data = pd.get_dummies(data)
print("One hot encoder ",data.shape)

Y=data.iloc[:,0]
X=data.iloc[:,2:]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

from sklearn import tree
decisiontree_model = tree.DecisionTreeClassifier(min_samples_split=10,min_samples_leaf=5,random_state=42)
decisiontree_model.fit(X_train,y_train)


pickle.dump(decisiontree_model, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))