import requests
from helpers.env_variables import url, headers
from flask_smorest import abort


class Place:

    def get_places_by_location(self, location):
        querystring = {"location": location, "radius": "1500"}
        try:
            response = requests.get(url+"/nearbysearch/json",
                                    headers=headers, params=querystring)
            return response.json()

        except Exception as error:
            logger.error(error)
            abort(400, message="Bad Request")
