import inquirer
from prettytable import PrettyTable
from pprint import pprint
from controllers.location import Location
from controllers.places import Place


class EntryMenu:

    def welcome_menu(self):

        answer = self.taking_user_input()

        if answer.get('choice') == 'Search By Any Query':
            self.search_places_by_query()

        elif answer.get('choice') == 'Search By Location':
            locations_list = self.search_places_by_location()
            self.choose_correct_location(locations_list)

    def taking_user_input(self):
        print("This is Welcome Menu...")
        questions = [
            inquirer.List('choice',
                          message="Please Select Your Choice : ",
                          choices=['Search By Any Query',
                                   'Search By Location'],
                          ),
        ]
        answer = inquirer.prompt(questions)
        return answer

    def search_places_by_location(self):
        location_instance = Location()
        user_location = self.__input_user_location()
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
        place_instance = Place()
        response = place_instance.get_places_by_query(query.get('query'))
        results = response.get('ok').get('results')
        formatted_response = [{'name': place.get('name'), 'address': place.get(
            'formatted_address'), 'place_id': place.get(
            'place_id')} for place in results]

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
        return answer

    def choose_correct_location(self, locations_list):
        choice_list = [location.get("description")
                       for location in locations_list]
        questions = [
            inquirer.List('choice',
                          message="Please Select Your Choice : ",
                          choices=choice_list,
                          ),
        ]
        answer = inquirer.prompt(questions)
        return answer

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
        return answer
