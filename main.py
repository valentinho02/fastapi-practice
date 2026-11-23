from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"messaage" : "Hello FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return{
        "user_id" : user_id,
        "name": "inho",
    }


@app.get("/search")
def search(keyword: str, limit: int = 10):
    return {
        "keyword" : keyword,
        "limit": limit
    }


from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    user_id: int

@app.post("/chat")
def chat(request: ChatRequest):
    return{
        "user_id" : request.user_id,
        "question" : request.message,
        "answer": f"the input is '{request.message}'."
    }