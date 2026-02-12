import pandas as pd

def preprocess_data(filepath):
    """
    Loads the dataset, handles missing values, encodes categorical variables,
    maps rating text to numeric scores, and returns features (X) and target (y).

    Args:
        filepath (str): Path to the CSV file

    Returns:
        X (DataFrame): Feature matrix
        y (Series): Target vector (numeric rating)
    """

    # Step 1: Load the dataset
    try:
        df = pd.read_csv(filepath, encoding='utf-8')
        print("📥 Dataset loaded successfully with UTF-8 encoding.")
    except UnicodeDecodeError:
        print("⚠️ UTF-8 decoding failed. Retrying with 'latin1' encoding...")
        df = pd.read_csv(filepath, encoding='latin1')
        print("📥 Dataset loaded successfully with Latin-1 encoding.")

    # Step 2: Handle missing values
    df = df.ffill()
    print("🧹 Missing values handled using forward fill.")

    # Step 3: Map 'Rating text' to numeric scores
    rating_map = {
        'Excellent': 5.0,
        'Very Good': 4.0,
        'Good': 3.0,
        'Average': 2.0,
        'Poor': 1.0
    }

    if 'Rating text' not in df.columns:
        raise ValueError("❌ 'Rating text' column not found in dataset.")

    df['Rating'] = df['Rating text'].map(rating_map)

    # Drop rows where mapping failed (e.g., unknown rating text)
    missing_ratings = df['Rating'].isna().sum()
    if missing_ratings > 0:
        print(f"⚠️ Dropping {missing_ratings} rows with unmapped ratings...")
        df = df.dropna(subset=['Rating'])

    print("🔢 'Rating text' successfully mapped to numeric scores.")

    # Step 4: Encode other categorical variables
    categorical_cols = df.select_dtypes(include='object').columns.tolist()
    categorical_cols.remove('Rating text')  # Already handled

    if categorical_cols:
        print(f"🔤 Encoding categorical columns: {categorical_cols}")
        df = pd.get_dummies(df, columns=categorical_cols)
    else:
        print("ℹ️ No additional categorical columns found for encoding.")

    # Step 5: Separate features and target
    X = df.drop(['Rating text', 'Rating'], axis=1)
    y = df['Rating']
    print(f"✅ Features and target separated. Final shape: {X.shape[0]} samples, {X.shape[1]} features")

    return X, y

