from flask import Flask,request
from flask_smorest import abort

app = Flask(__name__)

@app.get("/hello")
def print_hello():
    return {"message":"hello..done"}