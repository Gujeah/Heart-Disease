# Heart-Disease Classifier
A repository showing a walkthrough of heart disease prediction I did from EDA to deployment

I am more than glad to welcome you all for my machine learning project. This project is a heart disease risk classifier prediction web application built using Flask and served using Waitress in a Docker container. The application processes user input data and predicts the probability of heart disease risk using a trained machine learning model.
With the evolving field of machine learning and artificial intelligence, the  aim of this project is to help health professionals to classify the conditions of the person if he has the likelihood of having heart diseaes to minimize the errors tha the professionals make sometimes when diagnonising someone with a heart disease. 

<h2> Problem Statement </h2>
Heart disease is one of the leading cause of death worldworld, claiming over 17.9 million lives each year In United States of America alone, someone dies from heart diseases every 37 seconds. This is a devastating situation which needs urgent intervations to reduce these death by either diagnosing patients quickly before the symptoms stats to progress and by encorporating the power of machine learning to predict the likehood of a ptient to get that disease so that we should provide right guidance to improve the health and well being of people in line with United Nation Sustainable Development Goals (SDG3)
<strong>The Objective of this project</strong> : developing a machine learning model which classifies the likelihood of a heart disease based on the parameters that are shown in an individual
<h2> Source of the Data</h2>
I used data from Kaggle and it has these features id (Unique id for each patient)
age (Age of the patient in years),origin (place of study), sex (Male/Female), cp chest pain type ([typical angina, atypical angina, non-anginal, asymptomatic]),trestbps resting blood pressure (resting blood pressure (in mm Hg on admission to the hospital)), chol (serum cholesterol in mg/dl), fbs (if fasting blood sugar > 120 mg/dl), restecg (resting electrocardiographic results)Values: [normal, stt abnormality, lv hypertrophy], thalach: maximum heart rate achieved, exang: exercise-induced angina (True/ False)
oldpeak: ST depression induced by exercise relative to rest, slope: the slope of the peak exercise ST segment, ca: number of major vessels (0-3) colored by fluoroscopy
thal: [normal; fixed defect; reversible defect],num: the predicted attribute
<h1>The Process of bringing ths project to life</h1>
<h2> Data Loading and Exploitory Data Analysis (Getting our hands dirty)</h2>
Using Pandas  I loaded the data. After that, duplicates were checked (using drop_duplicates), changed the text in the same format to prevent errors that could have arised during our modeling. I then checked if the columns had some null values, used describe function to see how the data was distributed. The step by step EDA is much explained in the train.py file.
<h2>Model development and Saving</h2>
In this project I made two pipelines; one consisting of a logistic regression and onehot encoder and the other one consisting of a decision tree classifier and one hot encoder. The one which had decision tree performed better unlike the one which used logistice regression. Using pickle I saved my model for deployment. For more detailed walkthrough on how I navigated refer to the train.py file in the folder

<h2> Deployment: Local Deployment</h2>
<strong>Tools</strong>: I used Flask for the backend and I also made a simple web page using html and css to provide a professional interface for the predicted values that were coming from the model. Additionally, I used Docker as a container of this application. 
<h2>Future work</h2>
Despite the good performance of the model, I believe that I need to reduce false negatives that were found after training a model by tryng other models. Additionally, I apln to deploy this project on cloud like AWS
<h2>Acknowlegement</h2>
Special thanks to the Data Talks Club for providing a free machine learning zoomcamp and for giving me this opportunity to choose a proect of my choice and reach this far. I have learnt alot from this data and the skills I gained will be of much value to my career



