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
        
        # Reading from JSON file
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
                
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
        
        # Writing to JSON file
        try:
            with open(FILENAME, "w") as file:
                json.dump(user_database, file, indent=4)
            return True
        except (OSError, json.JSONDecodeError) as error:
            print("Error while updating database: {error}")
            return False


        


