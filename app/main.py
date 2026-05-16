from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def helath_chekc():
    return {"status": "ok"}

@app.get("/add")
def add(a: int, b: int):
  return {"result": a + b}

@app.post("/user")
def create_user(data: dict):
  name = data.get("name", "")
  if not name:
      return {"error": "name is required"}
  return {"message": f"User {name} created"}