import pandas as pd
import tensorflow as tf
tf.set_random_seed(777)
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Activation
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint
import numpy as np

##########데이터 로드

train_df = pd.read_excel('http://june3471.pythonanywhere.com/media/%EC%95%84%EB%B2%84%EC%A7%80%EC%95%84%EB%93%A4%ED%82%A4.xlsx', sheet_name='train')
test_df = pd.read_excel('http://june3471.pythonanywhere.com/media/%EC%95%84%EB%B2%84%EC%A7%80%EC%95%84%EB%93%A4%ED%82%A4.xlsx', sheet_name='test')

##########데이터 분석

##########데이터 전처리

x_train_df = train_df.drop(['Son'], axis=1)
x_test_df = test_df.drop(['Son'], axis=1)
y_train_df = train_df[['Son']]
y_test_df = test_df[['Son']]

print(x_train_df.head())
'''
    Father
0  160.782
1  166.116
2  165.608
3  169.672
4  176.530
'''

x_train = x_train_df.values
x_test = x_test_df.values
y_train = y_train_df.values
y_test = y_test_df.values

print(x_train.shape)
print(y_train.shape)

##########모델 학습
##########모델 검증

input = Input(shape=(1,))

net = Dense(units=512)(input)
net = Activation('relu')(net)
net = Dense(units=512)(net)
net = Activation('relu')(net)
net = Dense(units=1)(net)
model = Model(inputs=input, outputs=net)

model.compile(loss='mean_squared_error', optimizer=Adam(lr=0.01))

model.fit(x_train, y_train, epochs=50, validation_data=(x_test, y_test), callbacks=[ModelCheckpoint(filepath='model/son_height_regression_model.h5', save_best_only=True, verbose=1)]) 

##########모델 예측

y_predict = model.predict(np.array([[162.789]]))
print(y_predict) #[[8.182088]]
print(y_predict.flatten()) #[8.182088]
print(y_predict.flatten()[0]) #8.182088