import requests
import logging
from flask import Flask
from flask_smorest import abort

from env_varaibles import url, headers

logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.get("/status")
def check_status():
    return {"status": "UP"}


@app.get("/search/<string:query>")
def query_serch(query):
    querystring = {"radius": "1500", "query": query}
    response = requests.get(url+"/textsearch/json",
                            headers=headers, params=querystring)

    return {"ok": response.json()}


@app.get("/place/<string:query>")
def place_autocomplete(query):
    logger.debug(f"place_autocomplete callled with params: {query}")
    querystring = {"input": query, "radius": "50000"}
    try:
        response = requests.get(url+"/autocomplete/json",
                                headers=headers, params=querystring)
    except Exception as error:
        logger.warning(error)
        abort(400, message="Bad Request")
    return response.json()


@app.get("/place/<string:placeid>/details")
def place_details(placeid):
    querystring = {"place_id": placeid}
    try:
        response = requests.get(url+"/details/json",
                                headers=headers, params=querystring)

    except Exception as error:
        logger.warning(error)
        abort(400, message="Bad Request")

    return response.json()
