import pathlib
import os
import prediction_model


PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATA_PATH = os.path.join(PACKAGE_ROOT,"dataset")

TRAIN_FILE = "train.csv"
TEST_FILE = "test.csv"

MODEL_NAME = "clasiffication.pkl"
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,"trained_model")

TARGET="Loan_Status"

# Final Fetaures used in the model 
FEATURES = ['ApplicantIncome', 'CoapplicantIncome' ,'LoanAmount','Loan_Amount_Term','Gender', 'Married',
             'Dependents', 'Education', 'Self_Employed','Credit_History', 'Property_Area']


NUM_FEATURES = ['ApplicantIncome', 'LoanAmount','Loan_Amount_Term']
       
CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed','Credit_History', 'Property_Area']

# Same as CAT in this projects
FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed','Credit_History', 'Property_Area']

FEATURE_TO_MODIFY = ['ApplicantIncome']
FEATURE_TO_ADD = 'CoapplicantIncome'
DROP_FEATURES = ['CoapplicantIncome']

LOG_FEATURES = ['ApplicantIncome', 'LoanAmount'] # Log of numerical coulmns