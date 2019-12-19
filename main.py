# Importing libraries
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from keras.utils import plot_model

import numpy
import pandas as pd

# fix random seed for reproducibility
numpy.random.seed(7)

# Defining column names for datasets

COLUMN_NAMES = [
        'Duration', 
        'Protocol',
        'Service', 
        'Flag', 
        'SrcBytes',
        'DstBytes',
        'Land',
        'WrongFragment',
        'Urgent',
        'Hot',
        'NumFailedLogins',
        'LoggedIn',
        'Count',
        'SrvCount',
        'DstHostCount',
        'DstHostSrcCount',
        'DstHostSameSrvRate',
        'DstHostDiffSrvRate'
        ]

# Import training dataset
training_dataset = pd.read_csv('training.csv', names=COLUMN_NAMES, header=0)
train_x = training_dataset.iloc[:, 0:17].values
train_y = training_dataset.iloc[:, 17].values


# Encoding training dataset
encoding_train_y = np_utils.to_categorical(train_y)

# Import testing dataset
test_dataset = pd.read_csv('testing.csv', names=COLUMN_NAMES, header=0)
test_x = test_dataset.iloc[:, 0:17].values
test_y = test_dataset.iloc[:, 17].values

# Encoding training dataset
encoding_test_y = np_utils.to_categorical(test_y)

# Creating a model
model = Sequential()
model.add(Dense(10, input_dim=17, activation='relu'))
model.add(Dense(9, activation='relu', use_bias=True))
model.add(Dense(8, activation='sigmoid', use_bias=True))
model.add(Dense(2, activation='softmax'))

# Compiling model
#model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training a model
model.fit(train_x, encoding_train_y, epochs=300, batch_size=10)

# evaluate the model
scores = model.evaluate(test_x, encoding_test_y)
print("\nAccuracy: %.2f%%" % (scores[1]*100))


# Import testing dataset
second_dataset = pd.read_csv('compare.csv', names=COLUMN_NAMES, header=0)
second_x = second_dataset.iloc[:, 0:17].values
second_y = second_dataset.iloc[:, 17].values

# Encoding training dataset
encoding_second_y = np_utils.to_categorical(second_y)

# evaluate the model by second choose
second_scores = model.evaluate(second_x, encoding_second_y)
print("\nAccuracy2: %.2f%%" % (second_scores[1]*100))

predict_dataset = pd.read_csv('predict.csv', names=COLUMN_NAMES, header=0)
predict_x = predict_dataset.iloc[0:1, 0:17].values
y = predict_dataset.iloc[0:1, 17].values
predict_value = model.predict_classes(predict_x)
print(predict_value, y)

predict_x = predict_dataset.iloc[1:2, 0:17].values
y = predict_dataset.iloc[1:2, 17].values
predict_value = model.predict_classes(predict_x)
print(predict_value, y)

predict_x = predict_dataset.iloc[2:3, 0:17].values
y = predict_dataset.iloc[2:3, 17].values
predict_value = model.predict_classes(predict_x)
print(predict_value, y)


predict_x = predict_dataset.iloc[3:4, 0:17].values
y = predict_dataset.iloc[3:4, 17].values
predict_value = model.predict_classes(predict_x)
print(predict_value, y)


predict_x = predict_dataset.iloc[4:5, 0:17].values
y = predict_dataset.iloc[4:5, 17].values
predict_value = model.predict_classes(predict_x)
print(predict_value, y)

predict_x = predict_dataset.iloc[5:6, 0:17].values
y = predict_dataset.iloc[5:6, 17].values
predict_value = model.predict_classes(predict_x)
print(predict_value, y)


plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True, expand_nested=True)
