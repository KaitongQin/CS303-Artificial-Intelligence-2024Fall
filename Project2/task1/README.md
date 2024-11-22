# Project 2

# SubTask 1 - Image Classification

## Environment preparation
Python version: 3.10

Packages:
```
matplotlib==3.7.1
numpy==1.26.1
tqdm==4.64.1
scikit-learn==1.5.2
```
You can use `pip install -r requirements.txt` to install the above packages.

It is recommended to create a separate environment to keep your programs of project 2 isolated from project 1.
```
conda create -n python310 python=3.10
conda activate python310
conda install jupyter
pip install -r requirements.txt
```

## Requirement
The following files are provided for this subtask:
```
.
├── README.md: read me first
├── requirements.txt: packages needed
├── classification_train_data.pkl: image features of the training set
├── classification_train_label.pkl: image corresponding labels of the training set
├── image_classification_demo.ipynb: the baseline program of project 1 subtask 1
├── SoftmaxRegression.py:implement a softmax regression model
├── classifier.py:a example of `classifier.py` which you need to submit
└── util.py: some common functions

```
You are required to independently train a model using the provided training set. This model should then be utilized to predict labels for the test set. To exemplify this procedure, a Python script named `image_classification_demo.ipynb` has been supplied. You can run `image_classification_demo.ipynb` and observe the results.
Additionally, you have the freedom to customize the provided demo by incorporating your own methodologies.

## Grading
To be graded, you need to implement `classifier.py` and submit it to oj.
<p style="color: red;">
If the test accuracy of your algorithm exceeds that of the given baseline, you will get full points for the subtask, otherwise you will get a score of 0.
</p>
