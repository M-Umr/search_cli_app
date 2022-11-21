#!/usr/bin/python
# -*- coding: utf-8 -*-
import click
import json
import os


# This function is get all unique searchable fields in the selected json file
def get_all_searchable_fields(data):
    all_unique_fields, new_list = [], []
    all_unique_fields = list(data[0].keys()) #all keys of index 0 dictionary
    
    #print(all_unique_fields)
    
    set1 = set(all_unique_fields)
    for items in data:
        new_list = list(items.keys())
        set2 = set(new_list)
        new_list = list(set2 - set1) #get all values which are not in **all_unique_fields** and extend in same list
        if len(new_list) != 0:
            all_unique_fields.extend(new_list)
    return all_unique_fields
        

# To read any selected json file
def read_json():
    choice = \
        input('''
              Select any option:
              * 1) Users
              * 2) Tickets
              * 3) Organizations
              ''')
    data = dict()
    all_unique_fields = []
    
    if choice == str(1):
        
        #Read file the use json.load to make dictionary and also **get_all_searchable_fields** of this selected file
        with open('users.json', 'r+') as f:
            data = json.load(f)
            all_unique_fields = get_all_searchable_fields(data) 
            file_name = 'users.json'
            
    elif choice == str(2):
        with open('tickets.json', 'r+') as f:
            data = json.load(f)
            all_unique_fields = get_all_searchable_fields(data)
            file_name = 'tickets.json'
            
    elif choice == str(3):
        with open('organizations.json', 'r+') as f:
            data = json.load(f)
            all_unique_fields = get_all_searchable_fields(data)
            file_name = 'organizations.json'
            
    return (file_name, data, all_unique_fields)


# Searching result
def search_fun(data):
    
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


@click.command()
def cli_app_def():
    print("Wlecome to CLI_APP using Python")
    val = \
        input("Type 'quit' anytime to quit or press 'Enter' or anything to continue: ")
    if val == 'quit':
        return
    else:
        value = \
            input('''
              Select any options:
              * press 1 for search
              * press 2 to see all searchable fields
              * type 'quit' to quit anytime
              ''')
            
        if value == str(1):
            file_name, file_, all_searchable_fields = read_json()
            print('Welcome to Search bar')
            search_fun(file_)
            
        elif value == str(2):
            file_name, file_,all_searchable_fields = read_json()
            print('\n\nHere ALL the Searchable Fields of ',str(file_name),'\n')
            print(all_searchable_fields)
            
        elif value == 'quit':
            return
        
        else:
            print('Next time enter correct option')