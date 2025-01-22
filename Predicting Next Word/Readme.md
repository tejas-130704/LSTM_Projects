# Next Word Prediction

This project is a **Next Word Prediction** application built using **Streamlit**. It uses a trained LSTM model to predict the next word based on the input text provided by the user. The project is designed to provide real-time predictions with an intuitive and user-friendly interface.

## Features
- **Interactive Interface**: Built using Streamlit, ensuring an easy-to-use and responsive application.
- **Accurate Predictions**: Powered by a trained LSTM model to predict the next word with high accuracy.

## Requirements
Make sure you have the following installed:
- Python 3.7 or higher
- Streamlit
- TensorFlow
- Other required dependencies (listed in `requirements.txt`)

## Setup Instructions
Follow the steps below to set up and run the project on your local machine:

### Step 1: Clone the Repository
```bash
git clone https://github.com/tejas-130704/LSTM_Projects.git
cd next-word-prediction
```

### Step 2: Install Dependencies
Install all required dependencies using the following command:
```bash
pip install -r requirements.txt
```

### Step 3: Download the LSTM Model
The trained LSTM model file (`lstm_new_model.h5`) is too large to store on GitHub. It is hosted in a Google Drive folder. Follow these steps to download and use it:

1. Click on the link below to access the Google Drive folder:
   [Next Word Prediction - Google Drive Folder](https://drive.google.com/drive/folders/1ecPa2vGnYDlLSkT59FBaW5mRFhxk4PJ1?usp=sharing)
2. Locate the folder named **"Next Word Prediction"**.
3. Download the file `lstm_new_model.h5`.
4. Place the downloaded file in the root directory of this repository.

### Step 4: Run the Application
Start the Streamlit application with the following command:
```bash
streamlit run app.py
```
This will launch the application in your default web browser.

### Step 5: Using the Application
1. Enter the text in the input field.
2. The application will predict the next word based on the input text.

## Folder Structure
The repository structure is as follows:
```
next-word-prediction/
├── main.py                 # Main Streamlit application
├── lstm_new_model.h5     # LSTM model file (download from Google Drive)
├── requirements.txt      # List of dependencies
└── tokenizer.pkl
```

## Screenshots

![Screenshot 2025-01-22 211312](https://github.com/user-attachments/assets/16dc0f0b-a63b-4924-9312-e951767d4f19)


---

For any issues or queries, feel free to raise an issue in the repository or contact the author.


