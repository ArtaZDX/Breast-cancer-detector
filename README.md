# Breast Cancer Detection with Python

This Python program uses machine learning to predict breast cancer. We use the breast cancer dataset from `sklearn.datasets`, split it into training and testing data, apply the K-Neighbors Classifier to it, and visualize the correlation of features with a heatmap.

## Installation and Requirements

Before running the program, ensure you have the necessary libraries. This code requires:

- Python 3.6 or above
- Scikit-learn
- NumPy
- Pandas
- Seaborn
- Matplotlib

If you haven't installed them, you can do it using pip:

```bash
pip install -r requirements.txt
```
## Dataset

The dataset used in this project is the breast cancer wisconsin dataset available in sklearn's datasets. This dataset consists of 30 features and a target variable which indicates the presence of cancer.

## Methodology

The K-Neighbors Classifier is used in this code. The classifier is trained on the training data. After training, the classifier's accuracy is evaluated on the testing data. This gives an idea about the performance of our model.

After model evaluation, we analyze the correlation between features using a heatmap.

## Running the Program

To run the program, simply navigate to the directory containing the Python file and run the following command:

```bash
python3 breast_cancer_detector.py   
```
## Output

Upon running the program, it outputs the following:

1. The accuracy score of the classifier on the testing data.
2. The number of features in the dataset.
3. A pandas DataFrame showing the correlation between different features.
4. A heatmap visualization of the correlation matrix.

## Contributions

Feel free to fork this project, make changes according to your need and create a pull request. Any suggestions or feedbacks are also welcome.

## Disclaimer
This project is intended for educational purposes and should not be used as a definitive medical diagnostic tool. Always consult with a trained medical professional for medical advice.

## License

MIT License
<br />
© Arta Moghaddasi