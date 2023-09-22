import requests
import logging
from flask import Flask
from flask_smorest import abort

from env_variables import url, headers, radius

logging.basicConfig(filename='app.log',
                    format='%(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.get("/status")
def check_status():
    return {"status": "UP"}


@app.get("/search/<string:query>")
def query_search(query):
    """Search for places using a text query string, such as "pizza in Noida" or "shoe stores near Advant noida"."""
    logger.debug(f"query_search callled with params: {query}")

    try:
        querystring = {"radius": radius, "query": query}
        response = requests.get(url+"/textsearch/json",
                                headers=headers, params=querystring)

        return {"ok": response.json()}

    except Exception as error:
        logger.error(error)
        abort(400, message="Bad Request")


@app.get("/nearby_search/<string:location>&<string:type>")
def nearby_search(location, type):
    logger.debug(f"nearby_search callled with params: {location},{type}")

    try:
        querystring = {"location": location, "radius": "1500", "keyword": type}
        response = requests.get(url+"/nearbysearch/json",
                                headers=headers, params=querystring)
        return response.json()

    except Exception as error:
        logger.error(error)
        abort(400, message="Bad Request")


@app.get("/place/<string:query>")
def place_autocomplete(query):
    logger.debug(f"place_autocomplete callled with params: {query}")
    querystring = {"input": query, "radius": "50000"}
    try:
        response = requests.get(url+"/autocomplete/json",
                                headers=headers, params=querystring)
        return response.json()

    except Exception as error:
        logger.warning(error)
        abort(400, message="Bad Request")


@app.get("/place/<string:placeid>/details")
def place_details(placeid):
    logger.debug(f"place_details callled with params: {placeid}")
    querystring = {"place_id": placeid}
    try:
        response = requests.get(url+"/details/json",
                                headers=headers, params=querystring)
        return response.json()

    except Exception as error:
        logger.warning(error)
        abort(400, message="Bad Request")
