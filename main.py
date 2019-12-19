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
        'DstHostDiffSrvRate',
        'Result'
        ]
end=18
result=18
# Import training dataset
training_dataset = pd.read_csv('training.csv', names=COLUMN_NAMES, header=0)
train_x = training_dataset.iloc[:, 0:end].values
train_y = training_dataset.iloc[:, result].values


# Encoding training dataset
encoding_train_y = np_utils.to_categorical(train_y)
#encoding_train_y =train_y

# Import testing dataset
test_dataset = pd.read_csv('testing.csv', names=COLUMN_NAMES, header=0)
test_x = test_dataset.iloc[:, 0:end].values
test_y = test_dataset.iloc[:, result].values

# Encoding training dataset
encoding_test_y = np_utils.to_categorical(test_y)
#encoding_test_y = test_y

# Creating a model
model = Sequential()
model.add(Dense(10, input_dim=18, activation='sigmoid'))
model.add(Dense(10, activation='sigmoid', use_bias=True))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(2, activation='softmax'))

# Compiling model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training a model
model.fit(train_x, encoding_train_y, epochs=300, batch_size=10)

# evaluate the model
scores = model.evaluate(test_x, encoding_test_y)
print("\nAccuracy: %.2f%%" % (scores[1]*100))

for i in range(0, 10):
    predict_dataset = pd.read_csv('predict.csv', names=COLUMN_NAMES, header=0)
    predict_x = predict_dataset.iloc[i:i+1, 0:end].values
    y = predict_dataset.iloc[i, result]
    predict_value = model.predict_classes(predict_x)
    print(predict_value[0], y)



#plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True, expand_nested=True)
