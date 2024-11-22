# Project 2

# Subtask 2 - Image Retrieval

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
├── README.md: read me first
├── image_retrieval_repository_data.pkl: an image repository containing image features
├── image_retrieval_demo.ipynb: the baseline program of project 2 subtask 2
├── NNS.py: implement an NNS model
├── retrieval.py:a example of `retrieval.py` which you need to submit
└── util.py: some common functions

```
You are required to independently train a model using the provided image repository. This model should then be utilized to respond to image queries from the test set. For each image in the test set, you should retrieve **5** similar images from the image repository. The response will be in the form of a list of image IDs retrieved from the image repository. To exemplify this procedure, a Python script named `image_retrieval_demo.ipynb` has been provided. You can run `image_retrieval_demo.ipynb` and observe the results.
Additionally, you have the freedom to customize the provided demo by incorporating your own methodologies.

## Grading
To be graded, you need to implement `retrieval.py` and submit it to oj.

For each test image, suppose you submit **n** similar images(In this subtask, **n** = 5), and there are **m** images that are considered similar by the evaluation process, the accuracy will be calculated as m/n×100%. The test accuracy is the average accuracy across the entire test set.
<p style="color: red;">
If the test accuracy of your algorithm exceeds that of the given baseline, you will get full points for the subtask, otherwise you get a score of 0.
</p>
