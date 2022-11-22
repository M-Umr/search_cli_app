import json

class users:
    
    # To read users json file
    def read_users(self):
        data = dict()
        
        with open('users.json', 'r+') as f:
            data = json.load(f)
            file_name = 'users.json'
            
        return (file_name, data)
 
class tickets:
    
    # To read tickets json file
    def read_tickets(self):
        data = dict()
        
        with open('tickets.json', 'r+') as f:
            data = json.load(f)
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
            
            choice = \
                input('''
                      Select any option:
                        * 1) Whole data of selected ID
                        * 2) Want to see any specific Field data with its ID
                    ''')
                
            if choice == str(1):
                print('''

------------------------SEARCH RESULT------------------------
    ''')
                for i, (j, k) in enumerate(data[value_id].items()):
                    print(f'{j:20}{k}')
                    
            elif choice == str(2):
                print('\nHere all the Fields of the selected ID\n')
                print(list(data[value_id].keys()))
                
                print('\nEnter fields you want to see...\nTo break loop press CTRL+Z and ENTER')
                field_value=[]
                while True:
                    try:
                        field_value.append(input())   #Each input given by the user gets appended to the list "field_value"
                    except EOFError:
                        break 
                print('''

------------------------SEARCH RESULT------------------------
    ''')
                for i, (j, k) in enumerate(data[value_id].items()):
                    if j == '_id' or j in field_value:
                        print(f'{j:20}{k}')
                    else:
                        print('\nPlease enter correct fields, Thanks')
                        break
        else:
            print('No result found')