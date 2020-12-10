import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

data=pd.read_csv('application_train.csv')
for column in data.columns:
    data[column].fillna(data[column].mode()[0], inplace=True)
print("Shape of Training Data : ",data.shape)
#Dropping the redundant features
remove_class=['SK_ID_CURR', 'FLAG_OWN_CAR', 'FLAG_MOBIL', 'FLAG_CONT_MOBILE', 'FLAG_DOCUMENT_2', 'FLAG_DOCUMENT_4', 'FLAG_DOCUMENT_7', 'FLAG_DOCUMENT_10', 'FLAG_DOCUMENT_12', 'FLAG_DOCUMENT_17', 'FLAG_DOCUMENT_19', 'FLAG_DOCUMENT_21','NONLIVINGAREA_MODE', 'ELEVATORS_AVG', 'FLOORSMIN_MODE', 'AMT_ANNUITY', 'LANDAREA_MODE', 'FLOORSMIN_MEDI', 'FLOORSMAX_MODE', 'LIVINGAREA_MODE', 'BASEMENTAREA_MODE', 'ELEVATORS_MEDI', 'ENTRANCES_MEDI', 'FLOORSMAX_MEDI', 'OBS_60_CNT_SOCIAL_CIRCLE', 'NONLIVINGAREA_MEDI', 'NONLIVINGAPARTMENTS_MEDI', 'BASEMENTAREA_AVG', 'APARTMENTS_MODE', 'ELEVATORS_MODE', 'ENTRANCES_MODE', 'COMMONAREA_MODE', 'LIVINGAPARTMENTS_MEDI', 'DEF_60_CNT_SOCIAL_CIRCLE', 'NONLIVINGAREA_AVG', 'LIVE_CITY_NOT_WORK_CITY', 'AMT_GOODS_PRICE', 'LIVINGAREA_MEDI', 'YEARS_BEGINEXPLUATATION_MEDI', 'COMMONAREA_MEDI', 'YEARS_BEGINEXPLUATATION_MODE', 'LIVINGAPARTMENTS_MODE', 'REGION_RATING_CLIENT_W_CITY', 'NONLIVINGAPARTMENTS_MODE', 'YEARS_BUILD_MEDI', 'YEARS_BUILD_MODE', 'BASEMENTAREA_MEDI', 'LIVINGAPARTMENTS_AVG', 'LIVINGAREA_AVG', 'APARTMENTS_MEDI', 'TOTALAREA_MODE', 'LANDAREA_MEDI', 'CNT_FAM_MEMBERS', 'YEARS_BUILD_AVG']
data.keys()
data.drop(labels=remove_class, axis=1, inplace=True)
test = data.loc[[3]]
test.drop(['TARGET'],axis = 1,inplace = True)
print(test)



Y=data['TARGET']
data.drop('TARGET',axis = 1, inplace = True)
X=data



labelencoder_dict = {}
onehotencoder_dict = {}
for col in X:
    if X[col].dtype == 'object':
        # print(X[col])
        if len(list(data[col].unique())) <= 2:
          le = LabelEncoder()
          labelencoder_dict[col] = le
          le.fit(X[col])
          X[col] = le.transform(X[col])
print("Label Encoder ",X.shape)

for col in X:
  if X[col].dtype == 'object':
        # print(X[col])
      if len(list(data[col].unique())) > 2:
        onehot_encoder = OneHotEncoder()
        onehotencoder_dict[col] = onehot_encoder
        w = onehot_encoder.fit_transform(np.array(list(X[col])).reshape(-1,1)).toarray()
        dfOneHot = pd.DataFrame(w, columns = [col+str(int(i)) for i in range(w.shape[1])])
        X = pd.concat([X, dfOneHot], axis=1)
        X = X.drop(col, axis=1)
print("Label Encoder ",X.shape) 
# X2 = pd.get_dummies(X)
print("One hot encoder ",X.shape)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

print(onehotencoder_dict)
print(labelencoder_dict)

# test.to_csv('out.csv')
for i in test:
  if test[i].dtype == 'object':
        # print(X[col])
        if len(list(data[i].unique())) <= 2:
          lea = labelencoder_dict[i]
          lea.fit(test[i])
          test[i] = lea.transform(test[i])

print("Label Encoder ",test.shape)
print(test)

for k in onehotencoder_dict.keys():

          print(k)
          ohe = onehotencoder_dict[k]
          # print(np.array(list(data[i].unique())).reshape(-1,1))
          z = ohe.transform(np.array(list(test[k])).reshape(-1,1)).toarray()
          dfHot = pd.DataFrame(z, columns = [k + str(int(i)) for i in range(z.shape[1])])
          # if 'level_0' in test.columns:
          #   test.drop('level_0',axis = 1)
          test = test.reset_index(drop = True)
          test = pd.concat([test, dfHot], axis=1)
          test = test.drop(k,axis = 1)
          # test3 = pd.concat([test3,dfHot], axis=1)
          # test3 = test3.reset_index()


print(test)
# for k in test:
#     if len(list(data[k].unique())) > 2:
#       test = test.drop(k,axis = 1)

# onehotencoder = onehotencoder_dict['NAME_TYPE_SUITE']
# X = onehotencoder.transform(np.array(list(data['NAME_TYPE_SUITE'])).reshape(-1,1)).toarray()
# dfOneHot = pd.DataFrame(X, columns = ["NAME_TYPE_SUITE_"+str(int(i)) for i in range(X.shape[1])]) 
# df = pd.concat([data, dfOneHot], axis=1)
# df= df.drop(['NAME_TYPE_SUITE'], axis=1)
# print(df)acis
# print("Test ",test2)
test.to_csv('out.csv')  

# onehotencoder = OneHotEncoder()
# X = onehotencoder.fit_transform(np.array(list(data['NAME_TYPE_SUITE'])).reshape(-1,1)).toarray()
# dfOneHot = pd.DataFrame(X, columns = ["NAME_TYPE_SUITE_"+str(int(i)) for i in range(X.shape[1])]) 
# df = pd.concat([data, dfOneHot], axis=1)
# df= df.drop(['NAME_TYPE_SUITE'], axis=1)
#   if test[i].dtype == 'object':
    
#     if len(list(X[i].unique())) <= 2:
#       le=  labelencoder_dict[i]
#       test[i] = le.transform(test[i])
# test = pd.get_dummies(test)
# print(test.shape)






# labelencoder_dict = {}
# onehotencoder_dict = {}
# X_train = None
# for i in range(0, X.shape[1]):
#     label_encoder = LabelEncoder()
#     labelencoder_dict[i] = label_encoder
#     feature = label_encoder.fit_transform(X[:,i])
#     feature = feature.reshape(X.shape[0], 1)
#     onehot_encoder = OneHotEncoder(sparse=False)
#     feature = onehot_encoder.fit_transform(feature)
#     onehotencoder_dict[i] = onehot_encoder
#     if X_train is None:
#       X_train = feature
#     else:
#       X_train = np.concatenate((X_train, feature), axis=1)

# def getEncoded(test_data,labelencoder_dict,onehotencoder_dict):
#     test_encoded_x = None
#     for i in range(0,test_data.shape[1]):
#         label_encoder =  labelencoder_dict[i]
#         feature = label_encoder.transform(test_data[:,i])
#         feature = feature.reshape(test_data.shape[0], 1)
#         onehot_encoder = onehotencoder_dict[i]
#         feature = onehot_encoder.transform(feature)
#         if test_encoded_x is None:
#           test_encoded_x = feature
#         else:
#           test_encoded_x = np.concatenate((test_encoded_x, feature), axis=1)
#     return test_encoded_x

# t2 = getEncoded(test,labelencoder_dict,onehotencoder_dict)
# print(t2.shape)
from sklearn import tree
decisiontree_model = tree.DecisionTreeClassifier(min_samples_split=10,min_samples_leaf=5,random_state=42)
decisiontree_model.fit(X_train,y_train)


pickle.dump(decisiontree_model, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict(test)) 