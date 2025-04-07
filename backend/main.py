from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.db import init_db, save_function, get_function
from backend.docker_runner import execute_function

app = FastAPI()
init_db()

class FunctionRequest(BaseModel):
    name: str
    code: str
    language: str
    timeout: int = 5

@app.post("/functions")
def create_function(function_req: FunctionRequest):
    save_function(function_req)
    return {"status": "Function saved"}

@app.get("/functions/{name}")
def fetch_function(name: str):
    func = get_function(name)
    if not func:
        raise HTTPException(status_code=404, detail="Function not found")
    return func

@app.post("/functions/{name}/execute")
def run_function(name: str):
    func = get_function(name)
    if not func:
        raise HTTPException(status_code=404, detail="Function not found")
    result = execute_function(func)
    return {"output": result}