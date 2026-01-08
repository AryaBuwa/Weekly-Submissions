import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential            # type: ignore
from tensorflow.keras.layers import Dense                 # type: ignore
from tensorflow.keras.optimizers import Adam              # type: ignore
from tensorflow.keras.losses import BinaryCrossentropy    # type: ignore
import traceback

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

# Exception handling
try :
  # Building the neural network
  model = Sequential()
  model.add(Dense(8, input_dim=2, activation='relu', kernel_initializer='he_normal'))   # First Hidden Layer
  model.add(Dense(4, input_dim=2, activation='relu'))                                   # Second Hidden Layer
  model.add(Dense(1, activation='sigmoid'))                                             # Output Layer

  # Now Compiling the model
  model.compile(optimizer=Adam(learning_rate=0.01), loss=BinaryCrossentropy(), metrics=['accuracy'])

  # training the model
  print("\nTraining the model...")
  history = model.fit(x, y, epochs=1000, verbose=0)

  # Evaluating the model
  loss, accuracy = model.evaluate(x, y, verbose=0)
  print(f"\n Accuracy : {accuracy*100:.2f}%")

  # now making predictions
  predictions = (model.predict(x) > 0.5).astype(int)
  print("\nPredictions")
  print(predictions)

  # Visualize the loss
  plt.figure(figsize=(10, 6))
  plt.plot(history.history['loss'], label='Loss', color='blue')
  plt.xlabel('epochs')
  plt.ylabel('Loss')
  plt.title('Training Loss Over Time')
  plt.legend()
  plt.grid(True)
  plt.show()

# Exception handling for potential errors
except Exception as e:
  print("\n An error ocurred:")
  print(str(e))
  traceback.print_exc()

