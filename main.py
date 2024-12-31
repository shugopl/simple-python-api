from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hellow from FastAPI with CI/CD"