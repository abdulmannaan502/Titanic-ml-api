import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Clean and preprocess data
def clean_data(df):
    df = df.copy()
    
    # Fill missing age with median
    df["Age"].fillna(df["Age"].median(), inplace=True)

    # Fill embarked with mode
    df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

    # Fill fare with median
    df["Fare"].fillna(df["Fare"].median(), inplace=True)

    # Drop columns not useful for prediction
    df.drop(["Cabin", "Ticket", "Name", "PassengerId"], axis=1, inplace=True)

    # Encode categorical variables
    label_encoders = {}
    for col in ["Sex", "Embarked"]:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    return df, label_encoders

# Preprocess data
df_clean, label_encoders = clean_data(df)

# Split features and target
X = df_clean.drop("Survived", axis=1)
y = df_clean["Survived"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")

# Save model and encoders
joblib.dump(model, "titanic_model.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")
