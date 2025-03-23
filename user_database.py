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
                    my_list.append(json.loads(line))
            return my_list
        except (FileNotFoundError, json.JSONDecodeError) as error:
            print(f"Error loading user info from database: {error}")
            return {}



    def save_user_info(user_info):
        try:
            with open(FILENAME, "a") as file:
                # writing to text file, dumps() turn dict into json string + \n for better reading in load_user_database()
                file.write(json.dumps(user_info) + "\n")
                # json.dump(user_info + "\n", file)

            return True
            
        except (OSError, json.JSONDecodeError) as error:
            print(f"Error saving user to database: {error}")
            return False