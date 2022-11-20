#!/usr/bin/python
# -*- coding: utf-8 -*-
import click
import json

def get_all_searchable_fields(data):
    all_unique_fields, new_list = [], []
    all_unique_fields = list(data[0].keys())
    
    #print(all_unique_fields)
    
    set1 = set(all_unique_fields)
    for items in data:
        new_list = list(items.keys())
        set2 = set(new_list)
        new_list = list(set2 - set1)
        if len(new_list) != 0:
            all_unique_fields.extend(new_list)
    return all_unique_fields
        


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
        with open('D:/myprojects/assessments/ginkgo assessment/json/users.json'
                  , 'r+') as f:
            data = json.load(f)
            all_unique_fields = get_all_searchable_fields(data)
            file_name = 'users.json'
    elif choice == str(2):
        with open('D:/myprojects/assessments/ginkgo assessment/json/tickets.json'
                  , 'r+') as f:
            data = json.load(f)
            all_unique_fields = get_all_searchable_fields(data)
            file_name = 'tickets.json'
    elif choice == str(3):
        with open('D:/myprojects/assessments/ginkgo assessment/json/organizations.json'
                  , 'r+') as f:
            data = json.load(f)
            all_unique_fields = get_all_searchable_fields(data)
            file_name = 'organizations.json'
    return (file_name, data, all_unique_fields)



def search_fun(data):
    
    file_length = len(data)
    print('\n','Term ID value should be between 0 to ',str(file_length-1))
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
#@click.option('--quit_or_enter','-q_or_e', help='Type "quit" anytime to quit or press "Enter" to continue', required=True)
def cli_app_def():
    #print(quit_or_enter)
    print("Wlecome to CLI_APP using Python")
    val = \
        input("Type 'quit' anytime to quit or press 'Enter' to continue: ")
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
            print('\n\nHere ALL the Searchable Fields of ',str(file_name))
            print(all_searchable_fields)
        elif value == 'quit':
            return
        else:
            print('Next time enter correct option')