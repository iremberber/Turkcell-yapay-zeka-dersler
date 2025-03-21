import numpy as np
import pandas as pd

#Random veri oluşturmak
numberOfSamples = 1000 #1000 adet veri

np.random.seed(42) # farklı data üretmesi için

age = np.random.randint(1,10,numberOfSamples)
kilometer = np.random.randint(10,100000,numberOfSamples) #100 bin demek istedik aslında
engine_size = np.random.randint(1000,2000,numberOfSamples)

noise = np.random.randint(-5000, 5000, size=numberOfSamples) #gerçek değerlere yakın olması için gürültü ekledik max min  olacak şekilde

price =  abs((engine_size * 100) - (kilometer * 2) - (age * 5000) + 100000 + noise)

df =  pd.DataFrame({
    "Age": age,
    "Kilometer": kilometer,
    "Engine_size": engine_size,
    "Price": price
}) #verileri df e atadık

print(df.head(10))

#Veriyi bağımlı bağımsız değişken olarak tanımladık
X=df[["Age","Kilometer","Engine_size"]]
y=df[["Price"]]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train,y_train)

selling_car=model.predict([[4,70000,1600]])
print(selling_car) #tahmin price ımız budur sorudaki tahmin değer

print(df.iloc[435])

selling_car=model.predict([[2,36519,1563]])
print(selling_car) #tahmin price ımızla gerçek değer ne kadar yakın onu kontrol ediyoruz

from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test) #test değeri ile y nin predi arasındaki kontrol yapıyor

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("r²:", r2)
print("mse:", mse)

import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel("Gerçek Fiyat")
plt.ylabel("Tahmin Edilen Fiyat")
plt.title("Gerçek Fiyat ile Tahmin Edilen Fiyat Arasındaki Bağlantı")
plt.show()