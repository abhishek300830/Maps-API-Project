import requests
import logging

from helpers.env_variables import base_url 
logger = logging.getLogger(__name__)

class Location:

    def get_location_by_query(self,query):

        logger.debug(f"place_autocomplete callled with params: {query}")
        try:
            response = requests.get(base_url+"/place/"+query)
            return response.json()

        except Exception as error:
            logger.error(error)


