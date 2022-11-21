from abc import ABC, abstractmethod
import json

class json_files(ABC):
    
    @abstractmethod
    def get_all_searchable_fields(self, data, file_name):
        pass
        
    @abstractmethod
    def read_json(self):
        pass
 
class users(json_files):
    
    # get all searchable fields 
    def get_all_searchable_fields(self, data, file_name):
        all_unique_fields, new_list = [], []
        all_unique_fields = list(data[0].keys()) #all keys of index 0 dictionary
        set1 = set(all_unique_fields)
        
        for items in data:
            new_list = list(items.keys())
            set2 = set(new_list)

            #subtract two sets to get firelds which are not in **all_unique_fields** and extend in same list
            new_list = list(set2 - set1) 
            
            if len(new_list) != 0:
                all_unique_fields.extend(new_list)
                
        print('\n\nHere ALL the Searchable Fields of **',str(file_name),'**\n')
        print(all_unique_fields)
    
    # To read users json file
    def read_json(self):
        data = dict()
        
        with open('users.json', 'r+') as f:
            data = json.load(f)
            file_name = 'users.json'
            
        return (file_name, data)
 
class tickets(json_files):
    
    def get_all_searchable_fields(self, data, file_name):
        all_unique_fields, new_list = [], []
        all_unique_fields = list(data[0].keys()) #all keys of index 0 dictionary
        set1 = set(all_unique_fields)
        
        for items in data:
            new_list = list(items.keys())
            set2 = set(new_list)
            #subtract two sets to get firelds which are not in **all_unique_fields** and extend in same list
            new_list = list(set2 - set1) 
            
            if len(new_list) != 0:
                all_unique_fields.extend(new_list)
                
        print('\n\nHere ALL the Searchable Fields of **',str(file_name),'**\n')
        print(all_unique_fields)
    
    
    # To read tickets json file
    def read_json(self):
        data = dict()
        
        with open('tickets.json', 'r+') as f:
            data = json.load(f)
            file_name = 'tickets.json'
            
        return (file_name, data)
 
class organizations(json_files):
    
    def get_all_searchable_fields(self, data, file_name):
        all_unique_fields, new_list = [], []
        all_unique_fields = list(data[0].keys()) #all keys of index 0 dictionary
        set1 = set(all_unique_fields)
        
        for items in data:
            new_list = list(items.keys())
            set2 = set(new_list)
            #subtract two sets to get firelds which are not in **all_unique_fields** and extend in same list
            new_list = list(set2 - set1) 
            
            if len(new_list) != 0:
                all_unique_fields.extend(new_list)
                
        print('\n\nHere ALL the Searchable Fields of **',str(file_name),'**\n')
        print(all_unique_fields)
    
    # To read organizations json file
    def read_json(self):
        data = dict()

        with open('organizations.json', 'r+') as f:
            data = json.load(f)
            file_name = 'organizations.json'
            
        return (file_name, data)
