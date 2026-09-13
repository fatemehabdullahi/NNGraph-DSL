# NNGraph DSL

This repository contains an **academic compiler project** implementing a **Domain-Specific Language (DSL)** called **NNGraph** for describing neural network architectures in a simple textual format.

The compiler parses NNGraph programs, performs **semantic analysis**, and automatically generates equivalent **PyTorch code** and a **Graphviz representation** of the neural network architecture.

---

## 📌 Project Overview

NNGraph allows users to describe the structure of neural networks without directly implementing them in a deep learning framework.

A user specifies the **model definition, input tensor, network nodes, connections, and optional configuration settings** in an NNGraph file. The compiler then processes the input through several stages:

* Lexical analysis
* Syntax analysis using **ANTLR4**
* Parse Tree generation
* Model extraction using the **Visitor pattern**
* Semantic analysis
* PyTorch code generation
* Graphviz graph generation

The generated PyTorch model can then be used as an executable neural network implementation.

---

## ✨ Features

* Custom **NNGraph Domain-Specific Language**
* Grammar implementation using **ANTLR4**
* Automatic Lexer and Parser generation
* Parse Tree traversal using the **Visitor pattern**
* Internal representation of neural network models
* Semantic validation of network architectures
* Detection of:

  * Duplicate nodes
  * Undefined nodes
  * Invalid edges
  * Orphan nodes
  * Unreachable nodes
  * Cycles
  * Invalid output paths
  * Invalid parameter types and ranges
  * Invalid Residual connections
* Automatic **PyTorch code generation**
* Automatic **Graphviz visualization**
* Support for sequential and multi-branch neural network architectures

---

## 🧠 Supported Layers & Operations

The NNGraph language supports a variety of neural network components.

### Layers

* Linear
* Conv1d
* Conv2d
* BatchNorm2d
* LayerNorm
* MaxPool2d
* AvgPool2d
* Dropout
* Flatten
* Embedding
* MultiHeadAttention
* LSTM
* GRU

### Activation Functions

* ReLU
* Sigmoid
* Tanh
* GELU
* Softmax
* LeakyReLU
* ELU

### Graph Operations

* Add
* Concat
* Residual
* Split

These operations allow the language to describe more complex architectures containing **branches, merges, and skip connections**.

---

## 🏗️ Compiler Architecture

The compiler is designed as a modular pipeline:

```text
NNGraph Source File
        │
        ▼
      Lexer
        │
        ▼
      Parser
        │
        ▼
    Parse Tree
        │
        ▼
     Visitor
        │
        ▼
 Internal Model
        │
        ▼
Semantic Analyzer
        │
        ▼
 ┌──────┴────────┐
 ▼               ▼
PyTorch       Graphviz
Code          Graph
```

The main components are:

* **NNGraph.g4** — Defines the grammar of the language
* **Lexer & Parser** — Generated automatically by ANTLR4
* **Visitor** — Extracts information from the Parse Tree
* **Models** — Defines the internal representation of the network
* **Semantic Analyzer** — Validates the network structure and parameters
* **Code Generator** — Generates equivalent PyTorch code
* **Graphviz Exporter** — Generates a graphical representation of the network
* **Main** — Coordinates the complete compilation process

---

## 🔍 Semantic Analysis

After parsing and constructing the internal representation, the compiler performs several semantic checks to ensure that the neural network is logically valid.

The analyzer verifies:

* Node identifiers are unique
* All edges reference existing nodes
* The declared output node exists
* Required layer parameters are provided
* Parameter types are valid
* Parameter values are within valid ranges
* Nodes are connected to the graph
* All nodes are reachable from the input
* The output is reachable from the input
* The graph does not contain cycles
* Residual nodes have exactly two input connections

Code generation is performed only when the model passes semantic validation successfully.

---

## ⚙️ Code Generation

The Code Generator converts the validated internal model into executable **PyTorch** code.

For example, an NNGraph model containing several Linear layers and activation functions can be automatically converted into a PyTorch `nn.Module`.

The generated code includes:

* PyTorch imports
* Neural network class definition
* Layer initialization
* Forward-pass implementation
* Graph execution order
* Branch and merge handling
* Final output generation

The generator uses a topological ordering of the graph to ensure that each node is executed after its required parent nodes.

---

## 📊 Graphviz Visualization

In addition to generating PyTorch code, NNGraph can generate a **Graphviz representation** of the neural network.

The visualization makes it easier to:

* Understand the network architecture
* Inspect connections between layers
* Visualize branches and merges
* Debug invalid architectures
* Document neural network designs

The generated graph distinguishes the model input, internal nodes, and final output.

---

## 🧪 Test Cases

Several neural network architectures were tested with the compiler, including:

### Example 1 — Simple MLP Classifier

A fully connected neural network containing:

* Linear layers
* ReLU activations
* Dropout
* Softmax output

### Example 2 — ResNet-Style Block

A network containing:

* Convolutional layers
* Batch Normalization
* ReLU
* Residual / Skip Connection
* Flatten

### Example 3 — Multi-Branch Inception-Style Block

A network containing:

* Multiple parallel branches
* Convolutional layers
* ReLU activations
* Concat operation
* Batch Normalization

### Example 4 — Transformer Encoder Block

A network containing:

* Multi-Head Attention
* Dropout
* Layer Normalization
* Linear layers
* GELU activation

The tests demonstrated that valid NNGraph inputs can be parsed, semantically analyzed, and converted into equivalent PyTorch implementations.

---

## 🛠 Tools & Environment

* **Python**
* **ANTLR 4.13.2**
* **PyTorch**
* **Graphviz**
* **ANTLR4 Python Runtime**

---

## 📄 License

This project was developed for **academic and educational purposes** as part of the **Compiler Design Principles** course.
