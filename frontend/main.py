import logging

from controllers.location import Location
from helpers.entry_menu import EntryMenu
from controllers.places import Place


logging.basicConfig(filename='app.log',
                    format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    instance = EntryMenu()
    instance.welcome_menu()


if __name__ == "__main__":
    main()
