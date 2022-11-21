#!/usr/bin/python
# -*- coding: utf-8 -*-
import click
from read_json import users, tickets, organizations
from search import search

# main function
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
            
            # Table options
            choice = \
                input('''
                      Select any option:
                        * 1) Users
                        * 2) Tickets
                        * 3) Organizations
                    ''')
            if choice == str(1):
                u_obj = search()
                file_name, data = u_obj.read_users()
                u_obj.search_fun(data, file_name)
                
            elif choice == str(2):
                t_obj = search()
                file_name, data = t_obj.read_tickets()
                t_obj.search_fun(data, file_name)
                
            elif choice == str(3):
                o_obj = search()
                file_name, data = o_obj.read_organizations()
                o_obj.search_fun(data, file_name)
            
        elif value == str(2):
            # Table options
            choice = \
                input('''
                      Select any option:
                        * 1) Users
                        * 2) Tickets
                        * 3) Organizations
                    ''')
            
            if choice == str(1):
                u_obj = users()
                file_name, data = u_obj.read_json()
                u_obj.get_all_searchable_fields(data, file_name)
            
            elif choice == str(2):
                t_obj = tickets()
                file_name, data = t_obj.read_json()
                t_obj.get_all_searchable_fields(data, file_name)
            
            elif choice == str(3):
                o_obj = organizations()
                file_name, data = o_obj.read_json()
                o_obj.get_all_searchable_fields(data, file_name)
            
        elif value == 'quit':
            print('\nHave a nice day')
        
        else:
            print('Next time enter correct option')