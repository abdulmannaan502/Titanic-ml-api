# 🚢 Titanic Prediction API

A machine learning project that predicts whether a Titanic passenger survived, served via both **REST** and **GraphQL** APIs using **FastAPI** and **Strawberry**.

---

## 📌 FEATURES

- Clean and preprocess Titanic dataset  
- Train a Random Forest model  
- Expose predictions via:  
  - ✅ REST API (POST `/predict`)  
  - ✅ GraphQL API (`/graphql`)  
- Includes unit tests  
- Easily test with Postman and Python  
- Make your API public temporarily using ngrok  

---

## 🛠️ TECH STACK

- **Python**  
- **Pandas**, **Scikit-learn**  
- **FastAPI** (REST)  
- **Strawberry GraphQL** (GraphQL)  
- **Uvicorn** (ASGI server)  
- **Joblib** (model persistence)  
- **Pytest**, **Httpx** (testing)  
- **Ngrok** (exposing local API)  

---

## 📁 PROJECT STRUCTURE

```
titanic_prediction_api/
├── main.py              # FastAPI app (REST + GraphQL)
├── model/
│   ├── train_model.py   # Model training code
│   └── titanic_model.pkl # Trained model
├── schema/
│   └── graphql.py       # GraphQL schema (Strawberry)
├── tests/
│   └── test_api.py      # Unit tests
├── test_client.py       # Python script to test the REST API
├── requirements.txt
└── README.md
```

---

## 📥 SETUP INSTRUCTIONS

### VERIFY VIRTUAL ENVIRONMENT ACTIVATION
```bash
.venv\Scripts\activate
```

### 1. CLONE THE REPOSITORY

```bash
git clone https://github.com/abdulmannaan502/titanic-prediction-api.git
cd titanic_prediction_api
```

### 2. INSTALL DEPENDENCIES

```bash
pip install pandas scikit-learn fastapi uvicorn joblib pytest httpx strawberry-graphql python-multipart
```

### 🧠 TRAIN THE MODEL

```bash
python model/train_model.py
```

### 🚀 RUN THE API

```bash
uvicorn main:app --reload
```

---

## 📬 REST EXAMPLE

### REQUEST: POST `/predict`

```json
{
  "Pclass": 1,
  "Sex": "female",
  "Age": 30,
  "SibSp": 0,
  "Parch": 0,
  "Fare": 100.0,
  "Embarked": "S"
}
```

### RESPONSE:

```json
{
  "survived": true
}
```

---

## 🔮 GRAPHQL EXAMPLE

Open [http://localhost:8000/graphql](http://localhost:8000/graphql) and run the following query:

```graphql
{
  predict(
    Pclass: 1,
    Sex: "female",
    Age: 29,
    SibSp: 0,
    Parch: 0,
    Fare: 100,
    Embarked: "S"
  ) {
    survived
  }
}
```

---

## ✅ RUN UNIT TESTS

```bash
pytest
```

---

## 🧪 TEST WITH PYTHON REQUESTS

Create a file named `test_client.py`:

```python
import requests

url = "http://localhost:8000/predict"  # Replace with your ngrok URL if using
data = {
    "Pclass": 3,
    "Sex": "male",
    "Age": 22,
    "SibSp": 1,
    "Parch": 0,
    "Fare": 7.25,
    "Embarked": "S"
}

response = requests.post(url, json=data)
print(response.json())  # Example output: {'survived': False}
```

Run the script:

```bash
python test_client.py
```

---

## 📬 TEST WITH POSTMAN

- **Method:** POST  
- **URL:** `http://localhost:8000/predict`  
- **Body → raw → JSON:**

```json
{
  "Pclass": 2,
  "Sex": "female",
  "Age": 25,
  "SibSp": 0,
  "Parch": 1,
  "Fare": 26.0,
  "Embarked": "C"
}
```

---

## 🌐 EXPOSE API WITH NGROK

Make your API publicly accessible:

```bash
ngrok http 8000
```

Use the generated public URL in Postman or your Python client.
