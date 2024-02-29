from fastapi import FastAPI, HTTPException
from common import ask_to_get
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# 정적 파일을 제공할 경로를 앱에 마운트합니다.
app.mount("/static", StaticFiles(directory="static"), name="static")

class messageRequest(BaseModel):
    userInput :str



@app.get("/")
def test():
    return FileResponse('index.html')

@app.post("/getMessage")
def test(request : messageRequest):
    try:
        response = ask_to_get(request.userInput) 
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




