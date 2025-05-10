import strawberry
from strawberry.fastapi import GraphQLRouter
import joblib
import pandas as pd

# Load model and encoders
model = joblib.load("model/titanic_model.pkl")
label_encoders = joblib.load("model/label_encoders.pkl")

@strawberry.type
class PredictionResult:
    survived: bool

@strawberry.type
class Query:
    @strawberry.field
    def predict(
        self,
        Pclass: int,
        Sex: str,
        Age: float,
        SibSp: int,
        Parch: int,
        Fare: float,
        Embarked: str,
    ) -> PredictionResult:
        df = pd.DataFrame([{
            "Pclass": Pclass,
            "Sex": Sex,
            "Age": Age,
            "SibSp": SibSp,
            "Parch": Parch,
            "Fare": Fare,
            "Embarked": Embarked,
        }])
        for col, le in label_encoders.items():
            df[col] = le.transform(df[col])
        pred = model.predict(df)[0]
        return PredictionResult(survived=bool(pred))

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
