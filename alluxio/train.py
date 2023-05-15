#!/usr/bin/env python
# -*- coding: utf-8 -*-

import alluxio
from alluxio import client
from alluxio import option

filepath = "/Data/test.json"
server = "10.10.0.80"
#port=19998
port=39999


client = alluxio.Client(server,port)
if client.exists(filepath):
    print('File exists')
else:
    print('File does not exist')

with client.open(filepath, 'r') as f:
    data = f.read()
    print(data)


    '''
    while True:
        data = f.read(1024) 
        if not data:
            break

        print(data.decode('utf-8'))
        break
    '''

'''
import alluxio
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler

# Connect to Alluxio and read the CSV file
client = alluxio.Client()
with client.open('/path/to/csv') as f:
    df = pd.read_csv(f)

# Scale the data
scaler = MinMaxScaler()
data = scaler.fit_transform(df.values)

# Split the data into input (X) and output (y) variables
X, y = data[:, :-1], data[:, -1]

# Reshape input data to be 3-dimensional [samples, timesteps, features]
X = X.reshape((X.shape[0], 1, X.shape[1]))

# Define and compile the LSTM model
model = Sequential()
model.add(LSTM(50, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')

# Fit the model on the training data
model.fit(X, y, epochs=50, batch_size=72, verbose=2)
'''
