from sklearn.ensemble import RandomForestClassifier 
from sklearn.ensemble import RandomForestRegressor 
from sklearn.neural_network import MLPClassifier

import pandas as pd 
import numpy as np 

import pickle 

from sklearn.metrics import confusion_matrix 

#import dataset 
dataKematangan = pd.read_csv('tomat.csv') 
    # dataBerat = pd.read_csv('tomatBerat.csv') 
dataCoba = dataKematangan.drop(["Class"], axis=1)
dataCoba = dataCoba.drop(["Pixel"], axis=1)
dataCoba = dataCoba.drop(["Berat"], axis=1)
dataCoba = dataCoba.drop(["Lebar"], axis=1)
dataCoba1 = dataKematangan["Class"]
dataBerat = dataKematangan[['Pixel', 'Lebar']]
dataBerat1 = dataKematangan["Berat"]

# dataBerat = dataBerat.values.reshape(-1,1)

#split data test dan data train 
trainKematangan=dataKematangan.sample(frac=0.8,random_state=200) 
testKematangan= dataKematangan.sample(frac=0.2,random_state=200) 

# trainBerat=dataBerat.sample(frac=0.8,random_state=200) 
    # testBerat= dataBerat.sample(frac=0.2,random_state=200) 

#mengambil class dari dataset 
kematanganTrain = trainKematangan["Class"] 
    # beratTrain = trainBerat["berat"] 


#memisahkan class dari dataset 
trainKematangan = trainKematangan.drop(["Class"], axis=1) 
trainKematangan = trainKematangan.drop(["Pixel"], axis=1) 
trainKematangan = trainKematangan.drop(["Berat"], axis=1) 
trainKematangan = trainKematangan.drop(["Lebar"], axis=1) 
    # trainBerat = trainBerat.drop(["berat"], axis=1) 


#membuat model menggunakan random forest 
modelKematangan = MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto', beta_1=0.9, beta_2=0.999, early_stopping=False, epsilon=1e-08, hidden_layer_sizes=(30, 20 ), learning_rate='constant', learning_rate_init=0.001, max_iter=1000000, momentum=0.9, nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True, solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False, warm_start=False)
modelKematangan.fit(trainKematangan, kematanganTrain)

modelBerat = RandomForestRegressor() 
modelBerat.fit(dataBerat,dataBerat1) 


###### data test 
kematanganTestAsli = testKematangan["Class"] 
testKematangan=testKematangan.drop(["Class"], axis=1) 
testKematangan=testKematangan.drop(["Pixel"], axis=1)
testKematangan=testKematangan.drop(["Berat"], axis=1)
testKematangan=testKematangan.drop(["Lebar"], axis=1)

    # beratTestAsli = testBerat["berat"] 
    # testBerat=testBerat.drop(["berat"], axis=1) 

####prediksi data test menggunakan model random forest 
kematanganPredict = modelKematangan.predict(dataCoba) #nnti ini test : inputan baru 
beratPredict = modelBerat.predict(dataBerat) 
print(kematanganPredict)
print(beratPredict)
    # print(testBerat) 

####confusion matrix 
print(confusion_matrix(dataCoba1, kematanganPredict)) 




# save the model to disk 
filename = 'modelTomatKematangan.sav' 
pickle.dump(modelKematangan, open(filename, 'wb')) 

filename = 'modelTomatBerat.sav' 
pickle.dump(modelBerat, open(filename, 'wb')) 





# load the model from disk 
    # loaded_model = pickle.load(open(filename, 'rb')) 
    # beratPredict = loaded_model.predict(testBerat) #nnti ini test : inputan baru 
    # print(beratPredict)
