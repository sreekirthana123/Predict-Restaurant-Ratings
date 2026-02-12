# evaluate_model.py

from sklearn.metrics import r2_score

def evaluate_r_squared(model, X_test, y_test):
    """
    Evaluates the R-squared score of a trained regression model.

    Parameters:
        model: Trained regression model
        X_test: Features of the test set
        y_test: True target values of the test set

    Returns:
        r2: R-squared score
    """
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    print(f"📈 R-squared Score: {r2:.4f}")
    return r2
