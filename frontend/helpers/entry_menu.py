from typing import Any
import inquirer
from pprint import pprint
from controllers.location import Location


class EntryMenu:

    def welcome_menu(self):

        answer = self.taking_user_input()

        print(answer)

        if answer.get('choice') == 'Search By Query':
            self.search_places_by_query()
        elif answer.get('choice') == 'Search By Location':
            self.search_places_by_location()

    def taking_user_input(self):
        print("This is Welcome Menu...")
        questions = [
            inquirer.List('choice',
                          message="Please Select Your Choice : ",
                          choices=['Search By Query', 'Search By Location'],
                          ),
        ]
        answer = inquirer.prompt(questions)
        return answer

    def search_places_by_location(self):
        response = self.get_places_by_location()
        pprint(response)

    def get_places_by_location(self):
        location_instance = Location()
        response = location_instance.get_location_by_coordinates()
        return response

    def search_places_by_query(self):
        response = self.get_places_by_query()
        pprint(response)

    def get_places_by_query(self):
        query = self.input_user_query()
        location_instance = Location()
        response = location_instance.get_location_by_query(query.get('query'))
        return response

    def input_user_query(self):
        questions = [
            inquirer.Text('query', message="Enter Your Query : ")
        ]
        answer = inquirer.prompt(questions)
        return answer


if __name__ == "__main__":
    obj = EntryMenu()
    res = obj.input_user_query()
    print(res)
