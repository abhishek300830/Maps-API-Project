from helpers.env_variables import base_url
import requests
import logging
logger = logging.getLogger(__name__)


class Place:

    def get_places_by_location(self, location):  # location = "lat,lng"
        logger.debug(f"called get_places_by_location with params: {location}")
        try:
            response = requests.get(
                base_url+f"/nearby_search/{location}")
            return response.json()

        except Exception as error:
            logger.error(f"Error in get_places_by_location: {error}")
            return {"error": "Something went wrong while fetching places."}

    def get_places_by_query(self, query):
        logger.debug(f"called get_places_by_query with params: {query}")
        try:
            response = requests.get(
                base_url+f"/search/{query}")
            return response.json()

        except Exception as error:
            logger.error(f"Error in get_places_by_query: {error}")
            return {"error": "Something went wrong while fetching places."}
    
    def get_place_details_by_place_id(self,place_id):
        logger.debug(f"called get_place_details_by_place_id with params: {place_id}")
        try:
            response = requests.get(
                base_url+f"/place/{place_id}/details")
            return response.json()
        except Exception as error:
            logger.error(f"Error in get_place_details_by_place_id: {error}")
            return {"error": "Something went wrong while fetching lat long."}
            


# if __name__ == "__main__":
#     instance = Place()
#     response = instance.get_places_by_location("12.9716,77.5946")

#     print(response)
