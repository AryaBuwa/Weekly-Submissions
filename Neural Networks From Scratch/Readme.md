# MNIST Digit Recognition with a Neural Network (NumPy & Pure Math)

This repository contains a Jupyter Notebook demonstrating how to build a **two-layer neural network from scratch** using pure Python and NumPy. The project trains a neural network to accurately classify handwritten digits from the classic MNIST dataset.

---

### Project Overview

This project covers:

- **Data Loading & Preprocessing:** Loading the MNIST `train.csv`, transposing, splitting into training and validation sets, and normalizing pixel values.
- **Neural Network Architecture:** A structured network with an input layer, a hidden layer of 128 units, and an output layer with 10 units for digits 0-9.
- **Parameter Initialization:** Random initialization of weights and biases.
- **Activation Functions:** Implementation of Leaky ReLU for the hidden layer and Softmax for the output layer.
- **Forward Propagation:** Computing the network's output given input data.
- **One-Hot Encoding:** Converting labels into a suitable format for training.
- **Backward Propagation:** Calculating gradients of the loss with respect to weights and biases.
- **Gradient Descent:** Updating network parameters to minimize loss and improve accuracy.
- **Prediction & Accuracy Evaluation:** Functions to make predictions and evaluate model performance.
- **Visualization:** Plotting training and validation accuracy to monitor learning progress.

---

### Technologies Used

- **Python:** Primary programming language.
- **NumPy:** For efficient numerical computations.
- **Pandas:** For data handling and preprocessing.
- **Matplotlib:** For visualization of training progress.

---

### Dataset

The project uses the MNIST Digit Recognizer dataset, consisting of grayscale images of handwritten digits (0-9). This dataset is available on platforms such as Kaggle.

---

### How to Run

1. Clone the repository:

   ```bash
   git clone git clone https://github.com/AryaBuwa/Weekly-Submissions.git
   cd Weekly-Submissions/Neural\ Networks\ From\ Scratch

2. Ensure Python is installed.

3. Install required libraries:

    ```bash
    pip install jupyter numpy pandas matplotlib

4. Place the train.csv (and optionally test.csv) file in the same directory as the notebook, or update the file paths accordingly.

5. Launch Jupyter Notebook: 
    
    ```bash
    jupyter notebook

6. Open building-a-neural-network-with-mnist-numpy-math.ipynb.

7. Run the notebook cells sequentially to train and evaluate the neural network.

---

### Credits

Inspired by Samson Zhang’s YouTube tutorial: https://www.youtube.com/watch?v=w8yWXqWQYmU&ab_channel=SamsonZhang

Assistance from ChatGPT for code explanations and README structuring.