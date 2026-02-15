**Content Monetization Modeler**

**Overview :**

Domain **:** Social media Analysis

A Machine Learning project that predicts YouTube ad revenue in usd, for individual videos based on various performance and contextual features and implements the results in a simple Streamlit web application.

**Project Deliverables:**

- Understand the Dataset
- EDA (Exploratory Data Analysis)
- Feature Engineering
- Model Building
- Model Evaluation
- Streamlit App Development
- Interpretation & Insights

**Input features:**

- Video_id,likes,views,comments,watch_time minutes
- Date,Country,Device.

**Target column:**

- Ad_Revenue_usd.

**Technology Used:**

- Python 3.13
- Pandas
- Numpy
- Seaborn,Matplotlib,plotly
- Streamlit App
- Pickle and Joblib

**Understand the Dataset:**

- Read the dataset from csv format to data frame using pandas library
- Then, Understand the Dataset, like what are the input features and find out the target column
- Likes, subscribers…are input features.
- Ad_revenue is the target Column.

**EDA (Exploratory Data Analysis):**

- Getting an idea about datatypes and correcting those data types.
- Handled the Null values(5%), inputting the median values.
- Remove the duplicates values(2%).
- Encode the Categorical variables .(Country, Device, Category).
- Comprehensive statistical Analysis
- Correlation between input feature and target variable.
- Outliers’ detection and handling.
- Distribution Analysis of target variables.

**Feature Engineering:**

Creating the new features:

- Year,
- Month,
- Engagement rate = (Likes + Comments) / Views.

**Model Building:**

Here 5 different kinds of models are utilized.

Linear Regression, Ridge, Lasso, gradient boost regressor, Random forest

Regressor.

**Model Evaluation:**

From which i have taken one model and saved it in the pickle file format.

**Model Selection:**

Model : Linear Regression

Lowest RMSE : 13.80

Lowest MAE : 3.264

Feature selection also done by the model

**Feature importance:**

- Watch time minutes
- Likes
- Comments
- Views , these are important features predicted by the model.

**Realtime predictions:**

Realtime time predictions based on user input done.

Based on input clearly display the Ad_revenue output.

**Key Insights :**

- All models achieved >95% R² score, indicating excellent predictive capability.
- Views, engagement metrics, and subscriber count are primary revenue drivers.
- Model consistency is linear relationship.
