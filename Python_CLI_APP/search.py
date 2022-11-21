import json

class users:
    
    # To read users json file
    def read_users(self):
        data = dict()
        
        with open('users.json', 'r+') as f:
            data = json.load(f)
            #all_unique_fields = get_all_searchable_fields(data) 
            file_name = 'users.json'
            
        return (file_name, data)
 
class tickets:
    
    # To read tickets json file
    def read_tickets(self):
        data = dict()
        
        with open('tickets.json', 'r+') as f:
            data = json.load(f)
            #all_unique_fields = get_all_searchable_fields(data) 
            file_name = 'tickets.json'
            
        return (file_name, data)
 
class organizations:
    
    # To read organizations json file
    def read_organizations(self):
        data = dict()

        with open('organizations.json', 'r+') as f:
            data = json.load(f)
            file_name = 'organizations.json'
            
        return (file_name, data)


class search(users, tickets, organizations):

    
    # Searching result
    def search_fun(self, data, file_name):
        
        print('Welcome to Search bar of **', str(file_name), '**')
        file_length = len(data)
        print('\nTerm ID value should be between 0 to ',str(file_length-1))
        value_id = int(input('Enter term number: '))
        
        if value_id >= 0 and value_id <= (file_length-1):
            print('''

    ------------------------SEARCH RESULT------------------------
    ''')
            for i, (j, k) in enumerate(data[value_id].items()):
                print(f'{j:20}{k}')
        else:
            print('No result found')