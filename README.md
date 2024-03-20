# Diabetes Diagnosis Web Application

This repository contains code for a web application built with Streamlit to predict diabetes using a machine learning model. The model is trained on the `diabetes.csv` dataset and saved as a pickle file named `diabetes.pkl` using `diabetes.py`. The web application is implemented in `webapp.py` using Streamlit.

## Files

- `diabetes.csv`: Dataset containing variables related to diabetes.
- `diabetes.py`: Python script containing code to train the machine learning model and save it as a pickle file (`model.pkl`).
- `webapp.py`: Python script containing code for the Streamlit web application to predict diabetes using the trained model.

## Usage

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository:

    ```bash
    git clone https://github.com/your_username/Diabetes-Diagnosis.git
    ```

3. Navigate to the project directory:

    ```bash
    cd Diabetes-Diagnosis
    ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the Streamlit application:

    ```bash
    streamlit run webapp.py
    ```

6. Access the application in your web browser by visiting [http://localhost:8501](http://localhost:8501).

7. Enter the necessary information such as pregnancies, insulin levels, BMI, age, etc., into the form provided and click on the "Predict" button to get the diabetes prediction.
