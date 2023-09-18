import requests

from flask import Flask
from flask_smorest import abort

from env_varaibles import url, headers


app = Flask(__name__)


@app.get("/status")
def check_status():
    return {"status": "UP"}


@app.get("/search/<string:query>")
def query_serch(query):
    try:
        querystring = {"radius": "1500", "query": query}
        response = requests.get(url+"/textsearch/json",
                                headers=headers, params=querystring)

        return {"ok": response.json()}
    except Exception as error:
        abort(400,message="Bad Request")

@app.get("nearby_search/<string:location>")
def nearby_search(location):

    try:
        querystring = {"location":location,"radius":"1500"}
        response = requests.get(url+"/nearbysearch/json", headers=headers, params=querystring)
        return response.json()
    except Exception:
        abort(400,message="Bad Request")


@app.get("/place/<string:query>")
def place_autocomplete(query):
    querystring = {"input": query, "radius": "50000"}
    response = requests.get(url+"/autocomplete/json",
                            headers=headers, params=querystring)

    return response.json()


@app.get("/place/<string:placeid>/details")
def place_details(placeid):
    querystring = {"place_id": placeid}
    response = requests.get(url+"/details/json",
                            headers=headers, params=querystring)

    return response.json()
