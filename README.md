# 🧠 Artificial Neuron From Scratch

A beginner-friendly implementation of an Artificial Neuron and Perceptron using Python.

This project demonstrates how a simple artificial neuron works internally using:

- Inputs
- Weights
- Bias
- Weighted Sum
- Activation Function
- Prediction
- Perceptron Training

The project also implements an OR Gate using a simple perceptron.

---

## 🚀 Project Overview

An artificial neuron is one of the fundamental building blocks of neural networks.

It receives input values, multiplies them by weights, adds a bias, and passes the result through an activation function.

The basic idea is:

Input → Weighted Sum → Activation Function → Output

This project implements these concepts from scratch to understand what happens inside a simple neural network.

---

## 🧠 Concepts Covered

- Artificial Neuron
- Perceptron
- Inputs
- Weights
- Bias
- Weighted Sum
- Step Activation Function
- Prediction
- Perceptron Learning
- OR Gate
- Model Training

---

## 📊 OR Gate

The project uses the following OR Gate dataset:

| Input 1 | Input 2 | Output |
|--------:|--------:|-------:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

The perceptron learns this relationship during training.

---

## ⚙️ How It Works

The neuron first calculates the weighted sum:

Weighted Sum = (Input × Weight) + Bias

Then an activation function determines the final output.

For the perceptron, a simple step function is used:

- If the value is greater than or equal to 0 → Output 1
- Otherwise → Output 0

---

## 🛠️ Technologies Used

- Python
- NumPy

---

## 📂 Project Structure

```text
artificial-neuron-from-scratch/
│
├── artificial_neuron.py
├── build_OR_Gate.py
├── README.md
├── requirements.txt
└── .gitignore

▶️ How to Run
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/artificial-neuron-from-scratch.git
2. Open the project
cd artificial-neuron-from-scratch
3. Install dependencies
pip install -r requirements.txt
4. Run the project
python build_OR_Gate.py
📌 Example Output
[0, 0] -> 0
[0, 1] -> 1
[1, 0] -> 1
[1, 1] -> 1
🎯 Learning Outcomes

After completing this project, I learned:

How an artificial neuron works
How weights affect predictions
Why bias is important
How activation functions work
How a perceptron learns from data
How a simple neural network can solve the OR Gate problem
🔮 Future Improvements
Implement AND Gate
Implement NOT Gate
Implement XOR Gate using multiple neurons
Build a multi-layer neural network from scratch
Implement gradient descent
Compare the implementation with TensorFlow/Keras
👨‍💻 Author

Dinbandhu Kumar Jha

Aspiring AI / ML Engineer

Python | Machine Learning | Deep Learning | Artificial Intelligence
