########################################################### Important Libraries ############################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kstest
import statsmodels.api as sm
import scipy.stats as stats
from feature_engine.outliers import OutlierTrimmer
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from pickle import dump, load
import streamlit as st
from streamlit_option_menu import option_menu
import base64
import warnings
warnings.filterwarnings('ignore')


#################################################### Work With Data and Model prediction #######################################################

# Import Dataset.
def Data(path):
    dataset = pd.read_csv(path)
    return dataset

# Remove Duplicates.
def Remove_Duplicate(Data):
    Data = Data.drop_duplicates()
    return Data

# Feature Engineering.
def Feature_Engineering(Remove_Duplicate, variable):
    Remove_Duplicate.loc[Remove_Duplicate[variable]
                         == 'never', variable] = 'non_smoker'
    Remove_Duplicate.loc[Remove_Duplicate[variable]
                         == 'No Info', variable] = 'non_smoker'
    Remove_Duplicate.loc[Remove_Duplicate[variable]
                         == 'current', variable] = 'current'
    Remove_Duplicate.loc[Remove_Duplicate[variable]
                         == 'former', variable] = 'past_smoker'
    Remove_Duplicate.loc[Remove_Duplicate[variable]
                         == 'ever', variable] = 'past_smoker'
    Remove_Duplicate.loc[Remove_Duplicate[variable]
                         == 'not current', variable] = 'past_smoker'
    return Remove_Duplicate

# Remove Outliers.
def Remove_Outlier(Feature_Engineering, variables):
    trimmer = OutlierTrimmer(
        variables=variables,
        capping_method="iqr",
        tail="both",
        fold=1.5,
    )
    trimmer.fit(Feature_Engineering)
    dataset = trimmer.transform(Feature_Engineering)
    return dataset

# Encoding.
def Encoder(Remove_Outlier, var1, var2, var3, var4, var5, var6, var7, var8):
    le = LabelEncoder()
    col = [var1, var2, var4]
    for i in col:
        le.fit_transform(Remove_Outlier[i])
    dataset = pd.get_dummies(Remove_Outlier, columns=[var1, var2, var3, var4])
    dataset = dataset.drop([var5, var6, var7, var8], axis=1)
    return dataset

# Feature Scaling.
def Scaling(Encoder):
    sc = MinMaxScaler()
    sc.fit(Encoder)
    dump(sc, open('Scale.pkl', 'wb'))
    Encoder = sc.transform(Encoder)
    return Encoder


# Concat two data frame.
def Concatenate(Encoder, Scaling):
    data = pd.DataFrame(
        Scaling, columns=['age', 'bmi', 'HbA1c_level', 'blood_glucose_level'])
    Encoder.reset_index(drop=True, inplace=True)
    data.reset_index(drop=True, inplace=True)
    dataset = pd.concat([data, Encoder], axis=1)
    return dataset

# Fix imblanced data.
def Imbalanced_Data(Encoder, predictor):
    y = Encoder[predictor]
    X = Encoder.drop([predictor], axis=1)
    smote = SMOTE(sampling_strategy=0.5)
    X_over, y_over = smote.fit_resample(X, y)
    dataset = pd.concat([X_over, y_over], axis=1)
    return dataset


# Split train and test data.
def X_train(Imbalanced_Data, predictor):
    y = Imbalanced_Data[predictor]
    X = Imbalanced_Data.drop([predictor], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, stratify=y, random_state=141)
    return x_train


def Y_train(Imbalanced_Data, predictor):
    y = Imbalanced_Data[predictor]
    X = Imbalanced_Data.drop([predictor], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, stratify=y, random_state=141)
    return y_train


# Random Forest Classifier.
def RandomForest(X_train, y_train):
    RFC = RandomForestClassifier()
    RFC.fit(X_train, y_train)
    dump(RFC, open('model1.pkl', 'wb'))


# XGBoost Classifier.
def XG(X_train, y_train):
    XGB = XGBClassifier()
    XGB.fit(X_train, y_train)
    dump(XGB, open('model2.pkl', 'wb'))


########################################################### Working with main data ############################################################

Main_data = Data('diabetes.csv')
Remov_dup = Remove_Duplicate(Main_data)
Feature_engin = Feature_Engineering(Remov_dup, 'smoking_history')
After_outlier = Remove_Outlier(Feature_engin, ["age", "bmi", "HbA1c_level", "blood_glucose_level"])
Encoding = Encoder(After_outlier, 'gender', 'hypertension', 'smoking_history', 'heart_disease', 'age', 'bmi', 'HbA1c_level', 'blood_glucose_level')
Scale = Scaling(After_outlier[['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']])
Con = Concatenate(Encoding, Scale)
Imb = Imbalanced_Data(Con, 'diabetes')
X = X_train(Imb, 'diabetes')
y = Y_train(Imb, 'diabetes')
RandomForest(X, y)
XG(X, y)