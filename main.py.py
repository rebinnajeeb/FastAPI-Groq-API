#file1
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq

app = FastAPI()
client = Groq(api_key="YOUR_GROQ_API_KEY")

class Question(BaseModel):
    text: str

@app.post("/ask")
def ask_bot(q: Question):
    if not q.text.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": q.text}],
    )
    answer = response.choices[0].message.content
    return {"question": q.text, "answer": answer}

