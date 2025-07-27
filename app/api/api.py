from fastapi import FastAPI, HTTPException
from starlette.responses import Response
import uvicorn

app= FastAPI()
@app.get("/")
def root():
    return {"message: FastAPI in python"}

@app.post("/add")
def add(a,b):
    a=int(a)
    b=int(b)
    return a+b

@app.post("/sub")
def sub(a,b):
    a=float(a)
    b=float(b)
    return a-b

if __name__ == "__main__":
    #print(add(a=2.3,b=4))
    #print(sub(a=3,b=5))
    #print("This is the initialization of my AI Journey")

    uvicorn.run(app, port=5001)