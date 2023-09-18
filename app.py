import requests

from flask import Flask
from flask_smorest import abort

from env_varaibles import url,headers


app = Flask(__name__)

@app.get("/status")
def check_status():
    return {"status":"UP"}


@app.get("/search/<string:query>")
def query_serch(query):
    querystring = {"radius":"1500","query":query}
    response = requests.get(url+"/textsearch/json", headers=headers, params=querystring)

    return {"ok":response.json()}

    