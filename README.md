📄 README.md — Task-1: Restaurant Rating Prediction | Cognifyz Technologies
# 📌 Cognifyz Technologies Internship  
## Task-1: Restaurant Rating Prediction using Machine Learning

This repository contains the implementation of **Task-1** for the internship at **Cognifyz Technologies**. The objective of this task is to build a modular machine learning pipeline that predicts restaurant ratings based on various features such as location, cuisine, and visual rating cues.

---

## 🧠 Project Overview

The project follows a structured 5-step pipeline:

1. **Preprocessing**  
   - Handle missing values using forward fill  
   - Encode categorical variables using One-Hot Encoding  
   - Convert target column to numeric  
   - Separate features and target

2. **Data Splitting**  
   - Split the dataset into training and testing sets (80/20 ratio)

3. **Model Training**  
   - Train a Linear Regression model  
   - Evaluate using MAE and RMSE

4. **Model Evaluation**  
   - Calculate R-squared score to assess model performance

5. **Feature Interpretation**  
   - Analyze top influential features using model coefficients

---

## 📁 Folder Structure
predict_restaurant_ratings/
├── preprocess.py # Step 1: Data cleaning and encoding
├── split_data.py # Step 2: Train-test split
├── train_model.py # Step 3: Model training and error metrics
├── evaluate_model.py # Step 4: R-squared evaluation
├── feature_importance.py # Step 5: Feature interpretation
├── main.py #Pipeline controller
└── README.md # Project documentation

---

## 📊 Model Summary

- **Algorithm Used**: Linear Regression  
- **MAE**: 0.00  
- **RMSE**: 0.01  
- **R-squared**: 1.0000

---

## 🔍 Top Influential Features

| Feature                      | Coefficient |
|-----------------------------|-------------|
| Rating color_Orange         | -2.499      |
| Rating color_Green          | +2.493      |
| Rating color_Red            | +1.485      |
| Rating color_Dark Green     | -1.480      |
| Rating color_White          | +0.501      |

---

## 📦 Dataset Details

- Format: CSV  
- Encoding: UTF-8  
- Preprocessing includes:
  - Forward fill for missing values
  - One-Hot Encoding for categorical features
  - Numeric encoding for target column

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install pandas scikit-learn numpy
2.Run the pipeline:
    python main.py

would like to express my sincere gratitude to Cognifyz Technologies for this opportunity.
Task-1 has helped me strengthen my understanding of regression modeling, modular ML workflows,
and feature interpretation.
I look forward to applying these skills in upcoming tasks and continuing to grow as a machine learning engineer.

Submitted by:
Sree Kirthana
Second-year AIML Undergraduate
JB Institute of Engineering and Technology, Telangana.

##This is the sample output
📥 Dataset loaded successfully with UTF-8 encoding.
🧹 Missing values handled using forward fill.
🎨 'Rating color' will be encoded and included in features.
🔤 Categorical variables encoded using One-Hot Encoding.
🔢 Target column encoded numerically.
✅ Features and target separated.
✅ Preprocessing complete.
📊 Features shape: (9551, 20836)
🎯 Target shape: (9551,)
✂️ Data split complete.
📦 Training set size: 7640 samples
🧪 Testing set size: 1911 samples
Please wait a few minutes
🚀 Training Linear Regression model...
✅ MAE: 0.00
✅ RMSE: 0.01
✅ Model training complete.
📐 MAE: 0.00
📐 RMSE: 0.01
📈 R-squared Score: 0.9999
🔍 Top Influential Features Affecting Ratings:
                               Feature  Coefficient
20832              Rating color_Orange    -2.499073
20831               Rating color_Green     2.492583
20833                 Rating color_Red     1.484510
20830          Rating color_Dark Green    -1.479872
20834               Rating color_White     0.500924
20835              Rating color_Yellow    -0.499073
581     Restaurant Name_Bake Me A Cake     0.033499
3978          Restaurant Name_Makhni's     0.025425
4673     Restaurant Name_Oh So Stoned!    -0.024993
14696  Address_Punjabi Bagh, New Delhi    -0.024500
✅ Feature importance analysis complete.
                                                 Feature  ...  Abs_Coefficient
16967                                   Rating color_Red  ...         1.968896
16964                            Rating color_Dark Green  ...         1.960637
16965                                 Rating color_Green  ...         0.993323
16966                                Rating color_Orange  ...         0.992434
11492                    Address_Punjabi Bagh, New Delhi  ...         0.029673
3015                            Restaurant Name_Makhni's  ...         0.029184
11548                  Address_Rajouri Garden, New Delhi  ...         0.029012
7050   Address_24, 1st Floor, Park Center Building, P...  ...         0.026285
10229  Address_Ground Floor, DLF Mall Of India, Secto...  ...         0.026177
1368                       Restaurant Name_Crave Busters  ...         0.026097

[10 rows x 3 columns]
>>> 




