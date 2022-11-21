# search_cli_app
The complete source code of CLI_App. This app is about reading JSON file, do searching and see all the searchable fields

# 1. Create Virtual Enviorment

Steps to create Virtual Enviorment:
    
    py -m venv env
    
    .\env\Scripts\activate
    
# 2. Create .egg-info file
egg-info file is to contain the project meta-data

Step to create egg-info file

    cd Python_CLI_APP
    
    pip install --editable .
    
# 3. Run the project:

    cd ..
    
    app


# Each File Description:
1. cli_app.py

    This is where the code will start. It contain the main function

2. setup.py

    This file is to maintain version, packages and entry-points 

3. read_json.py

    Uses OOP concept. This file contain abstract class with two abstract methods

4. search.py 

    OOP concept, this file contain Multiple Inheritance to do search on any selected JSON file

