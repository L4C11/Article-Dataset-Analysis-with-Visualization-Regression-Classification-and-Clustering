# Data Mining & Machine Learning Analysis

## Project Overview
This project performs a comprehensive data mining analysis on a structured dataset of online news articles. The objective was to uncover hidden patterns using unsupervised learning techniques and to build predictive models for article categorization and popularity prediction.

## Workflow & Methodology

### 1. Data Preprocessing & EDA
- Data cleaning and normalization using `StandardScaler`.
- Exploratory Data Analysis (EDA) with **Seaborn** and **Matplotlib** to visualize correlations and distributions.

### 2. Unsupervised Learning (Clustering)
- Applied **K-Means** and **DBSCAN** algorithms to identify inherent groupings and density-based clusters within the article metadata (e.g., keywords, LDA topics).

### 3. Supervised Learning
- **Regression:** Implemented **Linear Regression** to predict the number of shares (article popularity).
- **Classification:** Built and compared multiple models to classify articles into 7 distinct topics:
  - Logistic Regression
  - Decision Tree Classifier
  - **Support Vector Machine (SVM)**

## Key Results
The comparative analysis showed that the **Support Vector Machine (SVM)** model with a linear kernel yielded the best performance for topic classification.

- **Accuracy:** **54.12%**
- **Context:** Given 7 distinct categories, a random guess would result in ~14.28% accuracy. The SVM model significantly outperforms the random baseline, demonstrating strong predictive power on the dataset.

## Technologies Used
- **Python** (3.x)
- **Pandas & NumPy** (Data Manipulation)
- **Scikit-learn** (Machine Learning algorithms)
- **Matplotlib & Seaborn** (Visualization)
