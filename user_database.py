# Database
#class imports
# module imports
import json

# FILENAME = "user_database.txt"
FILENAME = "user_database.json"

class UserDatabase():

    def __init__(self):
        self.user_database_info = self.load_user_database()

    
    def __str__(self):
        return str(self.user_database_info)


    def load_user_database(self):
        my_list = []
        try:
            with open(FILENAME, "r") as file:
                # return json.load(file)
                for line in file:   
                    return json.loads(line)
                    # my_list.append(json.loads(line).strip())
            # return my_list
        except (FileNotFoundError, json.JSONDecodeError) as error:
            print(f"Error loading user info from database: {error}")
            return {}



    def save_user_info(self, user):
        user_database = self.user_database_info # returning JSON from file as a dict
        print(user_database)
        id = user.get_user_id()
        new_dict = {id: [user.name, user.surname, user.borrowed_books]}
        user_database.append(new_dict)
        # user_database[id] = "user"
        try:
            with open(FILENAME, "w") as file:
                json.dump(user_database, file)
        except (OSError, json.JSONDecodeError) as error:
            print(f"Error saving user to database: {error}")
            return False