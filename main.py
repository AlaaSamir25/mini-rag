from fastapi import FastAPI
app=FastAPI()

@app.post("/welcome")
def welcome():
    return {"message": "Welcome to the FastAPI application!"}