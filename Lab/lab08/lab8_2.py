from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D, BatchNormalization
import time
import datetime
import ssl
ssl.create_default_context = ssl._create_unverified_context
start_time = time.time()

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

y_train = y_train ==2
y_test = y_test == 2

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3), activation='relu'))
model.add(Conv2D(32, (3, 3), activatiopn='relu'))
model.add(MaxPool2D(poll_size=(2, 2)))
model.add(BatchNormalization())
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same', input_shape=(32, 32, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activatiopn='relu'))
model.add(MaxPool2D(poll_size=(2, 2)))
model.add(BatchNormalization())
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=32, epochs=10, validation_data=(X_test, y_test), shuffle=True)
model.save('otputs/bird_classifier_model_5epochs.h5')
print(f'Done in {datetime.timedelta(seconds=time.time() - start_time)}')