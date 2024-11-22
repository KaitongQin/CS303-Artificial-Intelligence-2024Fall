# Project 2

# Subtask 3 - Feature Selection

## Environment preparation
Python version: 3.10

Required Packages:
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
├── README.md
├── classification_validation_data.pkl: image features of the classification validation set
├── classification_validation_label.pkl: image corresponding labels of the classification validation set
├── image_recognition_model_weights.pkl: a baseline model for image classification is trained on the training data from sub-task 1 and is fixed
├── feature_selection.ipynb: demonstrate how to select features from the classification_validation_datal.pkl
├── selector.py:a example of `selector.py` which you need to submit
└── image_recognition.ipynb: an image classification process for evaluating the quality of the selected features by evaluating the model on the classification validation set

```
You should write an algorithm to select no more than 30 features from the image features of the classification validation set. 
Here a binary vector of feature mask is applied to each input image vector. This means that for each input image vector x ∈ R^n, the same binary vector mask x ∈{0,1}^n is applied so that x ̌=x∙mask will be the actual input for the trained model during testing. n denotes the dimensionality of the test input vector, and ∙ denotes the inner product of two vectors. 
For example, if n=3, and there is a test input vector of 〈112,345,321〉 and the mask is 〈1,0,1〉, then the x ̌=x∙mask=〈112,345,321〉∙〈1,0,1〉=〈112,0,321〉. The masked features (the feature value 345 in the above example) have no effect on the trained model which means the corresponding feature dimensions are disregarded. 
A demonstration implementation `feature_selection.ipynb` is provided. 
The test procedure is demonstrated in `image_recognition.ipynb`.It reads the mask vectors from `mask_code.pkl` which is the output of running `feature_selection.ipynb`, then uses the mask vectors to mask the features of the classification validation set, predicts the labels using a fixed trained model whose weights are loaded from `image_recognition_model_weights.pkl`, finally calculates the accuracy base on `classification_validation_label.pkl`.

You should re-implement the specific functions in the `feature_selection.ipynb` to construct your feature selection algorithm, and then run the `image_recognition.ipynb` to see if the accuracy improves.

## Grading
To be graded, you need to implement `selector.py` and submit it to oj.
The test procedure is similar to that of `image_recognition.ipynb`. The difference is that when we test, we use the test data.
<p style="color: red;">
If the test accuracy of your algorithm exceeds that of the given baseline, you will get full points for the subtask, otherwise you will get a score of 0.
</p>
