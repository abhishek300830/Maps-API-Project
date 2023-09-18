import inquirer

from pprint import pprint
from controllers.location import Location
from controllers.places import Place


class EntryMenu:

    def welcome_menu(self):

        answer = self.taking_user_input()

        if answer.get('choice') == 'Search By Any Query':
            self.search_places_by_query()

        elif answer.get('choice') == 'Search By Location':
            self.search_places_by_location()

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

        pprint(response)

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
        pprint(formatted_response)

    def __input_user_query(self):
        questions = [
            inquirer.Text('query', message="Enter Your Query : ")
        ]
        answer = inquirer.prompt(questions)
        return answer


# if __name__ == "__main__":
#     obj = EntryMenu()
#     res = obj.input_user_query()
#     print(res)
