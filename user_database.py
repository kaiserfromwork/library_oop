# Database
#class imports
# module imports
import json

# FILENAME = "user_database.txt"
FILENAME = "user_database.json"

class UserDatabase():

    def __init__(self):
        self.user_database_info = self.load_user_database()  # storing contents of JSON file

    
    def __str__(self):
        return str(self.user_database_info)


    def load_user_database(self):
        """Retrieves information from user database.
        
        Return: 
            Returns information from JSON file if file exists, otherwise returns an empty dict

        """
        
        try:
            with open(FILENAME, "r") as file:
                for line in file:   
                    return json.loads(line)
                
        except (FileNotFoundError, json.JSONDecodeError) as error:
            print(f"Error loading user info from database: {error}")
            return {}
        
    def update_user_database(self, user_database):
        """Updates user database
        
        Keyword arguments:
            user_database (list) -- user database
        
        Return: 
            Return true if file written successfully and false otherwise
        """
        
        if user_database:
            try:
                with open(FILENAME, "w") as file:
                    json.dump(user_database, file)
                return True
            except (OSError, json.JSONDecodeError) as error:
                print("Error while updating database: {error}")
                return False



    def save_user_to_database(self, user):
        """Saves information of user to database
        
        Keyword arguments:
        user (obj) -- user object
        
        Return: 
            return False if fails to write to file
        """
        
        user_database = self.user_database_info # returning JSON from file as a dict
        id = user.get_user_id() # getting user id user getter

        # Creating dict to append to JSON file
        new_dict = {id: [user.name, user.surname, user.borrowed_books]}
        
        # checking if JSON file is empty, if file is empty it creates a new list
        if user_database:
            user_database.append(new_dict)
        else:
            user_database = [new_dict]

        # Writing to JSON file
        try:
            with open(FILENAME, "w") as file:
                json.dump(user_database, file)

        except (OSError, json.JSONDecodeError) as error:
            print(f"Error saving user to database: {error}")
            return False
        

