from preprocess import preprocess_data
from split_data import split_dataset
from train_model import train_and_evaluate
from evaluate_model import evaluate_r_squared  
from feature_importance import show_feature_importance

def main():
    try:
        # Step 1: Preprocess the dataset
        filepath = r"C:\Users\Sree Kirthana\Documents\predict_restaurent_ratings (2)\predict_restaurent_ratings\Dataset  (1).csv"
        X, y = preprocess_data(filepath)
        print("✅ Preprocessing complete.")
        print(f"📊 Features shape: {X.shape}")
        print(f"🎯 Target shape: {y.shape}")

        # Step 2: Split the data
        X_train, X_test, y_train, y_test = split_dataset(X, y)
        print("✂ Data split complete.")
        print(f"📦 Training set: {X_train.shape[0]} samples")
        print(f"🧪 Testing set: {X_test.shape[0]} samples")
        print("Please wait a few minutes")

        # Step 3: Train the model
        model, mae, rmse = train_and_evaluate(X_train, y_train, X_test, y_test)
        print("✅ Model training complete.")
        print(f"📐 MAE: {mae:.2f}")
        print(f"📐 RMSE: {rmse:.2f}")

        # Step 4: Evaluate R-squared
        r2 = evaluate_r_squared(model, X_test, y_test)  
        print(f"📈 R-squared Score: {r2:.4f}")

        # Step 5: Show top influential features
        top_features_df = show_feature_importance(model, X.columns.tolist(), top_n=10)
        print("✅ Feature importance analysis complete.")
        print(top_features_df)

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the path.")
    except UnicodeDecodeError as e:
        print("❌ Unicode error while reading the CSV:", e)
    except Exception as e:
        print("❌ Unexpected error:", e)

if __name__ == "__main__":
    main()

