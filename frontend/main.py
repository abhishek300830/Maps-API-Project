
from controllers.location import Location
from helpers.entry_menu import EntryMenu

import logging


logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    instance = EntryMenu()
    instance.welcome_menu()

if __name__ == "__main__":
    # main()
    instance = Location()
    instance.get_location_by_query("Noida")

    




