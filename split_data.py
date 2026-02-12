# split_data.py

from sklearn.model_selection import train_test_split

def split_dataset(X, y, test_size=0.2, random_state=42):
    """
    Splits the dataset into training and testing sets.

    Parameters:
        X (DataFrame): Feature matrix
        y (Series): Target variable
        test_size (float): Proportion of data to use for testing (default is 20%)
        random_state (int): Seed for reproducibility

    Returns:
        X_train, X_test, y_train, y_test: Split datasets
    """

    # Perform the split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Print confirmation
    print("✂️ Data split complete.")
    print(f"📦 Training set size: {X_train.shape[0]} samples")
    print(f"🧪 Testing set size: {X_test.shape[0]} samples")

    return X_train, X_test, y_train, y_test
