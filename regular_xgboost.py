#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import GradientBoostingClassifier


# In[4]:


train_data = pd.read_csv(r"C:\Users\ankus\OneDrive\Desktop\regular\train.csv")
test_data = pd.read_csv(r"C:\Users\ankus\OneDrive\Desktop\regular\test.csv")


# In[5]:


y_train = train_data["Survived"]
train_data.drop(labels="Survived", axis=1, inplace=True)


# In[6]:


full_data = train_data.append(test_data)


# In[7]:


drop_columns = ["Name", "Age", "SibSp", "Ticket", "Cabin", "Parch", "Embarked"]
full_data.drop(labels=drop_columns, axis=1, inplace=True)


# In[8]:


full_data = pd.get_dummies(full_data, columns=["Sex"])
full_data.fillna(value=0.0, inplace=True)


# In[9]:


X_train = full_data.values[0:891]
X_test = full_data.values[891:]


# In[11]:


scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#Now we can split the data into training and te


# In[12]:


state = 12  
test_size = 0.30  
  
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train,  
    test_size=test_size, random_state=state)


# In[13]:


lr_list = [0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1]

for learning_rate in lr_list:
    gb_clf = GradientBoostingClassifier(n_estimators=20, learning_rate=learning_rate, max_features=2, max_depth=2, random_state=0)
    gb_clf.fit(X_train, y_train)

    print("Learning rate: ", learning_rate)
    print("Accuracy score (training): {0:.3f}".format(gb_clf.score(X_train, y_train)))
    print("Accuracy score (validation): {0:.3f}".format(gb_clf.score(X_val, y_val)))


# In[14]:


gb_clf2 = GradientBoostingClassifier(n_estimators=20, learning_rate=0.5, max_features=2, max_depth=2, random_state=0)
gb_clf2.fit(X_train, y_train)
predictions = gb_clf2.predict(X_val)

print("Confusion Matrix:")
print(confusion_matrix(y_val, predictions))

print("Classification Report")
print(classification_report(y_val, predictions))


# In[15]:


from xgboost import XGBClassifier


# In[16]:


xgb_clf = XGBClassifier()
xgb_clf.fit(X_train, y_train)


# In[17]:


score = xgb_clf.score(X_val, y_val)
print(score)


# In[ ]:




