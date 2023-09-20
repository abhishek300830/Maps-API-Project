import os
import inquirer
from helpers.audio_converter import convert_text_to_speech
from controllers.location import Location
from controllers.places import Place
from helpers.validators import validate_string
from termcolor import colored
import traceback
import threading

WELCOME_TEXT = """

____    __    ____  _______  __        ______   ______   .___  ___.  _______    .___________.  ______                   .___  ___.      ___      .______     _______.
\   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|   |           | /  __  \        _     _   |   \/   |     /   \     |   _  \   /       |
 \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__      `---|  |----`|  |  |  |     _| |_ _| |_ |  \  /  |    /  ^  \    |  |_)  | |   (----`
  \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|         |  |     |  |  |  |    |_   _|_   _||  |\/|  |   /  /_\  \   |   ___/   \   \    
   \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____        |  |     |  `--'  |      |_|   |_|  |  |  |  |  /  _____  \  |  |   .----)   |   
    \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|       |__|      \______/                  |__|  |__| /__/     \__\ | _|   |_______/    
                                                                                                                                                                     

"""


class EntryMenu:

    def welcome_menu(self):

        convert_text_to_speech("Welcome to ++Maps")

        while True:
            os.system("cls")
            try:
                answer = self.taking_user_input()
                if answer.get('choice') == 'Search By Any Query':
                    self.search_places_by_query()

                elif answer.get('choice') == 'Search By Location':
                    self.search_by_location()

                elif answer.get('choice') == 'Exit':
                    convert_text_to_speech(
                        "Thank you for using ++Maps. Have a Nice day.")
                    return
            except Exception as error:
                print(traceback.print_exc())
                print("Internal Server Error", error)

            input("Press Enter to Continue....")

    def taking_user_input(self):
        colored_welcome_text = colored(WELCOME_TEXT, 'green', attrs=['bold'])
        print(colored_welcome_text)
        questions = [
            inquirer.List('choice',
                          message="Please Select Your Choice : ",
                          choices=['Search By Any Query',
                                   'Search By Location',
                                   "Exit"],
                          ),
        ]
        answer = inquirer.prompt(questions)
        convert_text_to_speech("You Selected "+answer.get('choice'))
        return answer

    def search_by_location(self):
        locations_list = self.get_places_by_location()
        if locations_list is None:
            return
        place_id = self.choose_correct_location(locations_list)
        if place_id is None:
            return
        geometry = self.get_place_details(place_id)
        type = self.searching_nearby_places()

        formatted_response = self.getting_location_data_from_api(
            geometry, type)

        self.view_detailed_information_of_places(formatted_response)

    def getting_location_data_from_api(self, geometry, type):
        instance = Place()

        response = instance.get_places_by_location(
            geometry, type.get("choice"))

        formatted_response = [{'name': place.get('name'), 'address': place.get(
            'vicinity'), 'place_id': place.get(
            'place_id')} for place in response.get('results')]

        return formatted_response

    def get_places_by_location(self):
        location_instance = Location()
        user_location = self.__input_user_location()
        if validate_string(user_location.get('query')) is None:
            print("Enter Valid Input...")
            return None
        response = location_instance.get_location_by_query(
            user_location.get('query'))

        locations_list = []
        locations = response.get("predictions")
        if locations is not None:
            for location in locations:
                new_dict = {}
                new_dict["description"] = location.get("description")
                new_dict["place_id"] = location.get("place_id")
                locations_list.append(new_dict)
            return locations_list
        else:
            print("Location Data Not Available.")

    def __input_user_location(self):
        questions = [
            inquirer.Text('query', message="Enter Your Location Name : ")
        ]
        answer = inquirer.prompt(questions)
        return answer

    def search_places_by_query(self):
        query = self.__input_user_query()
        if validate_string(query.get('query')) is None:
            print("Enter Valid input...")
            return
        place_instance = Place()
        response = place_instance.get_places_by_query(query.get('query'))
        results = response.get('ok').get('results')
        formatted_response = [{'name': place.get('name'), 'address': place.get(
            'formatted_address'), 'place_id': place.get(
            'place_id')} for place in results]

        self.view_detailed_information_of_places(formatted_response)

    def view_detailed_information_of_places(self, formatted_response):
        while True:
            place = self.choose_place(formatted_response)
            if place.get('choice') == "None of the Above":
                print("No Place Found")
                return
            print("Detailed Information of Place : ")
            for i in formatted_response:
                if i.get('name') == place.get('choice'):
                    print("Name : ", i.get('name'))
                    print("Address : ", i.get('address'))
                    return

    def __input_user_query(self):
        questions = [
            inquirer.Text('query', message="Enter Your Query : ")
        ]
        answer = inquirer.prompt(questions)
        convert_text_to_speech("Your Query : "+answer.get('query'))
        return answer

    def choose_correct_location(self, locations_list):
        choice_list = [location.get("description")
                       for location in locations_list]
        choice_list.append("None of the Above")

        questions = [
            inquirer.List('choice',
                          message="Please Select Your Choice : ",
                          choices=choice_list,
                          ),
        ]
        answer = inquirer.prompt(questions)
        convert_text_to_speech("You Selected "+answer.get('choice'))
        for location in locations_list:
            if location.get("description") == answer.get("choice"):
                return location.get("place_id")
        return None

    def choose_place(self, places):
        choice_list = [place.get("name") for place in places]
        choice_list.append("None of the Above")
        questions = [
            inquirer.List('choice',
                          message="Please Select Your Choice : ",
                          choices=choice_list,
                          ),
        ]
        answer = inquirer.prompt(questions)
        convert_text_to_speech("You Selected "+answer.get('choice'))
        return answer

    def get_place_details(self, place_id):
        places_instance = Place()
        response = places_instance.get_place_details_by_place_id(place_id)
        geometry = response.get('result').get('geometry').get('location')
        lat = geometry.get('lat')
        lng = geometry.get('lng')
        geometry_string = str(lat)+","+str(lng)
        return geometry_string

    def searching_nearby_places(self):
        questions = [
            inquirer.List('choice',
                          message="What do you want Search: ",
                          choices=['Gas Station',
                                   'Landmarks',
                                   'Hospital',
                                   'GYM',
                                   'Malls'],
                          ),
        ]
        answer = inquirer.prompt(questions)
        convert_text_to_speech("You Selected "+answer.get('choice'))
        return answer
