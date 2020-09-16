#!/usr/bin/env python
# coding: utf-8

# Initial imports

# In[1]:


from keras.models import Sequential
from keras.layers import Dense
import numpy as np


# Creating the model

# In[2]:


# Creates model
model = Sequential()


# -----------------------------------------------------------------------------

# Initial steps

# In[3]:


print('We currently only provide services for dense layers.')
print('Please provide number of hidden layers :(integer input only)')
hidden_layers = int(input())
#activation function
print('There are only few activation basic functions but currently we only provide services for below 4 functions. \n1. relu \n2. sigmoid \n3. softmax \n4. tanh \nPlease type the index of the number when you are asked to provide activation function for individual layers.')
print('Please provide input dimensions:')
input_dim = int(input())


# ---------------------------------------------------------

# Hidden layers dimensions and activation functions

# In[4]:


#Hidden layers dimensions
hidden_layer_dim = []
hidden_layer_activation_function = []
for i in range(0,hidden_layers):
    print('Please provide activation units of hidden layer number',i+1)
    hidden_layer_dim.append(int(input()))
    print('Please provide activation function of hidden layer number',i+1)
    hidden_layer_activation_function.append(int(input()))


# In[5]:


#converting activation functions matrix at the back end
activation_matrix = []
for i in range(0,hidden_layers):
    if hidden_layer_activation_function[i] == 1:
        activation_matrix.append('relu')
    elif hidden_layer_activation_function[i] == 2:
        activation_matrix.append('sigmoid')
    elif hidden_layer_activation_function[i] == 3:
        activation_matrix.append('softmax')
    elif hidden_layer_activation_function[i] == 4:
        activation_matrix.append('tanh')
    else:
        print('ERROR!')


# In[6]:


model.add(Dense(hidden_layer_dim[0], input_dim=input_dim, activation=activation_matrix[0]))
    
for i in range(1,hidden_layers):
    model.add(Dense(hidden_layer_dim[i], activation=activation_matrix[i]))


# ----------------------------------------

# Final layer dimensions

# In[7]:


# final layer hyperparams
final_activation_1 = []
print('Please provide final layer dimension:')
final_layer = int(input())
print('Please provide final layer activation function:')
final_activation = int(input())
if hidden_layer_activation_function[i] == 1:
    final_activation_1.append('relu')
elif hidden_layer_activation_function[i] == 2:
    final_activation_1.append('sigmoid')
elif hidden_layer_activation_function[i] == 3:
    final_activation_1.append('softmax')
elif hidden_layer_activation_function[i] == 4:
    final_activation_1.append('tanh')
model.add(Dense(final_layer,activation=final_activation_1[0]))


# ------------------------------------------------------------

# In[8]:


model.summary()


# -------------------------------------------------------------------------------
