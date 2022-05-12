import tensorflow as tf
import os
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, BatchNormalization, Dropout,RandomFlip, RandomRotation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import TensorBoard, EarlyStopping, ModelCheckpoint
import pandas as pd
import shutil
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix



def conv_block(cnn,filters, depth=2,batchnorm =False, dropout=0.0):
    for i in range(depth):
        cnn.add(Conv2D(filters,(3,3),
                         padding='Same',
                         activation='relu',
                         kernel_initializer = 'he_uniform'))
        if batchnorm:
            cnn.add(BatchNormalization())
    cnn.add(MaxPooling2D((2,2)))
    if dropout >0:
        cnn.add(Dropout(dropout))
    return cnn

def load_data(fp,batch_size=32):
    training=keras.utils.image_dataset_from_directory(fp,
                                              batch_size=batch_size,
                                             validation_split =0.2,
                                             subset ='training',
                                             seed=42,
                                             image_size=(256,256),)
    val = keras.utils.image_dataset_from_directory(fp,
                                              batch_size=batch_size,
                                             validation_split =0.2,
                                             subset ='validation',
                                             seed=42,
                                             image_size=(256,256),)
    return training, val


def plot_confusion_matrix(predictions,labels,p=0.5):
  cm=confusion_matrix(labels, predictions>p)
  sns.heatmap(cm,annot=True,fmt ='d',xticklabels=['People','Weapon'],yticklabels=['People','Weapon'])
  plt.title(f'p>{p}')
  plt.ylabel('Actual Label')
  plt.xlabel('Predicted Label')

def get_predictions(model,data):
  """Expects a TF Dataset"""
  predicted=[]
  labels=[]
  for x, y in data:
    predicted.append(model.predict(x))
    labels.append(y)

  
  return np.concatenate(predicted), np.concatenate(labels)
