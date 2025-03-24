
# Data-Science
This repository contains my data science projects
# Gender Classification using Machine Learning

This repository contains a simple implementation of gender classification using three different machine learning algorithms:
- Decision Tree
- Support Vector Machine (SVM)
- k-Nearest Neighbors (k-NN)

## Dataset
The dataset consists of height, weight, and shoe size as input features and gender (male/female) as the target variable.

## Algorithms Used
1. **Decision Tree Classifier**: A tree-based model that splits data into branches based on feature values.
2. **Support Vector Machine (SVM)**: A model that finds the best hyperplane to separate data points.
3. **k-Nearest Neighbors (k-NN)**: A model that classifies based on the majority class of the closest neighbors.

## Installation
Ensure you have Python installed along with the required dependencies:
```sh
pip install scikit-learn
```

## Usage
Run the following Python script to train and test the models:
```python
python gender_classification.py
```

## Predictions
The script trains each classifier and predicts gender for given test inputs. Example outputs:
```
decision tree: female
SVM: male
KNN: female
```

## License
This project is open-source and available under the MIT License.
