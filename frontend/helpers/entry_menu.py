import inquirer

from controllers.location import Location


class EntryMenu:
    
    def welcome_menu(self):

        answer = self.taking_user_input()

        print(answer)
        
        if answer.get('choice')=='Search By Query':
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

        
        
        