#file2 
import requests

URL = "http://127.0.0.1:8000/ask"

while True:
    question = input("\nAsk something (or type 'quit'): ")
    if question.lower() == "quit":
        break
    response = requests.post(URL, json={"text": question})
    data = response.json()
    print("\nBot:", data["answer"])