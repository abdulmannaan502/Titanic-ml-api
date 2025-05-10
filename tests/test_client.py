import requests

url = "http://localhost:8000/predict"  # Replace with ngrok URL if using ngrok
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
print(response.json())  
