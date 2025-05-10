# 🚀 Titanic Prediction API – Setup and Usage Guide

## 1. SET UP YOUR ENVIRONMENT

### a. Clone the Repository (if you haven't already)

If you’ve already cloned the repo, skip this step.

```bash
git clone https://github.com/abdulmannaan502/titanic-prediction-api.git
cd titanic-prediction-api
```

### b. Create and Activate a Virtual Environment (optional but recommended)

A virtual environment isolates your project dependencies from the global Python environment.

**Create a new virtual environment:**

```bash
python -m venv venv
```

**Activate the virtual environment:**

- **Windows:**
```bash
venv\Scripts\activate
```

- **Mac/Linux:**
```bash
source venv/bin/activate
```

### c. Install Project Dependencies

Ensure all required libraries are installed using `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🧠 2. TRAIN THE MODEL (IF NOT DONE YET)

If you haven’t trained the model yet, or want to retrain it, you can do that by running:

```bash
python model/train_model.py
```

This step:
- Loads the Titanic dataset.
- Cleans, preprocesses, and trains the Random Forest model.
- Saves the model and encoders to `model/titanic_model.pkl`.

---

## 🚀 3. RUN THE API

### a. Start the FastAPI Server

Now, you can run the FastAPI server to start both REST and GraphQL endpoints.

```bash
uvicorn main:app --reload
```

- **REST API:** [http://localhost:8000/predict](http://localhost:8000/predict)  
- **GraphQL API:** [http://localhost:8000/graphql](http://localhost:8000/graphql)  
- **Swagger UI (API docs):** [http://localhost:8000/docs](http://localhost:8000/docs)  

---

## 🔧 4. TESTING THE API

### a. Test with `test_client.py`

If you want to test the API with a Python script:

```bash
python test_client.py
```

### b. Test with Postman

Open Postman and configure a **POST** request to `http://localhost:8000/predict`.

Add the following JSON body:

```json
{
  "Pclass": 3,
  "Sex": "male",
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked": "S"
}
```

Click **Send**, and you should receive a prediction.

---

## 🌐 5. EXPOSE THE API PUBLICLY (OPTIONAL)

If you want to make the API publicly accessible temporarily (for testing or sharing), you can use **ngrok**.

Start ngrok:

```bash
ngrok http 8000
```

Ngrok will give you a public URL such as `https://4f35-127-0-0-1.ngrok.io` that you can use to access the API from anywhere.

---

## 📄 6. SHUT DOWN THE SERVER

To stop the server, press `CTRL+C` in your terminal.

---

## 🔄 7. RE-RUN THE PROJECT (NEXT TIME)

Whenever you want to run the project again:

**Activate the virtual environment:**

```bash
source venv/bin/activate    # Mac/Linux
# or
venv\Scripts\activate     # Windows
```

**Start the FastAPI server:**

```bash
uvicorn main:app --reload
```

Test the API via Postman or Python requests.

---

## 📝 NOTES

- **Model Training:** You don’t need to retrain the model every time unless you change the training code or want to improve the model.
- **Saving Model:** The model is saved as `model/titanic_model.pkl`. As long as this file exists, FastAPI will load the saved model every time it starts.
