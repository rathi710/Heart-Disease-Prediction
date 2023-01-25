# Heart-Disease-Prediction

## Project Overview
The objective of this project is to check whether the patient is likely to be diagnosed with any
cardiovascular heart diseases based on their medical attributes such as gender, age, chest pain, fasting sugar
level, etc. A dataset is selected with patient’s medical history and attributes. By
using this dataset, we predict whether the patient can have a heart disease or not. To predict this, we use 14
medical attributes of a patient and classify him if the patient is likely to have a heart disease. These medical
attributes are trained under various algorithms like Logistic regression, KNN and Random Forest Classifier, etc. Most
efficient of these algorithms is Logistic Regression which gives us the accuracy of 86%. And, finally we classify
patients that are at risk of getting a heart disease or not and also this method is totally cost efficient.
This project uses Flask API to deploy the model and build the web application.


## Installation 

All libraries are available in Anaconda distribution of Python.

## Dataset
Dataset used: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

The dataset has 14 attributes:
 - age: age in years.
 - sex: sex (1 = male; 0 = female).
 - cp: chest pain type (Value 0: typical angina; Value 1: atypical angina; Value 2: non-anginal pain; Value 3: asymptomatic).
 - trestbps: resting blood pressure in mm Hg on admission to the hospital.
 - chol: serum cholestoral in mg/dl.
 - fbs: fasting blood sugar > 120 mg/dl (1 = true; 0 = false).
 - restecg: resting electrocardiographic results (Value 0: normal; Value 1: having ST-T wave abnormality; Value 2: probable or definite left ventricular hypertrophy).
 - thalach: maximum heart rate achieved.
 - exang: exercise induced angina (1 = yes; 0 = no).
 - oldpeak: ST depression induced by exercise relative to rest.
 - slope: the slope of the peak exercise ST segment (Value 0: upsloping; Value 1: flat; Value 2: downsloping).
 - ca: number of major vessels (0-3) colored by flourosopy.
 - thal: thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect).
 - target: heart disease (1 = no, 2 = yes).


## File Descriptions 

- `heart.csv`: the dataset file.
- `Heart_Disease_Prediction.ipynb`: contains the code of data exploration, preparation and modeling. 
- `heart_model.pkl`: the classification model. 
- `app.py`: Flask API that bind between the classification model and the web page. 
- templates:
	- `index.html`: a web page that contains a form for heart disease testing. 
  - `result.html`: a web page that shows the result based on inputs.
	
## Libraries Used
1. Flask<br>
2. Numpy<br>
3. Pandas<br>
4. Scikit-learn<br>
5. Seaborn<br>
6. Joblib<br>
7. Matplotlib<br>
8. HTML<br>
9. CSS<br>
10. Bootstrap<br><hr>

## Machine Learning algorithms used:

1. Logistic Regression (Scikit-learn)
2. Support Vector Machine (Linear) (Scikit-learn)
3. K-Nearest Neighbours (Scikit-learn)
4. Decision Tree (Scikit-learn)
5. Random Forest (Scikit-learn)
6. XGBoost (Scikit-learn)

Accuracy achieved: 86% (Logistic Regression)



## Accuracies and Confusion matrices<br>

![Screenshot 2023-01-25 214125](https://user-images.githubusercontent.com/85077087/214615819-d503f33a-a860-4c02-aacc-216fddd230a8.png)


![Screenshot 2023-01-25 214216](https://user-images.githubusercontent.com/85077087/214615933-f4153401-aaef-4c99-b266-ac6b2f3506d1.png)

<hr>

