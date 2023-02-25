from keras.layers import InputLayer
from keras.layers import Dense
from keras.models import Sequential
from keras.losses import MSE
from keras.optimizers import SGD


model= Sequential()
model.add(InputLayer(input_shape=(2,)))
model.add(Dense(5, activation='relu'))
model.add(Dense(3, activation='relu'))
model.add(Dense(2, activation='relu'))
model.add(Dense(2, activation='sigmoid'))

opt= SGD(learning_rate=0.000001)
model.compile(loss=MSE, optimizer=opt)
