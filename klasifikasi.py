from sklearn.ensemble import RandomForestRegressor 
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix 

from sklearn.model_selection import GridSearchCV

import pandas as pd 
import numpy as np 

import pickle

import matplotlib.pyplot as plt
import itertools



#ambil data dari csv
data = pd.read_csv('afterOversampling.csv') 

#manipulasi data untuk dicoba kan (Test)
dataCoba = data.drop(["Unnamed: 0"], axis=1)
dataCoba = dataCoba.drop(["Class"], axis=1)
dataCoba = dataCoba.drop(["Pixel"], axis=1)
dataCoba = dataCoba.drop(["Berat"], axis=1)
dataCoba = dataCoba.drop(["Lebar"], axis=1)
dataCoba1 = data["Class"]

#Untuk prediksi berat (Regresi)
dataBerat = data[['Pixel', 'Lebar']]
dataBerat1 = data["Berat"]

print(dataCoba)
print(dataBerat)

#Tuning Parameter
# parameters = {'activation':('identity', 'logistic', 'tanh', 'relu'), 'hidden_layer_sizes':[0, 100]}
# clf = GridSearchCV(MLPClassifier())
# print(clf)

#Pembuatan Model
modelMatang = MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto', beta_1=0.9, beta_2=0.999, early_stopping=False, epsilon=1e-08, hidden_layer_sizes=(30, 20), learning_rate='constant', learning_rate_init=0.001, max_iter=1000000, momentum=0.9, nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True, solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False, warm_start=False)
modelMatang.fit(dataCoba, dataCoba1)
akurasi = modelMatang.score(dataCoba, dataCoba1)*100

modelBerat = RandomForestRegressor() 
modelBerat.fit(dataBerat,dataBerat1)
akurasi1 = modelBerat.score(dataBerat, dataBerat1, sample_weight=None)*100



#Prediksi
matangPredict = modelMatang.predict(dataCoba)
beratPredict = modelBerat.predict(dataBerat)

print(matangPredict)
print(beratPredict)

cnf_matrix = confusion_matrix(dataCoba1, matangPredict)
print(cnf_matrix) 


print('Akurasi Prediksi Kematangan: %.2f%%' %(akurasi))
print('Akurasi Prediksi Berat: %.2f%%' %(akurasi1))

#Simpan Model
filename = 'kematangan1.sav' 
pickle.dump(modelMatang, open(filename, 'wb')) 

filename = 'berat1.sav' 
pickle.dump(modelBerat, open(filename, 'wb')) 

classes = ['Tidak Matang', 'Setengah Matang', 'Matang']

# Plot non-normalized confusion matrix
plt.figure()
plt.imshow(cnf_matrix, interpolation='nearest')
plt.colorbar()
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes, rotation=45)
plt.yticks(tick_marks, classes)

cm = modelMatang

plt.tight_layout()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()
