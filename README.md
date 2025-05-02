# Amharic Speech Recognition

In this project we are going to build deep learning model  to process and convert Ethiopians Amharic language speech/voice to text format.

## Table of Content
- [Introduction](#introduction)
- [Install](#instalation)
- [Data](#data)
- [Notebooks](#notebooks)
- [Scripts](#scripts)
- [Technologies used](#technologies-used)

### Introduction
The World Food Program wants to deploy an intelligent form that collects nutritional information of food bought and sold at markets in three different countries in Africa - Ethiopia and Kenya.  

The design of this intelligent form requires selected people to install an app on their mobile phone, and whenever they buy food, they use their voice to activate the app to register the list of items they just bought in their own language. The intelligent systems in the app are expected to live to transcribe the speech-to-text and organize the information in an easy-to-process way in a database. 

It is our obligation to create a deep learning model capable of converting speech to text. The model we create should be precise and resistant to background noise.
This project was created during the fourth week of the Machine Learning training session at 10Academy.

### To Get Started

- **Requirements**
``` 
git clone https://github.com/abu14/end-to-end-speech-to-text/
cd end-to-end-speech-to-text
pip install -r requirements.txt
```

- **Model Training & Versioning**
```
mlflow ui
```

- **Dashboard**
```
streamlit run app.py
```

### Data

The folder is being tarcked with DVC and the files are only shown after cloning and setting up locally. The sub-folder ```AMHARIC``` contain ```training``` and ```testing``` files for our model. Both files contain similar file structure.

- **```wav/```** : a folder containing all audio files
- **```text```** : file contining the metadata (audio file name and cropsonding transcription)
- **```spk2utt```**, **```trsTest.txt```**, **```utt2spk```**,  **```wav.scp```** : these are files provided with the dataset, Currently they don't have a purpose but could be used for future analysis.
