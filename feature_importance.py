# feature_importance.py

import pandas as pd

def show_feature_importance(model, feature_names, top_n=10):
    """
    Displays the top N most influential features based on model coefficients.

    Parameters:
        model: Trained Linear Regression model
        feature_names: List of feature names (X.columns)
        top_n: Number of top features to display (default is 10)

    Returns:
        top_features_df: DataFrame of top influential features
    """
    coef_df = pd.DataFrame({
        'Feature': feature_names,
        'Coefficient': model.coef_
    })
    coef_df['Abs_Coefficient'] = coef_df['Coefficient'].abs()
    top_features_df = coef_df.sort_values(by='Abs_Coefficient', ascending=False).head(top_n)

    print("🔍 Top Influential Features Affecting Ratings:")
    print(top_features_df[['Feature', 'Coefficient']])

    return top_features_df
